# Package indispensable
import pandas as pd
import numpy as np
import xlsxwriter

# Package traitement de la données
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import  accuracy_score, classification_report
from keras.layers import SpatialDropout1D
from keras_preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
import nltk
from collections import Counter
## Nettoyage
import gensim

## Modèle
from sklearn.linear_model import LogisticRegression
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras import layers
from xgboost import XGBClassifier
import lightgbm as lgbm

## Package nécessaire pour open AI
import backoff
import openai

##### ----------------------------------------------------------- Fonction de prétraitement du prompt ----------------------------------
def sent_to_words(sentences):
    """
    Convertit une phrase en une liste de mots les plus pertinents

    Arguments :
    sentences : str ou list[str]
        La phrase ou la liste de phrases à convertir en mots.

    Renvoie :
    list[list[str]]
        Une liste de listes de mots, où chaque liste interne représente les mots d'une phrase qui sont les plus pertinents

    Exemple :
    >>> sentence = "Je suis un exemple. p"
    >>> sent_to_words(sentence)
    [['je', 'suis', 'un', 'exemple']]
    
    """
    yield(gensim.utils.simple_preprocess(str(sentences), deacc=True)) 
    

def traitement(df):
    """
    Effectue le prétraitement du texte sur les colonnes spécifiées d'un DataFrame.

    Args:
        df (DataFrame): Le DataFrame contenant les données à prétraiter.
        text_columns (list): Une liste des noms des colonnes contenant le texte à prétraiter.

    Returns:
        DataFrame: Le DataFrame modifié avec les prétraitements appliqués sur les colonnes spécifiées.
    """
    # Supprime les valeurs manquantes et les doublons
    df.drop_duplicates(inplace=True)
    df.dropna(inplace  = True)   

    #Removing URLs with a regular expression
    url_pattern = r'https?://\S+|www\.\S+'

    # Remove Emails
    clean_email= r'\S*@\S*\s?'

    # Keep only word
    clean_regex = r"[^a-zA-Z\s]+"

    column = "prompt"
    df[column] = df[column].str.lower().replace(url_pattern, '', regex=True)
    df[column] = df[column].str.lower().replace(clean_email, '', regex=True)
    df[column] = df[column].str.lower().replace(clean_regex, '', regex=True)

    df[column] = df[column].apply(nltk.word_tokenize)
    
    df[column] = df[column].apply(lambda x: ' '.join(x)) 

    df[column] = df[column].apply(lambda x: " ".join(list(sent_to_words(str(x)))[0]))

    return df  
    

### -------------------------------- Métriques de comparaisons ------------------------------
def metrics_nlp(y_test, pred):
    """
    Calcule différentes métriques de performance pour un modèle de traitement du langage naturel (NLP).
    
    Args:
        y_test (array-like): Les vraies étiquettes (labels) des données de test.
        pred (array-like): Les prédictions faites par le modèle.
    
    Returns:
        tuple: Un tuple contenant les métriques de performance suivantes :
            - Précision (accuracy) en pourcentage.
            - Précision pondérée (weighted average precision) en pourcentage.
            - Rappel pondéré (weighted average recall) en pourcentage.
            - Score F1 pondéré (weighted average F1-score) en pourcentage.
    """
    # accuracy: (tp + tn) / (p + n)
    accuracy = accuracy_score(y_test, pred)* 100
    # print('Accuracy: %f' % accuracy)
    
    # precision tp / (tp + fp)
    classif_report= classification_report(y_test, pred, output_dict=True)
    # print('Rapport de classification: ', classif_report)
    
    return (accuracy, classif_report['weighted avg']['precision']*100, classif_report['weighted avg']['recall']*100, classif_report['weighted avg']['f1-score']*100)


# Modele Logit
def Logit_model(X_train, y_train, X_test):
    
    """
    Entraîne un modèle de régression logistique et effectue des prédictions sur les données de test.
    Args:
        X_train (array-like): Les données d'entraînement, les caractéristiques.
        y_train (array-like): Les données d'entraînement, les étiquettes.
        X_test (array-like): Les données de test, les caractéristiques.
    
    Returns:
        array-like: Les prédictions générées par le modèle de régression logistique.
    """
    
    # Vectorisation
    cv = CountVectorizer()
    X_train_cv = cv.fit_transform(X_train)
    X_test_cv = cv.transform(X_test)
    
    # Training Logistic Regression model
    lr = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter= 200)
    lr.fit(X_train_cv, y_train)

    
    # generate predictions
    prediction = lr.predict(X_test_cv)
    
    return prediction

# ----------------------------------------------------------   Modele Xgboost
def Xgboost_model(X_train, y_train, X_test):
    """
    Entraîne un modèle XGBOOST et effectue des prédictions sur les données de test.
    
    Args:
        X_train (array-like): Les données d'entraînement, les caractéristiques.
        y_train (array-like): Les données d'entraînement, les étiquettes.
        X_test (array-like): Les données de test, les caractéristiques.
    
    Returns:
        array-like: Les prédictions générées par le modèle de régression logistique.
    """
    ## Vectorisation 
    cv = CountVectorizer()

    # Encodage
    X_train_cv = cv.fit_transform(X_train)
    label_encoder = LabelEncoder()
    y_train_encode = label_encoder.fit_transform(y_train.values)# , fit_params)y_train.map({"positive": 0, "negative":1, "neutral": 2})
    
    # Train the xgboost model
    clf_CGB = XGBClassifier(max_depth= 6, n_estimators= 1000) #objective='multi:softmax', num_class=3, 
    clf_CGB.fit(X_train_cv, y_train_encode)
    
    # Data validation
    X_test_cv = cv.transform(X_test)

    # generate predictions
    decoded_predictions = clf_CGB.predict(X_test_cv)
    
    # Décodage des prédictions
    prediction = label_encoder.inverse_transform(decoded_predictions)
    return prediction

# -------------------------------------------------  Modele Lgbm
## Adapter seulement au multiclass, faudra le repréciser après
def Lgbm_model(X_train, y_train, X_test):
    """
    Entraîne un modèle LGBM et effectue des prédictions sur les données de test.
    
    Args:
        X_train (array-like): Les données d'entraînement, les caractéristiques.
        y_train (array-like): Les données d'entraînement, les étiquettes.
        X_test (array-like): Les données de test, les caractéristiques.
    
    Returns:
        array-like: Les prédictions générées par le modèle de régression logistique.
    """
    # Vectorisation avec la méthode idf
    tfidf_vec = TfidfVectorizer(dtype=np.float32, sublinear_tf=True, use_idf=True, smooth_idf=True)
    X_train_cv = tfidf_vec.fit_transform(X_train)
    
    # Modèle lgbm
    clf_LGBM = lgbm.LGBMClassifier(boosting = 'gbdt', 
              verbose=-1,
              # objective = 'multiclass', 
              max_depth = 20,
              max_bin = 1000, 
              num_leaves = 150, 
              n_estimators = 120,
              learning_rate = 0.1)#,
              # metric= "multi_logloss")
    clf_LGBM.fit(X_train_cv, y_train)
    
    ## Validation
    X_test_cv = tfidf_vec.transform(X_test)
    prediction = clf_LGBM.predict(X_test_cv)
    
    return prediction


def Keras_model(X_train, y_train, X_test):
    """
    Entraîne un modèle de reséaux de neurones via l'API KERAS de Tensorflow et effectue des prédictions sur les données de test.
    
    Args:
        X_train (array-like): Les données d'entraînement, les caractéristiques.
        y_train (array-like): Les données d'entraînement, les étiquettes.
        X_test (array-like): Les données de test, les caractéristiques.
    
    Returns:
        array-like: Les prédictions générées par le modèle de régression logistique.
    """
    train_labels = y_train.values

    # Tokenization
    tokenizer = Tokenizer(num_words=1000)
    tokenizer.fit_on_texts(X_train)
    train_sequences = tokenizer.texts_to_sequences(X_train)

    # Padding
    train_data = pad_sequences(train_sequences, maxlen=200)

    # Encodage des labels
    label_encoder = LabelEncoder()
    train_labels_encoded = label_encoder.fit_transform(train_labels)
    train_labels_encoded = np_utils.to_categorical(train_labels_encoded)
    
    ## Modèle LSTM
    model = Sequential()
    model.add(layers.Embedding(1000, 20, input_length = 200)) #The embedding layer
    model.add(SpatialDropout1D(0.4))
    model.add(layers.LSTM(15, dropout=0.5)) #Our LSTM layer
    model.add(layers.Dense(3, activation='softmax'))
    
    # Compilation du modèle
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    # Entraînement du modèle
    model.fit(train_data, train_labels_encoded, epochs=10)
    
    # Tokenization des données de test
    test_sequences = tokenizer.texts_to_sequences(X_test)
    test_data = pad_sequences(test_sequences, maxlen=200)
    
    # Prédictions
    predictions = model.predict(test_data)
    
    # Décodage des prédictions
    decoded_predictions = np.argmax(predictions, axis=1)
    prediction = label_encoder.inverse_transform(decoded_predictions)
        
    return prediction

# Fonction pour lancer le modèle Azure openai
def generer_texte(engine, prompt):
    """
    Génère un texte en utilisant le moteur spécifié open AI et le prompt donné.
    
    Args:
        engine (str): Le nom ou l'ID du moteur OpenAI à utiliser pour la génération du texte.
        prompt (str): La phrase ou le texte qui sert de base pour générer le texte.
    
    Returns:
        str: Le texte généré par le modèle OpenAI.
    """
    response = openai.Completion.create(
      engine = engine,
      prompt = prompt,
      temperature=0,
      max_tokens=1,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      best_of=1,
      stop= None)#["-","->", ">", "subject", "request", "g", "*"]
    return response.choices[0].text.strip()

def to_delete_list(liste_to_delete, X_test):
    """
    Effectue une prédiction en utilisant un modèle Azure spécifié sur les données de test.

    Args:
        model_spe (str): L'ID du déploiement du modèle Azure à utiliser pour la prédiction.
        X_test (DataFrame): Le DataFrame contenant les données de test.
        y_test (array): Le tableau contenant les étiquettes des données de test.

    Returns:
        tuple: Un tuple contenant les prédictions, le DataFrame X_test modifié et le tableau y_test modifié.
    """
    labels_to_delete= []
    for i in liste_to_delete:
        labels_to_delete.append(X_test.iloc[i:i+1].index[0]) 
    if labels_to_delete == []:
        print("RAS")
    return labels_to_delete


@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def azure_model(model_spe, X_test, y_test):
    """
    Effectue la prédiction en utilisant le modèle Azure Open AI pour classer des textes.
    
    Args:
        model_spe (str): L'ID du déploiement du modèle Azure ML.
        X_test (array-like): Les textes à classer.
        y_test (array-like): Les étiquettes de classe réelles correspondant aux textes.
    
    Returns:
        tuple: Un tuple contenant les prédictions générées pour les textes donnés,
               le DataFrame X_test sans les lignes qui ont provoqué des erreurs d'API,
               et le DataFrame y_test correspondant.
    """
    
    # Configuration de l'API OpenAI Azure
    openai.api_key = "5754e41be80b4d8298b706fd56c86b85"  # Clé Groupe
    openai.api_base = "https://groupedatascience.openai.azure.com/" # endpoint
    openai.api_type = "azure"
    openai.api_version = '2022-12-01'    #Pourrait être amené à être modifié dans les versions récentes
    
    # Utilisation de l'id du déploiement pour le modèle voulu
    deployment_id = model_spe 
    
    textes = []
    rows_to_delete_1 = []
    rows_to_delete_2 = []
    index_texte=[]
    
    
    for index, lines in enumerate(X_test): 
      try:
        start_phrase= f"Classify the following news tweets only into 1 of the specific following categories: positive, negative, neutral\n\nTweet: \"@VirginAmerica What @dhepburn said.\"\nsentiment: neutral\n\nTweet: \"@VirginAmerica plus you've added commercials to the experience... tacky.\"\nsentiment: positive\n\nTweet: \"@VirginAmerica it's really aggressive to blast obnoxious \"entertainment\" in your guests' faces &amp; they have little recourse\"\nsentiment: negative\n\nTweet:\ {lines}\n\nsentiment:"    
        texte_genere = generer_texte(deployment_id, start_phrase)        
        if texte_genere in ["positive", "negative", "neutral"]: 
            textes.append(texte_genere)
            index_texte.append(index)
        else:
           rows_to_delete_2.append(index) 
      except openai.error.APIError as e:
        #Handle API error, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        rows_to_delete_1.append(index)
        pass
      except openai.error.InvalidRequestError as e:
      #Handle invalid request error, e.g. validate parameters or log
        print(f"OpenAI API request was invalid: {e}")
        rows_to_delete_2.append(index)
        pass
    
    ### A supprimer
    index_to_delete_1 = to_delete_list(rows_to_delete_1, X_test)
    index_to_delete_2 = to_delete_list(rows_to_delete_2, X_test)
    
    # Données de validation
    X_test = X_test.drop(labels = index_to_delete_1 + index_to_delete_2, axis=0)
    y_test = y_test.drop(labels = index_to_delete_1 + index_to_delete_2, axis=0)

    predictions = textes
    print("Nombre de modalités dans les prédictions obtenues",dict(Counter(textes).items()))
    return (predictions, X_test, y_test)
    

## --------------------------------------------------------------- Utilisation des modèles dans une seule fonction ------------------------------

def get_prediction(data_init, var_cible= "completion", N_seed = [123], modeles = ["text-davinci-003", "custom-curie-model-sentiment", "logit", "xgboost", "lgbm", "keras"] ): 
    """
    Effectue des prédictions sur les données en utilisant différents modèles et renvoie les résultats et les valeurs cibles réelles.
    
    Args:
        data_init (DataFrame): Le DataFrame contenant les données à utiliser pour les prédictions.
        var_cible (str, optional): Le nom de la variable cible à prédire. Par défaut, "completion".
        N_seed (list, optional): Une liste de graines aléatoires à utiliser pour diviser les données en ensembles d'entraînement et de test. Par défaut, [123].
        modeles (list, optional): Une liste de noms de modèles à utiliser pour les prédictions. Par défaut, ["text-davinci-003", "custom-curie-model-sentiment", "logit", "xgboost", "lgbm", "keras"].
    
    Returns:
        tuple: Un tuple contenant les résultats des prédictions pour chaque modèle et les valeurs cibles réelles.
    """
    data = data_init.copy()
    resultat = []
    
    for my_seed in N_seed :
        # Application des traitement 
        data = traitement(data) 
        
        ## Echantillon train - test
        y = data[var_cible]
        X = data[data.loc[:, data.columns != var_cible].columns[0]]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= my_seed)      
        
        
        # Pour chaque modèle, on va tirer les prédictions et le nom du modèle afin de les mettre dans un dataset
        for modele in modeles:
            if modele == "text-davinci-003":
                print ("-----",modele,"en cours-----")
                prediction, X_test, y_test = azure_model(modele, X_test, y_test)
                resultat.append([modele, prediction])
                print("y_davinci_sortie", y_test.shape)
                
            elif modele == "custom-curie-model-sentiment":
                print ("-----",modele,"en cours-----")
                prediction, X_test, y_test = azure_model(modele, X_test, y_test)
                resultat.append([modele, prediction])
                
            elif modele == "logit":
                print ("-----",modele," en cours-----")
                prediction = Logit_model(X_train, y_train, X_test)
                resultat.append([modele, prediction])
                
            elif modele == "xgboost":
                print ("-----",modele,"en cours-----")
                prediction = Xgboost_model(X_train, y_train, X_test)
                resultat.append([modele, prediction])
                
            elif modele == "lgbm":
                print ("-----",modele,"en cours-----")
                prediction = Lgbm_model(X_train, y_train, X_test)
                resultat.append([modele, prediction])
                
            elif modele == "keras" :
                print ("-----",modele,"en cours-----")
                prediction = Keras_model(X_train, y_train, X_test)
                resultat.append([modele, prediction])
            else:
                print("Inserer un modèle valide")
                return None
            
    return (resultat, y_test)


## -------------------------------------------  Fonction qui permet de sortir les métriques sous forme de liste
def table_methode(name_dataset, resultat, y_test):
    metriques = []
    for i in range(0,len(resultat)):

        accuracy, precision, recall, f1_score = metrics_nlp(y_test, resultat[i][1])
        metriques.append([name_dataset, len(y_test), resultat[i][0], accuracy, precision, recall, f1_score])

    metriques_df = pd.DataFrame(metriques)
    metriques_df.columns = ["Datasets", "Taille dataset - Test" ,"Modele", "Accuracy", "Precision", "Recall", "F1score"]
    return metriques_df
    
########### --------------------------------------------------------------------------------------------------------------------------------
"""
Le nom des différents modèles et leur spécificité:
    - text_davinci-003: MOdle préentrainé d'Azure open AI
    - custom-curie-model-sentiment: Modèle curie fine-tuné pour l'analyse de sentiment
    - logit: Regression logitique
    - xgboost: Modèle Gradient boosting
    - lgbm: Modèle light gbm
    - keras: Réseau de neurone avec l'API Keras
    
    A noter que les modèles pour failiter la compréhension et le temps de calculs,
    les modèles ont été crées via Open AI. Il est donc possible d'en creer d'autres et de les tester
    Bien entendu il est important d'inserer un prompt adapter.
    
    NB: Les modèles d'Open AI peuvent poser des soucis au niveau des prédictions car il peuvent générer plus de prédiction qu'il ne le faut
    Il faut donc vérifier les prédictions généré et apporter des modifications si nécessaire
"""
path = r'C:\Users\DSONNE\Desktop\Azure openAI\Datasets sentiments'


#### Dataset 1: Tweets csv
data_airline = pd.read_csv(path + '\Tweets.csv', sep=",")
data_airline = data_airline[['text', 'airline_sentiment']].rename(columns = {'text':'prompt', "airline_sentiment": "completion"})

#### Dataset 2: Financial news
data_gop = pd.read_csv(path + '\\all-data.csv', sep=",", encoding = "ISO-8859-1", names=["completion", "prompt"], header=None)

### Dataset 3: Silicone
data_silicone = pd.read_parquet(path + '\silicone-train.parquet', engine='pyarrow')
data_silicone = data_silicone[['Utterance', 'Emotion']].rename(columns = {'Utterance':'prompt', "Emotion": "completion"})
data_silicone = data_silicone[data_silicone["completion"] != "surprise"]
data_silicone["completion"] = data_silicone["completion"].map({"no emotion": "neutral", "happiness": "positive", "sadness": "negative", "anger": "negative", "disgust": "negative", "fear": "negative"})
### Dataset 4: Kaggle https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset?select=train.csv
data_kaggle = pd.read_csv(path + '\\train.csv', sep=",", encoding = "ISO-8859-1")
data_kaggle = data_kaggle[['text', 'sentiment']].rename(columns = {'text':'prompt', "sentiment": "completion"})

### Dictionnaire des datasets
Datasets = {"data_airline": data_airline, "data_silicone": data_silicone, "data_gop": data_gop}
All_metriques = pd.DataFrame()

### Obtention des résultats
for key, values in Datasets.items():
    print("Jeu de données:", key)
    resultat, y_test = get_prediction(values, var_cible= "completion", N_seed = [123], modeles = ["logit", "lgbm", "xgboost", "keras"])#"text-davinci-003", "custom-curie-model-sentiment", 
    metriques_df = table_methode(key, resultat, y_test)
    All_metriques = pd.concat([All_metriques,metriques_df])


All_modeles= All_metriques.groupby("Modele").mean("Accuracy")


# Write each dataframe to a different worksheet.
writer = pd.ExcelWriter("Résultats analyse des sentiments.xlsx", engine="xlsxwriter")

# Write each dataframe to a different worksheet.
All_metriques.to_excel(writer, sheet_name="All datasets")
All_modeles.to_excel(writer, sheet_name="Mean models")


# Close the Pandas Excel writer and output the Excel file.
writer.close()
























