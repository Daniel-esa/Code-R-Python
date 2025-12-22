# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:59:31 2021

@author: ADUBOIS
"""

##############################################################################
##############################################################################
# 1.2 - CONCEPTS DE BASE
##############################################################################
##############################################################################

# ---------------------- #
# Typages numériques 
# ---------------------- #
 
entier = 10
print(type(entier))

reel = 10.5
print(type(reel))

piege = 10.0
print(type(piege))

nombre = 41
nombre = nombre + 2 # Addition
nombre = nombre - 2 # Soustraction
print('1. Multiplication :', nombre * 2)
print('2. Division :', nombre / 2)
print('3. Exposant :', nombre ** 2)
print('4. Partie entière de la division par 2 :', nombre // 2)
print('5. Partie restante de la division par 2 :', nombre % 2)
  
# ---------------------- #
# Typage booléen 
# ---------------------- #   
   
vrai = True
faux = False
print(type(vrai),', ',type(faux))

a = bool(0)
b = bool(1)
print(type(a), ', ', type(b))

x = (5>1)
y = (5<1)
z = (5 == 1)
print('x =', x)
print('y =', y)
print('z =', z)

# ------------------------- #
# Typage chaine de caractères 
# ------------------------- # 

texte1 = 'Paris, Paris outragé, Paris brisé,'
texte2 = "Paris martyrisé mais Paris libéré!"
print(type(texte1))

#Manipulation de texte
print('5 premiers caractères de texte1 :',texte1[0:5])
print('5 premiers caractères de texte1 :',texte1[:5])
print('6 derniers caractères de texte1 :',texte1[28:])
print('6 derniers caractères de texte1 :',texte1[-6:])


print('Extraire le sous-texte "Paris outragé" de texte1 :',texte1[7:20])

#Concaténation de textes
print(texte1 + texte2)

#	print('Concaténer "outragé" et "libéré" de texte1 et texte2 : ', ???) 

#Multiplication de texte
print(2*texte1)

# ------------------------- #
# Instanciation et affectation 
# ------------------------- #

#typage automatique
a = 1
#typage explicite 
a = float(1)

#même valeur pour plusieurs variables
a = b = 2.5
#affectations parallèles
a, b = 2.5, 3.2
# Le plus couramment utilisé : 1 instruction = 1 ligne
a = 1
b = 5
a= 3 + b

# ------------------------- #
# Transtypage  
# ------------------------- #

#Conversion numérique
a = '12' # a est une chaine de caractère 
b = float(a) #  b = 12.0
print(type(a)) 
print(type(b))

#Conversion en booléen
a = bool('False') #  a = True 
b = bool(0)       #  b = False
print(type(a)) 
print(type(b))

#Conversion en chaine de caractère 
a= str(15) #  a = '15'
print(type(a))

# ------------------------- #
# L'instruction « IF, ELIF, ELSE »   
# ------------------------- #

#Prix HT
pht = 10.0
code = 4

#Saisie à la console du code produit 
pht = int(input('Code produit : '))

#Action conditionnelle
if (code == 1):
    pttc = pht  * 1.055
elif (code == 2):
    pttc = pht * 1.1
else:
    pttc = pht * 1.2
    
#Affichage avec transtypage
print("Prix TTC : " + str(pttc))

# ------------------------- #
# Boucle "For"  
# ------------------------- #

#On choisit la valeur limite
n = int(input("n : "))
if n>10**6 :
    print('Vous avez choisi un nombre trop grand.')
    n = 10**6
    print('n a été fixé à 1000000')

#Initialisation 
somme_impaire = 0
somme_totale = 0

#Calcul de la somme
for i in range(1,n+1): #n+1 car range(1,n) s'arrête à n-1
    #Somme des valeurs impaires
    if (i % 2 == 1):
        somme_impaire = somme_impaire + i
    #On quitte le if mais on reste dans la boucle for 
    somme_totale = somme_totale + i 

#On sort de la boucle for et on affiche les résultats
print("Somme des valeurs impaires :" + str(somme_impaire))
print("Somme totale : " + str(somme_totale))

# ------------------------- #
# L'Instruction « break » 
# ------------------------- #

nb = 100 

total = 0
for i in range(nb+1):
    if nb>10: 
        break
    else:
        total +=i 

print('Le total des nombre entre 1 et nb est : ',total)

# ------------------------- #
# L'Instruction « continue » 
# ------------------------- #

nb = 10
total = 0
for i in range(nb+1):
    if i%2 != 0:
        continue
    total +=i 

print('Résultat des nombres pairs entre 1 et 10 : ', total)

# ------------------------- #
# L'Instruction « pass » 
# ------------------------- #

nb = 10
total = 0
for i in range(nb+1):
    if i%2 != 0:
        pass
    else:
        total +=i 

print('Résultat des nombres pairs entre 1 et 10 : ', total)

# ------------------------- #
# Boucle « While » : exemple d'application
# ------------------------- #

n = int(input("n : "))

#Initialisation 
somme_impaire = 0
somme_totale = 0

#Calcul de la somme et de la sommedes valeurs impaires
i = 0 #il faut initialiser i
while i <= n : # cette fois n car on utilise "<="
    #Somme des valeurs impaires 
    if (i % 2 == 1):
        somme_impaire = somme_impaire + i
    #On quitte le if mais on reste dans la boucle while 
    somme_totale = somme_totale + i 
    i = i + 1

#On sort de la boucle while et on affiche les résultats 
print("Somme des valeurs impaires :", str(somme_impaire))
print("Somme totale : ", somme_totale)

# ------------------------- #
# Boucle « While » avec « break »
# ------------------------- #

nb = input("Entrez un nombre entier entre 1 et 10 : ")
nb = int(nb)

total = 0
while True :
    total += nb 
    nb -= 1
    if nb == 0 : break
    
print('Le total des nombres entre 1 et nb est :',total)

# ------------------------- #
# Les tuples
# ------------------------- #

#Création d'un tuple
nuplet = ('caractères',12,True,1.25)

#Identifier un élément du tuple 
print('2ème élément de nuplet :',nuplet[2])

# Modification d'un tuple impossible car objet non mutable
nuplet[2] = 4

# ------------------------- #
# Opérations sur tuples
# ------------------------- #

t1 = (2,3,4,5)

print(t1) #  (2,3,4,5)
len(t1) #  4 (correspond à la taille du tuple)
t1[0] # 2 (accès aux éléments grâce aux indices, le premier indice est le 0)
t1[2] = 10 #  Error (les éléments d'un tuple ne sont pas modifiables)
t1[1:3] #  (3,4)(récupère de l'indice 1 inclus à l'indice 3 non inclus. (3,4)est un tuple)
t1[:2] #  (2,3)(les 2 premiers éléments)
t1[-1] #  5 (le dernier élément, indice négatif)
t1[-2:] #  (4, 5)(les 2 derniers éléments)

t2 = (2,3,3,4)
set(t2) #  {2, 3, 4}  avec type({2, 3, 4})égal à « set »

t1 = (1,2,3,4)
t2 = (5,2,4)
t1 + t2 #  (1, 2, 3, 4, 5, 2, 4)

2 * t2 #  (5, 2, 4, 5, 2, 4) 

t3 = ('caractères',12,True,1.25)

t4= ((2,3,4),(6,7,9),(2,3))

t = (2,3,6,8,6)

# ------------------------- #
# Les listes
# ------------------------- #

list1 = [2,3,4,5] #  les [ ] définissent le type liste et les éléments sont séparés par une virgule
list1[1] = 10 #  list1 = [2,10,4,5]

list1.append(33) #  list1 = [2,10,4,5,33] 
list1.insert(1,45) #  list1 = [2,45,10,4,5,33]
del list1[2] #  list1 = [2,45,4,5,33]
list1.pop(1) #  list1 = [2,4,5,33] ; a = 45
list1.reverse() #  list1 = [33,5,4,2]
list1.sort(reverse = False) 
list1.extend([6,7]) # / list1 = list1 + [6,7] # list1 = [33,5,4,2,6,7] 
['A','B','C'] + [1,2,3] + [True,False] #  ['A', 'B', 'C', 1, 2, 3, True, False]
list1.remove(6) #  list1 = [2,3,8,6]
list(set(['A','B','A','A','C','B'])) #  ['A', 'B', 'C']

l3 = [1,2,3]
#Affectation
l4 = l3 
#Modification d'une valeur 
l4[1] = 99
print(l4)
print(l3)

l3 = [1,2,3]
#Copie de la valeur
l4 = l3.copy()
#Modification d'une valeur 
l4[1] = 99
print(l4)
print(l3)

# ------------------------- #
# Les listes : slicing
# ------------------------- #

couleurs = ['bleu','blanc','rouge','gris','jaune','orange']

#Extraire des éléments
couleurs[1]   # 'blanc'
couleurs[-3]  # 'gris'
couleurs[:3]  # ['bleu', 'blanc', 'rouge']
couleurs[:-2] # ['bleu', 'blanc', 'rouge', 'gris']
couleurs[2:4] # ['rouge', 'gris']

#Remplacer des éléments
couleurs[0] = 'vert'
couleurs[3:] = ['A','B','C']
couleurs # ['vert', 'blanc', 'rouge', 'A', 'B', 'C']

#Supprimer des éléments
del couleurs[3]   # ['vert', 'blanc', 'rouge', 'B', 'C']
del couleurs[-2:] # ['vert', 'blanc', 'rouge']

# Inverser une liste
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
nums[::-1] # [90, 80, 70, 60, 50, 40, 30, 20, 10]

# ------------------------- #
# Les listes : optimisation d'écriture
# ------------------------- #

liste = [1,5,8,12,7]
resultat = []
for v in liste:
    resultat.append(v**2)
    
liste = [1,5,8,12,7]
resultat = [v**2 for v in liste]

liste = [1,5,8,12,7]
resultat = []
for v in liste:
    if (v%2==0):
        resultat.append(v**2)
        
liste = [1,5,8,12,7]
resultat = [v**2 for v in liste if (v%2==0)]

# ------------------------- #
# Les ensembles
# ------------------------- #

d = {1,2,3}

ensemble = set([1,2,3])  # set permet de transformer une liste en un ensemble
ensemble_gele = frozenset([1,2,3])

print("Set :",ensemble,type(ensemble))
print("Frozen set :",ensemble_gele,type(ensemble_gele))

# ------------------------- #
# Les dictionnaires
# ------------------------- #

d1 = {'nom':'Raoult', 'prénom':'Didier','age':68}

print("Clé :",d1.keys())
print("Valeur :",d1.values())
print("Item :",d1.items())

d2 = {('Pierre',56):['Directeur',1253,True],('Paul',44):['Employé',100,False]}
print(d2.keys())
print(d2.values())

# Création d'un dictionnaire 
dic = {'Jean' : 17, 'Paul' : 20, 'Léo' : 16}
print(dic) # ou print(dic.items())

print(len(dic)) #  3

print(dic.keys()) #  ['Léo', 'Jean', 'Paul']

print(dic.values()) #  [16, 17, 20]

print(dic['Jean']) # 17
# ou print(d1;get('Jean'))

print(dic['Charles']) # Erreur (Charles n'est pas une clé)

#Copier le dictionnaire :
dic2 = dic.copy()

#Vider le dictionnaire :
dic.clear()
print(dic) # {}

dic = dic2.copy()
del dic2
#Modification :
dic['Léo'] = 23
print(dic) #  {'Léo': 23, 'Jean': 17, 'Paul': 20}

#Ajout d'un élément
dic['Max'] = 45
print(dic) # {'Max': 45, 'Léo': 23, 'Jean': 17, 'Paul': 20}

# Ajout d'un bloc d'élément
dic.update({'Claire':43,'Caroline':39})
print(dic) #  {'Caroline': 39, 'Jean': 17, 'Claire': 43, 'Paul': 20, 'Max': 45, 'Léo': 23}

#Détecter la présence d'une clé 
test = 'Léo' in dic
print(test) #  True

#Suppression d'une clé 
del dic['Léo']
print(dic) # {'Caroline': 39, 'Jean': 17, 'Claire': 43, 'Paul': 20, 'Max': 45}


# ------------------------- #
# Les vecteurs
# ------------------------- #

import numpy as np # Import du package

#Création d'une matrice 3x5 avec des entiers de 0 à 14
a = np.arange(15).reshape(3,5) 

#Obtenir les dimensions de l'array
a.shape # (3, 5)

#Obtenir le rang de la matrice
a.ndim # 2

#Le type des éléments présents dans l'array
a.dtype.name # 'int32'

#Nombre d'éléments dans l'array
a.size # 15

#Création d'un array à l'aide de listes
b = np.array([[2,3,4],[6,7,8]]) 

#Création d'une matrice 3x4 de 0
np.zeros((3,4)) 

#Création d'une matrice avec 2 matrices 3x4 de 1
a = np.ones((2,3,4)) 

a[1,2,3] = 50*a[1,2,3] # Modification d'un élément (les indices commencent à 0)

'''Techniques de création de vecteur'''
np.arange(10,30,5) #--> array([10, 15, 20, 25])
np.arange(0,2,0.3) #--> array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
# 9 valeurs equidistantes de 0 à 2
np.linspace(0,2,9) # --> array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  , 
                                # 1.25,  1.5 ,  1.75,  2.  ])


'''Appliquer une fonction sur un vecteur'''

from numpy import pi
x = np.linspace(0,2*pi,100) # --> 100 points entre 0 et 2*pi
f = np.sin(x)               # On applique la fonction sin(x) sur les 100 points de x

'''Tracer un graphique rapidement'''
import matplotlib.pyplot as plt  # Package pour créer des graphiques
plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show

'''Création de vecteurs'''
a = np.array( [20,30,40,50] )
b = np.arange( 4 )  # --> array([0, 1, 2, 3])

'''Opérations entre vecteurs'''
c = a-b #-> array([20, 29, 38, 47])
b**2 # -->array([0, 1, 4, 9])
10*np.sin(a) # --> array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
a<35 #-->array([ True, True, False, False], dtype=bool)
a*b # --> array([  0,  30,  80, 150])

'''Création de matrices'''
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )

'''Opération sur les matrices'''
A*B    # Produit élément par élément
#array([[2, 0],
#       [0, 4]])

A.dot(B) # Produit matriciel
#array([[5, 4],
#       [3, 4]])
np.dot(A, B)  # Autre manière d'écrire le produit matriciel


a = np.random.random((2,3))
#array([[ 0.78492393,  0.93619717,  0.28750659],
#       [ 0.04839579,  0.08941263,  0.96451262]])

'''Somme des éléments'''
a.sum() # --> 3.1109487312709376

'''Min et max des éléments'''
a.min() #--> 0.048395787392701006
a.max() # --> 0.9645126204304354

'''Moyenne médiane quantilles'''
a.mean() # --> 0.51849145521182294
np.median(a) #--> 0.53621526026497179
np.nanpercentile(a, q = 10) # --> 0.068904209822096441

'''Exemple avec une matrice'''     
A = np.array( [[1,4], [0,1]] )
#array([[1, 4],
#       [0, 1]])
A.mean(axis = 0) #  axis = 0 --> les colonnes 
#array([ 0.5,  2.5])
A.mean(axis = 1) # axis = 1 --> les lignes
#array([ 2.5,  0.5])
A.mean() # Pas d'axis --> l'ensemble de la matrice
#1.5

# ------------------------- #
# Les fonctions
# ------------------------- #

# Si a est le max retourne a sinon retourne 100
def maxi(a,b) :
    if (a>b):
        e = a
    else :
        e = 100
    return(e)
        
c = 3
d = 10
print(maxi(c,d)) 
print(maxi(d,c)) 
print(maxi(a=c,b=d)) 
print(maxi(b=d,a=c))

#On calcule un prix

def f(prix,solde = False, red = 50):
    if solde == True :
        prix = prix - prix * red/100
    return(prix)

print(f(100))           
print(f(100,True)) 
print(f(100,True,75))


# Exemple avec des éléments simples
def non_mutable(x,y):
    x = x+3
    y = y-2
    print(x,y)
    
x = 4
y = 10
non_mutable(x,y)        # 7 8
print(x,y)              # 4 10


# Exemple avec des listes :
def mutable(l1,l2):
    l1.append(4)
    l2[0]= 0
    print(l1,l2)
    
l1 = [1,2]
l2 = [2,2,3]    
mutable(l1,l2)          # [1,2,4] [0,2,3]
print(l1,l2)            # [1,2,4] [0,2,3]


# ------------------------- #
# Les fonctions : retourner plusieurs valeurs
# ------------------------- #

def ordre(a,b) :
    if (a>b):
        return a,b
    else :
        return b,a

a= 10
b= 5
vmax , vmin = ordre(a,b)
print(vmax,vmin)            # 10 5
print(ordre(a,b))           # (10,5)
print(type(ordre(a,b)))     # <class 'tuple'>


def ordre_dic(a,b):
    if a > b :
        return( {'Max' : a, 'Min' : b})
    else :
        return({'Max' : b , 'Min' : a})
        
a = 10
b = 5
res = ordre_dic(a,b)    
print(res)              #{'Max': 10, 'Min': 5}
print(res['Max'])       #10
print(type(res))        #<class 'dict'>


def ordre_liste(a,b) :
    if (a>b):
        return [a,b]
    else :
        return [b,a]

a= 10
b= 5
res = ordre_liste(a,b)
print(res)            # [10,5]
print(res[0])           # 10
print(type(res))     # <class 'list'>

# ------------------------- #
# Les fonctions : variables locales et globales
# ------------------------- #

def remplace(v):
    x = v
    return(x)

x = 10
print(remplace(5))   #5
print(x)             #10


def remplace_2(v):
    x = x +v
    return(x)
    
x = 10
print(remplace_2(5))    #UnboundLocalError: local variable 'x' 
                        #referenced before assignment
print(x)                #10


def remplace_3(v):
    global x
    x = x + v
    return(x)
    
x = 10
print(remplace_3(5))    #15
print(x)                #15


# ------------------------- #
# Les fonctions : variables locales et globales
# ------------------------- #

#On définit la fonction globale
def glob(a):
    
    # On definit la fonction locale
    def loc(b):
        return(2*b)
    
    return(3*loc(a))
    
x = 10
print(glob(x)) #60
print(loc(x))  # NameError : name 'loc' is not defined

# ------------------------- #
# Les fonctions lambda
# ------------------------- #

list(map(lambda x:x**2,range(10)))

# ------------------------- #
# Les modules (ou packages)
# ------------------------- #

import math, random 
# Un nombre aléatoire entre 0 et 1
print(random.random())      # 0.07411960856255406
print(math.log(2))          # 0.6931471805599453

import math as m
import random as r
print(r.random())   # 0.9557576489937392
print(m.log(2))     # 0.6931471805599453

from math import log
from random import random
print(random())     # 0.7510624775356199
print(log(2))       # 0.6931471805599453

from math import *
print(log(2))       # 0.6931471805599453

# ------------------------- #
# Création d'un package
# ------------------------- #

#TVA 10%
def pttc_reduit(p):
    '''Retourne  le prix d'un produit toutes charges comprises
    avec une TVA réduite '''
    return(p*1.1)

#TVA 20%
def pttc_normal(p):
    '''Retourne  le prix d'un produit toutes charges comprises
    avec la TVA classique '''
    return(p*1.2)

# ------------------------- #
# Import package créé
# ------------------------- #

#On se  placer dans le répertoire où se trouve le package
import os
os.chdir(r'C:\Users\Documents\Slides de formation\Python')

# On importe le package
import tva
help(tva)
#Help on module tva:
#
#NAME
#    tva - # -*- coding: utf-8 -*-
#
#FUNCTIONS
#    pptc_normal(p)
#         Prix toutes charges comprises avec la TVA classique
#    
#    pttc_reduit(p)
#        Retourne le prix d'un produit toutes charges comprises
#        avec une TVA réduite
#
#FILE
#    c:\users\documents\slides de formation\python\tva.py

#Utilisation d'une fonction du package importé
print(tva.pttc_normal(100)) #120

##############################################################################
##############################################################################
# 1.3 - NUMPY ET SCIPY
##############################################################################
##############################################################################

# ------------------------- #
# Numpy
# ------------------------- #

# Manipulation des objets scipy : 
    
import numpy as np
a = np.arange(10)**3
print("Le tableau étudié est :", a, "\n")

#Index 
print("Le troisième élément de ce tableau est :", a[2], "\n")

#Slicing 
print("Les éléments entre le 3è et le 5è sont ", a[2:5])
a[:6:2] = 1000
print("Nous avons modifié les éléments 0 à 6 par pas de 2 :", a, "\n")

#Itération
print("Nous itérons sur le tableau créé :")
for i in a: print(i,"puissance 3 vaut ", i**3)

# Tableaux multi dimensions : 
    
def f(x,y) : return 10*x+y
b = np.fromfunction(f,(5,4), dtype=int)
print(b)

print(b[0:5,1])
print(b[:,1])
print(b[1:3,:])
print(b[-1])

# Quelques fonctions utiles : 
    
a = np.array([-1.7, -1.5, -0.2, 1.5, 1.7, 2.0])
print(np.floor(a))

a = np.floor(10*np.random.random((3,4)))
print(a) 

print(a.T)

np.sum([[0, 1], [0, 5]])

np.sum([[0, 1], [0, 5]], axis=0)

a = np.arange(10)
print(a)

b = np.where(a<5, 'Petit', 'Grand')
print(b)

a = np.array([1,2,1,0,5,1,9,5])
print(np.bincount(a))

a = np.array([5,3,2,-1,4])
print(np.any(a<0))

print(np.all(a>0))

# Synthèse : 
    
import time; import numpy as np
taille = 50000000

def pur_python_version():
    t1 = time.time()
    X= Y = range(taille)
    Z = [X[i] + Y[i] for i in range(len(X))]
    return time.time() - t1
    
def numpy_version():
    t1 = time.time()
    X = Y = np.arange(taille)
    Z = X + Y
    return time.time() - t1 

t1 = pur_python_version()
t2 = numpy_version()

print("Temps d'opérations est de {:d}".format(taille))
print("Temps pour la liste est de {:2.3} secondes".format(t1))
print("Temps pour numpy est de {:2.3} secondes".format(t2))
print("Numpy est {:2.0f} plus rapide".format(t1/t2))

# ------------------------- #
# Scipy
# ------------------------- #

# Quelques exemples : 
    
# Import package
import numpy as np
import scipy.stats as stat 

'''Soit d un vecteur d'observations'''
d = np.array([0.553,0.57,0.576,0.601,0.606,0.606,0.609,0.611,0.615,
              0.628,0.654,0.662,0.668,0.67,0.672,0.69,0.693,0.749])

'''Statisitiques descriptives'''
stat_d = stat.describe(d)
print(stat_d)
#DescribeResult(nobs=18, minmax=(0.55300000000000005, 0.749), 
#               mean=0.63516666666666666, 
#               variance=0.0025368529411764714, 
#               skewness=0.38763289979752136, 
#               kurtosis=-0.3587369048751916)

'''Récupérer une valeur en particulier (exemple nombre d'observations) '''
print(stat_d[0]) # --> 18

print(stat_d.nobs) #--> 18

n,mm,moy,var,skw,kt = stat.describe(d)
print(n) #--> 18

'''Médiane et quantile'''
print(np.median(d))  #--> 0.6215
print(np.percentile(d,q = 10)) #--> 0.5742
print(stat.percentileofscore(d,0.6215))  
# --> 50.0, la moitié des obs. ont une valeur inf. à 0.6215)

# Les tests statistiques : 
    
ag = stat.normaltest(d)
print(ag) #--> NormaltestResult(statistic=0.71439079391858273, 
          #                      pvalue=0.69963577767413498)

sp = stat.shapiro(d)
print(sp) #--> (0.9613385200500488, 0.627672016620636)
          # (statistique et p-value)


ad = stat.anderson(d,dist ='norm')
print(ad) #AndersonResult(statistic=0.34029632368620355, 
            #             critical_values=array([ 0.503,  0.573,  0.687,  0.802,  0.954]), 
            #               significance_level=array([ 15. ,  10. ,   5. ,   2.5,   1. ]))

# Les distributions statistiques : 
    
'''Obtenir les valeurs des quantilles et 
des fonctions de repartition'''

print(stat.norm.ppf(0.95, loc= 0, scale = 1)) # --> CR = 1.64485
# quantille d'ordre 0.95 d'une loi normale centrée réduite
print(stat.norm.cdf(1.96,loc = 0, scale = 1)) # --> 0.975

'''Générer 30 points aléatoirement issus d'une distributions normale'''
x = stat.norm.rvs(loc = 0, scale = 1,size = 30)
'''Test de normalité'''
print(stat.normaltest(x))
#NormaltestResult(statistic=2.8179964365275616, pvalue=0.2443879839834675)

'''Générer 30 point d'une loi exponentielle'''
E = stat.expon.rvs(size = 30)
'''Test de normalité'''
print(stat.normaltest(E))
#NormaltestResult(statistic=29.430225961869137, pvalue=4.0673133463526996e-07)

# Test de Student : 
    
'''Test de conformité de la moyenne : TEST DE STUDENT'''
print(stat.ttest_1samp(d,popmean=0.618)) # (1.446, 0.166)
#stat. de test et p-value, p-value < α, rejet de H0

'''Si l'on détaille les calculs'''
#moyenne
m = np.mean(d) # 0.6352
#écart-type – ddof = 1 pour effectuer le calcul : 1/(n-1)
sigma = np.std(d,ddof=1) # 0.0504
#stat. de test t
import math
t = (m - 0.618)/(sigma/math.sqrt(d.size))
print(t) # 1.446, on retrouve bien la bonne valeur de la stat de test
#p-value – c'est un test bilatéral
#t distribution de Student, cdf() : cumulative distribution function
p = 2.0 * (1.0 - stat.t.cdf(math.fabs(t),d.size-1))
print(p) # 0.166, et la bonne p-value

# Exemples : 
    
'''Statistiques à deux vecteurs '''
'''treated – valeurs pour échantillon des individus ayant suivi le traitement'''
dt = np.array([24,43,58,71,43,49,61,44,67,49,53,56,59,52,62,54,57,33,46,43,57])
'''Echantillon controle'''
dc = np.array([42,43,55,26,62,37,33,41,19,54,20,85,46,10,17,60,53,42,37,42,55,28,48])
'''t-test – comparaison de param. de localisation – hyp. de variances égales'''
print(stat.ttest_ind(dt,dc)) # (t = 2.2665, p-value = 0.0286)
'''t-test de Welch – comparaison de moyennes – hyp. de variances inégales'''
print(stat.ttest_ind(dt,dc,equal_var=False)) # (2.3109, 0.0264)
'''test de Mann-Whitney - non paramétrique - avec correction de continuité'''
print(stat.mannwhitneyu(dt,dc)) # (stat. U = 135, p-value unilatérale = 0.00634)
'''test de Bartlett – comparaison de paramètres d'échelle (variance)'''
print(stat.bartlett(dt,dc)) # (stat. = 3.8455, p-value = 0.0498)
'''test de Ansari Bradley'''
print(stat.ansari(dt,dc)) # (stat. = 266, p-value = 0.2477)
'''test de Levene'''
print(stat.levene(dt,dc)) # (stat. = 2.342, p-value = 0.1334)
'''test de Kolomogorov-Smirnov – écart entre les fonctions de répartition empiriques'''
print(stat.ks_2samp(dt,dc)) # (stat. = 0.4699, p-value = 0.0099)


#Comparaison de 2 populations

'''Les données'''
d1968 = np.array([0.42,0.5,0.52,0.45,0.43,0.55,0.45,0.34,0.45,
                  0.54,0.42,0.51,0.49,0.54,0.5,0.58,0.49,0.56,0.63])
d1972 = np.array([0.45,0.5,0.52,0.45,0.46,0.55,0.60,0.49,0.35,
                  0.55,0.52,0.53,0.57,0.53,0.59,0.64,0.5,0.57,0.64])

'''t-test related samples - paramétrique'''
print(stat.ttest_rel(d1968,d1972))# (stat.test = -2.45, p-value = 0.024)
'''test des rangs signés – non paramétrique'''
print(stat.wilcoxon(d1968,d1972)) # (stat = 16, p-value = 0.0122)


'''Données pour corrélation et régression (Irlande du Nord non incluse)'''
dalc = np.array([6.47,6.13,6.19,4.89,5.63,4.52,5.89,4.79,5.27,6.08])
dtob = np.array([4.03,3.76,3.77,3.34,3.47,2.92,3.2,2.71,3.53,4.51])
'''Différentes techniques de calcul pour la corrélation
        - Corrélation de Pearson'''
print(stat.pearsonr(dalc,dtob)) # (r = 0.7843, p-value pour test t = 0.0072)
'''     - Corrélation de Spearman - basé sur les rangs'''
print(stat.spearmanr(dalc,dtob)) # (rho = 0.8303, p-value = 0.0029)
'''     - Tau de Kendall - concordance et discordance'''
print(stat.kendalltau(dalc,dtob)) # (tau = 0.6444, p-value = 0.0095)
'''     - Régression linéaire simple'''
print(stat.linregress(dalc,dtob)) # (pente = 0.6115, const = 0.1081, r = 0.7843, 
#p-value test signif. pente = 0.0072, sigma err = 0.1710)


# Exemple test chi2 tableau de contingence :  
import pandas as pd
df = pd.read_csv(r'C:\Users\Documents\Data\data_titanic.csv',
             sep = ',')

cont_T = pd.crosstab(df['Sex'], df['Survived'])
#Survived    0    1
#Sex               
#female     81  233
#male      468  109

stat.chi2_contingency(cont_T, correction=False)
#
#(263.05057407065567,                    #test statistic
# 3.711747770113424e-59,                 #pvalue
# 1,                                     # degrés de liberté
# array([[ 193.47474747,  120.52525253], # fréquence espérée
#        [ 355.52525253,  221.47474747]]))


##############################################################################
##############################################################################
# 1.4 - PANDAS
##############################################################################
##############################################################################

import pandas as pd
import numpy as np 

# ------------------------- #
# Notions de Data Frame 
# ------------------------- #

#Nombre d'attributs et de méthodes dans Series et pas Data Frame
seriesexcl = len([x for x in dir(pd.Series) if x not in dir(pd.DataFrame) if not x.startswith('_')])

#Nombre d'attributs et de méthodes dans Data Frame et pas dans Series 
dfexcl = len([x for x in dir(pd.DataFrame) if x not in dir(pd.Series) if not x.startswith('_')])

#Nombre d'attributs et de méthodes en commun
commun = len([x for x in dir(pd.DataFrame) if x in dir(pd.Series) if not x.startswith('_')])



# ------------------------- #
# Typage des données 
# ------------------------- #

df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print(df2)
#     A          B    C  D      E    F
#0  1.0 2013-01-02  1.0  3   test  foo
#1  1.0 2013-01-02  1.0  3  train  foo
#2  1.0 2013-01-02  1.0  3   test  foo
#3  1.0 2013-01-02  1.0  3  train  foo


df2.dtypes
#A           float64
#B    datetime64[ns]
#C           float32
#D             int32
#E          category
#F            object
#dtype: object

# ------------------------- #
# Fonctions de base 
# ------------------------- #

df = pd.DataFrame({"Col1": pd.Series([1,2,3,4,5,6]),
                   "Col2" : pd.Categorical(["Oui","Non","Oui","Oui","Non","Oui"]),
                   "Col3": pd.Series([23,4,12,2,0,-10])})

'''les 2 premières lignes'''
df.head(2)
#   Col1 Col2  Col3
#0     1  Oui    23
#1     2  Non     4

'''Les 2 dernières lignes'''
df.tail(2)
#   Col1 Col2  Col3
#4     5  Non     0
#5     6  Oui   -10

'''Toutes les lignes moins les 2 dernières'''
df.head(-2)
#   Col1 Col2  Col3
#0     1  Oui    23
#1     2  Non     4
#2     3  Oui    12
#3     4  Oui     2


'''Obtenir des informations sur les variables numériques'''
df.describe()
#           Col1       Col3
#count  6.000000   6.000000
#mean   3.500000   5.166667
#std    1.870829  11.250185
#min    1.000000 -10.000000
#25%    2.250000   0.500000
#50%    3.500000   3.000000
#75%    4.750000  10.000000
#max    6.000000  23.000000

'''Transposer une table'''
df.T
#        0    1    2    3    4    5
#Col1    1    2    3    4    5    6
#Col2  Oui  Non  Oui  Oui  Non  Oui
#Col3   23    4   12    2    0  -10

'''Trier une table en fonction d'une colonne'''
df.sort_values(by= "Col3", ascending = True, inplace = True)
#   Col1 Col2  Col3
#5     6  Oui   -10
#4     5  Non     0
#3     4  Oui     2
#1     2  Non     4
#2     3  Oui    12
#0     1  Oui    23


# ------------------------- #
# Agrégations avancées
# ------------------------- #

df = pd.DataFrame({'ID_maison': [0,1,2,3,4,5], 
                   'date_vente': ['15/01/2021', '10/01/2021', '13/01/2021', '15/01/2021', '15/01/2021', '10/01/2021'], 
                   'ville': ['Paris', 'Paris', 'Lyon', 'Paris', 'Lyon', 'Paris'], 
                   'Prix_m2': [15000, 9000, 4000, 8000, 6000, 13000], 
                   'Surface' : [30, 21, 42, 15, 63, 40]})

df.groupby(['ville'])['Prix_m2'].mean() 
df.groupby(['ville','date_vente'])['Prix_m2'].agg(['mean', 'max']) 
df.groupby(['ville', 'date_vente'])[['Prix_m2', 'Surface']].agg(['mean', 'max'])

df_agg = df.groupby(['ville', 'date_vente'])[['Prix_m2', 'Surface']].agg(['mean', 'max']).reset_index()
df_agg.columns = ['_'.join(x) if len(x[1])>0 else x[0] for x in df_agg.columns]

# ------------------------- #
# Création de nouveaux indicateurs 
# ------------------------- #


df = pd.DataFrame({'Col1': pd.Series([1,2,3,4,5,6]),
                   'Col2': pd.Series([23,4,12,2,0,-10])})


'''Ajouter une colonne constante'''
df['Col4'] = "constant"

'''Ajouter une colonne'''
df['Col5'] = [7,9,6,6,19,44] # Attention le nombre d'éléments de la liste 
                             # doit être égal au nombre de lignes du dataframe                            
'''Supprimer une colonne'''
del df['Col1']
print(df)
#  Col2  Col3      Col4  Col5
#5  Oui   -10  constant     7
#4  Non     0  constant     9
#3  Oui     2  constant     6
#1  Non     4  constant     6
#2  Oui    12  constant    19
#0  Oui    23  constant    44

df = pd.DataFrame({'Col1': pd.Series([1,2,3,4,5,6]),
                   'Col2': pd.Series([23,4,12,2,0,-10])})

df.applymap(lambda x : x+3)
#   Col1  Col2
#0     4    26
#1     5     7
#2     6    15
#3     7     5
#4     8     3
#5     9    -7

df.apply(lambda x : x.mean())
#Col1    3.500000
#Col2    5.166667
#dtype: float64

df['Col1'].map(lambda x : x +3)
#0    4
#1    5
#2    6
#3    7
#4    8
#5    9
#Name: Col1, dtype: int64

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
DEPTS = pd.read_csv('https://www.insee.fr/fr/statistiques/fichier/3720946/departement2019-csv.zip', dtype = 'str')
dic_DEPTS = DEPTS.set_index('dep').to_dict()['libelle']
df = pd.DataFrame({'DEPT' :['10',np.nan,'976','2A','78','33','31']})
df['LIBELLE_DEPT'] = df.DEPT.map(dic_DEPTS)
df['LIBELLE_DEPT'] = df.applymap(dic_DEPTS.get)



df = pd.DataFrame({'Ville':['Paris','Londres','Manchester','Paris'],
                   'Statut':['Actif','Actif','Etudiant','Retraité'],
                   'Age':[45,56,19,78], 'Sexe':['H','F','F','H'],
                   'Nb_annees_travail' : [20,29,0,43]}) 

'''np.where'''
df['Travailleur'] = pd.DataFrame(np.where(df['Statut']=='Actif',1,0),
                                index = df.index)


df['Ville_statut'] = df['Ville'] + "_" + df['Statut']

df['Temps restant à travailler'] = 43 - df['Nb_annees_travail']

df['Proportion de temps passé au travail'] = df['Nb_annees_travail']/df['Age']


# ------------------------- #
# Fonctions avancées de Data Management
# ------------------------- #


df = pd.DataFrame({'ID_maison':[0,1,2,3,4,5], 'date_vente':['15/01/2021', '10/01/2021', '13/01/2021', '01/01/2021', '15/01/2021', '12/01/2021'], 'ville':['Paris','Paris','Lyon','Paris','Lyon','Paris'], 'Prix_m2':[15000, 9000, 4000, 8000, 6000, 13000]})

df['date_vente'] = pd.to_datetime(df['date_vente'], format = '%d/%m/%Y')
df.sort_values(by = ['ville','date_vente'], inplace = True)

df_var_ind = df.groupby('ville').rolling('10d', on = 'date_vente', closed = 'both').mean()['Prix_m2'].reset_index().rename(columns = {'level_1':'ID_maison'})
df_var_ind = df.groupby('ville').rolling('10d', on = 'date_vente', closed = 'left').mean()['Prix_m2'].reset_index().rename(columns = {'level_1':'ID_maison'})

df_var_ind = df.groupby('ville').rolling(2, on = None, closed = None).mean()['Prix_m2'].reset_index().rename(columns = {'level_1':'ID_maison'})
df_var_ind = df.groupby('ville').rolling(2, on = None, closed = 'left').mean()['Prix_m2'].reset_index().rename(columns = {'level_1':'ID_maison'})


##############################################################################
##############################################################################
# 1.5 - STATISTIQUES DESCRIPTIVES 
##############################################################################
##############################################################################

#Générer le dataframe 
import numpy as np; import pandas as pd 

np.random.seed(123) # reproductivité des résultats
df_f = pd.DataFrame({'SEXE':['F']*45,'AGE':np.random.randint(18,105,45),'TAILLE':np.random.randint(145,185,45)})
df_h = pd.DataFrame({'SEXE':['H']*45,'AGE':np.random.randint(18,95,45),'TAILLE':np.random.randint(165,205,45)})
df_aut = pd.DataFrame({'SEXE':[None]*10,'AGE':np.random.randint(18,105,10),'TAILLE':np.random.randint(145,205,10)})
df = pd.concat([df_f,df_h,df_aut],axis=0,ignore_index=True) # concaténation des trois dataframes

df['CAT_TAILLE'] = np.where(df['TAILLE']>=175,'GRAND','PETIT')

#Aperçu du dataframe
df.head(5) # 5 premières lignes du dataframe

# Etude du dataframe dans son ensemble
len(df) # nombre total d'observations

df.isnull().sum() # nombre de valeurs manquantes par colonne



df.describe() #présente les principales stats pour chaque champ numérique

df.AGE.mean() # identique à df['AGE'].mean()
df.AGE.min()
df.AGE.max() 
# .var() pour variance, .median(), .sum() pour la somme

df.groupby('SEXE')['TAILLE'].mean() # moyenne par SEXE pour POIDS

df.groupby('SEXE').mean() #moyenne pour toutes les var numériques 
#(sauf celles dans le GROUP BY)


df.groupby(['SEXE','CAT_TAILLE'])['TAILLE'].mean()

df.SEXE.value_counts() # tri à plat pour la variable SEXE

df.SEXE.value_counts(dropna=False) # dropna = False permet d'intégrer
# les valeurs manquantes

df.SEXE.str.len() # calcule le nombre de caractères pour 
# chaque observation pour la variable SEXE

pd.crosstab(df.SEXE,df.CAT_TAILLE) # tableau croisé 

pd.crosstab(df.SEXE.fillna('Non Renseigné'), df.CAT_TAILLE)
# .fillna('Non Renseigné') remplace les valeurs manquantes
# par la modalité 'Non Renseigné'

pd.crosstab(df.SEXE.fillna('Non Renseigné'),df.CAT_TAILLE, margins=True)
# margins = True pour intégrer les totaux

##############################################################################
##############################################################################
# 1.6 - MATPLOTLIB
##############################################################################
##############################################################################

import numpy as np
import matplotlib.pyplot as plt 
x= np.linspace(0,10,20) # génère 20 points entre 0 et 10
y = x**2

plt.title('Mon titre') # ajouter un titre
plt.xlabel('Label x') # ajouter un label à l'axe x
plt.ylabel('Label y') # ajouter un label à l'axe y
plt.plot(x,y,'blue') #tracer la courbe (en bleu)

fig, ax = plt.subplots() # génère le graphique vide 
ax.set_title('Mon titre') # ajouter un titre
ax.set_xlabel('Label x') # ajouter un label à l'axe x
ax.set_xlabel('Label y') # ajouter un label à l'axe y
ax.plot(x,y,'blue') #tracer la courbe (en bleu)

##############################################################################
##############################################################################
# 2.3 - PARTITIONNEMENT DES DONNEES
##############################################################################
##############################################################################

# ------------------------- #
# Validation croisée simple : apprentissage / test 
# ------------------------- #

import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_sas(r'C:/Users/TLENOUVEL/Formation_Python/Sources/titanic.sas7bdat',encoding='utf-8')
#df = pd.read_sas(r'C:/Users/ADUBOIS/Desktop/Formation_Python/data/titanic.sas7bdat',encoding='utf-8')

# Exemple de recodage de la variable cible
df['Survived'] = df['Survived'].map({'yes':1,'no':0}).astype('int8') 

# Variable cible
y = df['Survived']

# Covariables
X = df.loc[:,df.columns!='Survived']

# 1. Création des échantillons train et test pour X et y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42, stratify=y)

# 2. Séparation apprentissage / test en utilisant les index de lignes
train_index, test_index = train_test_split(df.index, test_size = 0.3, random_state=42, stratify=y)

# 3. Séparation apprentissage / test en utilisant les numéros de lignes
train_index, test_index = train_test_split(range(len(df)), test_size = 0.3, random_state=42, stratify=y)

# ------------------------- #
# K-Fold validation : exemple d'application
# ------------------------- #

'''Stratified K-fold'''

from sklearn.model_selection import StratifiedKFold
k=5
y =df['Survived'] #Extraction du vecteur cible au format series
X = df.copy()
del X['Survived'] # Suppression de la variable cible pour l'apprentissage

skf = StratifiedKFold(n_splits = k)

Y =pd.DataFrame(df['Survived'], index = df.index) # extraction de la variable cible au format DataFrame
for train_index, test_index in skf.split(X,y):
    X_train = X.iloc[train_index,:]
    X_test =  X.iloc[test_index,:]
    y_train = Y.iloc[train_index,:]
    y_test =  Y.iloc[test_index,:]
    
##############################################################################
##############################################################################
# 2.4 - PREPROCESSING
##############################################################################
##############################################################################

# ------------------------- #
# Gestion des variables QUANTI : Imputer les valeurs manquantes
# ------------------------- #

# Remplacement des valeurs manquantes
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

df= pd.DataFrame({'V1' : [1,2,np.nan,10,2],'V2' : [1,np.nan,3,4,5]})
imp = SimpleImputer(strategy="mean") 
imp.fit(df)
df_bis = imp.transform(df)
#array([[  1.  ,   1.  ],
#       [  2.  ,   3.25],
#       [  3.75,   3.  ],
#       [ 10.  ,   4.  ],
#       [  2.  ,   5.  ]])

imp_ter = SimpleImputer(strategy = "median")
'''Pour le mode : strategy = 'most_frequent' '''

imp_ter.fit(df)
df_ter = imp_ter.transform(df)
#array([[  1. ,   1. ],
#       [  2. ,   3.5],
#       [  2. ,   3. ],
#       [ 10. ,   4. ],
#       [  2. ,   5. ]])

# ------------------------- #
# Gestion des variables QUANTI : standardisation
# ------------------------- #

import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # charger la fonction pour centrer réduire

# Lecture de la table
path_data = 'C:/Formation Python/Datasets/'
#path_data = r'C:\Users\ADUBOIS\Desktop\Formation_Python\Sources\\'
df  = pd.read_csv(path_data + 'adult.csv', sep = ',')
y = (df['income']=='>50K').astype('int8').copy()
del df['income']

# Partitionnement
train_index, test_index = train_test_split(range(len(df)), test_size = 0.3, random_state=42, stratify=y)

# Standardisation des variables quantitatives
liste_var_cont = [var for var in df.select_dtypes(np.number)] # liste des variables numériques 

#Normalisation des variables concernées :
scaler = StandardScaler().fit(df.loc[train_index, liste_var_cont]) # préparation de la transformation à effectuer
df[liste_var_cont] = scaler.transform(df[liste_var_cont]) # application de la transformation

#Pour vérifier que les variables ont bien été normalisées :
df.loc[train_index, liste_var_cont].mean()
df.loc[train_index, liste_var_cont].std()

# ------------------------- #
# Gestion des variables numériques : Générer des variables polynomiales
# ------------------------- #

# Polynomiale features :
from sklearn.preprocessing import PolynomialFeatures
Z = np.arange(6).reshape(3, 2)
#array([[0, 1],
#       [2, 3],
#       [4, 5]])
poly = PolynomialFeatures(2) # degres par défaut = 2
poly.fit_transform(Z)
#array([[  1.,   0.,   1.,   0.,   0.,   1.],
#       [  1.,   2.,   3.,   4.,   6.,   9.],
#       [  1.,   4.,   5.,  16.,  20.,  25.]])
poly = PolynomialFeatures(interaction_only=True)
poly.fit_transform(Z)
#array([[  1.,   0.,   1.,   0.],
#       [  1.,   2.,   3.,   6.],
#       [  1.,   4.,   5.,  20.]])
poly = PolynomialFeatures(degree=3, interaction_only=False, include_bias=False)
poly.fit_transform(Z)
#array([[   0.,    1.,    0.,    0.,    1.,    0.,    0.,    0.,    1.],
#       [   2.,    3.,    4.,    6.,    9.,    8.,   12.,   18.,   27.],
#       [   4.,    5.,   16.,   20.,   25.,   64.,   80.,  100.,  125.]])


# ------------------------- #
# Encodage des variables catégorielles : label encoding
# ------------------------- #

import pandas as pd
from sklearn import preprocessing

df = pd.DataFrame({"Var_1":[1,1,2,4,7], 'Var_2' : ["Paris","Tokyo","Tokyo","Pekin","Paris"]})
Y = pd.Series(["Paris","Tokyo","Tokyo","Pekin","Paris"])


le = preprocessing.LabelEncoder()
le.fit(Y)
Y_lab = le.transform(Y)
print(Y_lab)    # [0 2 2 1 0]
list(le.inverse_transform(Y_lab)) # ['Paris', 'Tokyo', 'Tokyo', 
                                    #'Pekin', 'Paris']

Test = [0,1,1,2]
list(le.inverse_transform(Test))  # ['Paris', 'Pekin', 'Pekin', 'Tokyo']

Test2 = [0,1,1,2,3]
list(le.inverse_transform(Test2))  # ValueError: y contains unseen labels: [3]

Test3 = ["Paris","Tokyo","Madrid"]
list(le.transform(Test3))          # ValueError: y contains unseen labels: ['Madrid']

# ------------------------- #
# Encodage des variables catégorielles : one hot encoding
# ------------------------- #

import pandas as pd
from sklearn import preprocessing
df = pd.DataFrame({"Var_1":[1,1,2,4,7], 'Var_2' : ["Paris","Tokyo","Tokyo","Pekin","Paris"]})
#   Var_1  Var_2
#0      1  Paris
#1      1  Tokyo
#2      2  Tokyo
#3      4  Pekin
#4      7  Paris
le = preprocessing.LabelEncoder()
le.fit(df['Var_2'])
df['Var_2'] = le.transform(df['Var_2'])
#   Var_1  Var_2
#0      1      0
#1      1      2
#2      2      2
#3      4      1
#4      7      0
enc = preprocessing.OneHotEncoder()
enc.fit(df)  
df_bis = enc.transform(df).toarray()
#array([[ 1.,  0.,  0.,  0.,  1.,  0.,  0.],
#       [ 1.,  0.,  0.,  0.,  0.,  0.,  1.],
#       [ 0.,  1.,  0.,  0.,  0.,  0.,  1.],
#       [ 0.,  0.,  1.,  0.,  0.,  1.,  0.],
#       [ 0.,  0.,  0.,  1.,  1.,  0.,  0.]])


'''Choisir les variables catégorielles'''
from sklearn.compose import ColumnTransformer

transformer = ColumnTransformer(
    transformers=[
        ("OneHot", 
         preprocessing.OneHotEncoder(categories='auto'), # la transformation à appliquer
         ['Var_2']  # la colonne sur laquelle appliquer la transformation 
         )
    ], remainder='passthrough' # ne rien faire sur les autres colonnes
)
 
df_bis = transformer.fit_transform(df)
#array([[ 1.,  0.,  0.,  1.],
#       [ 0.,  0.,  1.,  1.],
#       [ 0.,  0.,  1.,  2.],
#       [ 0.,  1.,  0.,  4.],
#       [ 1.,  0.,  0.,  7.]])

'''En une ligne avec pandas '''
df = pd.DataFrame({"Var_1":[1,1,2,4,7], 'Var_2' : ["Paris","Tokyo","Tokyo","Pekin","Paris"]})
df = pd.get_dummies(df,columns = ['Var_2'])
#   Var_1  Var_2_Paris  Var_2_Pekin  Var_2_Tokyo
#0      1          1.0          0.0          0.0
#1      1          0.0          0.0          1.0
#2      2          0.0          0.0          1.0
#3      4          0.0          1.0          0.0
#4      7          1.0          0.0          0.0

# ------------------------- #
# Onehotencoder vs get_dummies
# ------------------------- #

import pandas as pd
train_data =pd.DataFrame(pd.Series(['good','bad','worst','good', 'good', 'bad']))
test_data = pd.DataFrame(pd.Series(['good','bad','worst','good', 'good', 'bad','excellent', 'perfect']))
# test_data contient 2 valeurs que data n'a pas

# 1. Dummisation avec get_dummies
df_train = pd.get_dummies(train_data)
df_test = pd.get_dummies(test_data)
df_test = df_test[df_train.columns] # pour ne conserver que les dummies présents dans la table d'apprentissage

# 2. Dummisation avec OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(handle_unknown="ignore", sparse=False)
encoder.fit(train_data)
encoder.transform(train_data)  
encoder.transform(test_data) #application sur la table test 

# ------------------------- #
# PCA
# ------------------------- #

import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv(r'C:/Users/ADUBOIS/Desktop/Formation_Python/Sources/diabetes.csv',sep =",")
Y = df['Outcome']
del df['Outcome']
X = df.copy()

# PCA
pca = PCA(n_components= 2)
pca.fit(X)
X_trans = pca.transform(X)
X_trans = pd.DataFrame(X_trans)
X_trans.head(3)
#           0          1  Target
#0 -75.714655 -35.950783       1
#1 -82.358268  28.908213       0
#2 -74.630643 -67.906496       1

'''Graphique classique'''
import matplotlib.pyplot as plt
X_trans['Target'] = Y
X_trans_0 = X_trans[X_trans['Target']==0]
X_trans_1 = X_trans[X_trans['Target']==1]
plt.plot(X_trans_0[0],X_trans_0[1],'bo')
plt.plot(X_trans_1[0],X_trans_1[1],'ro')

# ------------------------- #
# Etude des corrélations
# ------------------------- #

import pandas as pd
import seaborn as sns

path_data = 'C:/Formation Python/Datasets/'
df  = pd.read_csv(path_data + 'diabete.csv', sep = ',')
Y = df['Outcome']
del df['Outcome']
X = df.copy()

# Calcul de la matrice de corrélation
corr_mat = X.corr()

# Heatmap avec le package seaborn (beaucoup plus simple que matplotlib.pyplot)
sns.heatmap(corr_mat, vmin=corr_mat.values.min(), vmax=1, square=True, 
        linewidths=0.1, annot=True, annot_kws={"size":8}, cmap= 'coolwarm')


'''Estimation matrice de corrélation avec PCA'''
matrix_cov = pca.get_covariance()
matrix_corr = matrix_cov.copy()

for i in range(len(X.columns)) :
    name_i = X.columns[i]
    a = X[name_i].std()
    matrix_corr[i,:] = matrix_cov[i,:]/a
    
for i in range(len(X.columns)) :
    name_i = X.columns[i]
    a = X[name_i].std()
    print(a)
    matrix_corr[:,i] =  matrix_corr[:,i]/a 

##############################################################################
##############################################################################
# 2.5 - FONCTIONS AVANCÉES POUR LA GESTION DES VARIABLES CATÉGORIELLES
##############################################################################
##############################################################################

# ------------------------- #
# Frequency encoding
# ------------------------- #

import pandas as pd
df = pd.DataFrame({'Temperature':['Hot','Cold','Very Hot', 'Warm', 'Hot', 'Warm','Warm', 'Hot', 'Hot', 'Cold'], 'Color':['Red','Yellow','Blue','Blue','Red','Yellow','Red','Yellow','Yellow','Yellow'], 'Target':[1,1,1,0,1,0,1,0,1,1]})

fe = df.groupby('Temperature').size()/len(df)
df.loc[:, 'Freq_encode'] = df['Temperature'].map(fe) 

fe = df.Temperature.value_counts()/len(df)
df.loc[:, 'Freq_encode'] = df['Temperature'].map(fe) 

# ------------------------- #
# Leave one out encoding 
# ------------------------- #

import pandas as pd
from sklearn.model_selection import train_test_split
from category_encoders.leave_one_out import LeaveOneOutEncoder
# Lecture de la table
path_data = 'C:/Formation Python/Datasets/'
df  = pd.read_csv(path_data + 'adult.csv', sep = ',')

y = (df['income']=='>50K').astype('int8').copy()
del df['income'] # df est maintenant composée uniquement des variables explicatives

# Partitionnement des index en train / test
train_index, test_index = train_test_split(range(len(df)), test_size = 0.3, stratify = y, random_state = 0)

# Identification des variables catégorielles stockées sous forme de chaines de caractères
liste_var_str = [var for var in df.select_dtypes(object)] 

# LOO Encoding des variables de liste_var_str
Loo_enc = LeaveOneOutEncoder()
loo_varnames = ['LOO_' + v for v in liste_var_str] # nom des nouvelles variables
# Calcul des valeurs LOO et application à l'échantillon d'apprentissage
df.loc[train_index, loo_varnames] = Loo_enc.fit_transform(df.loc[train_index, liste_var_str],y[train_index]).values
# Application à l'échantillon test
df.loc[test_index, loo_varnames] = Loo_enc.transform(df.loc[test_index, liste_var_str]).values

# Frenquency Encoding
fe = df.gender.value_counts()/len(df) 
df['FE_gender'] = df['gender'].map(fe) 

# Comparaison LOO Encoding VS Frequency Encoding
df.gender.value_counts();	df.FE_gender.value_counts();	 pd.crosstab(df.loc[train_index, 'gender'], y[train_index]) 	


##############################################################################
##############################################################################
# 2.6 - REGRESSIONS LOGISTIQUES
##############################################################################
##############################################################################

# ------------------------- #
# Structure de code pour la modélisation 
# ------------------------- #

import pandas as pd
#Lecture de la table
path_data = 'C:/Formation Python/Datasets/'
df  = pd.read_csv(path_data + 'adult.csv', sep = ',')
y = (df['income']=='>50K').astype('int8').copy()
del df['income'] #df est maintenant composée que de la matrice des X

#Dummisation des variables catégorielles 
df = pd.get_dummies(df)

#Séparation apprentissage/test
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=123,solver='liblinear',max_iter=200)
clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test) # [0, 0,  ... 1, ...]
prob = clf.predict_proba(X_test)
#[[0.70325198 0.29674802]
# [0.70793944 0.29206056]
# [0.54816666 0.45183334]
# ...
# [0.80442867 0.19557133]
# [0.82394388 0.17605612]
# [0.81365684 0.18634316]]

# ------------------------- #
# Fonction du package STATSMODELS 
# ------------------------- #

import statsmodels.api as sm

#Chargement d'un jeu de données
spector_data = sm.datasets.spector.load_pandas()
spector_data.exog = sm.add_constant(spector_data.exog)

logit_mod = sm.Logit(spector_data.endog, spector_data.exog)

logit_res = logit_mod.fit()

print(logit_res.summary())


##############################################################################
##############################################################################
# 2.9 - SELECTION DE VARIABLES EXPLICATIVES
##############################################################################
##############################################################################

from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import pandas as pd 

# ------------------------- #
# Chargement des données
# ------------------------- #

df = pd.read_csv(r'C:\Users\MNOEL\SDXC\Documents\Supports Formation Python\Sources_ppt_2021\diabetes.csv',
                 sep =",")

#Ajouter le nom des colonnes absent dans le fichier d'origine

columns = ['Number of times pregnant',' Plasma glucose concentration',
           'Diastolic blood pressure','Triceps skin fold thickness',
           ' 2-Hour serum insulin (mu U/ml)','Body mass index (weight in kg/(height in m)^2)',
            'Diabetes pedigree function','Age','Target']

df.columns  = columns

Y =pd.DataFrame(df['Target'], index = df.index) # extraction de la variable cible au format DataFrame
X = df.copy()
del X['Target']
from sklearn import preprocessing

col = X.columns

X_scaled = preprocessing.scale(X)
X_scaled = pd.DataFrame(X_scaled, columns = col)

y = list(Y['Target']) # Question de format

# ------------------------- #
# Méthodes automatisées 
# ------------------------- #

lr = LogisticRegression()
selecteur = RFE(estimator=lr,
                n_features_to_select=5, step=1)
sol = selecteur.fit(X_scaled,Y['Target'])
print(sol.n_features_) # 5 --> Normal on l'a fixé précédement
print(sol.support_) # [ True  True  True False False  True  True False] 
print(sol.ranking_) # [1 1 1 4 3 1 1 2]


from sklearn.feature_selection import RFECV

selecteur_cv = RFECV(lr, step=1, cv=5, 
                     scoring='accuracy')

sol_cv = selecteur_cv.fit(X_scaled,Y['Target'])
print(sol_cv.n_features_) #4
print(sol_cv.support_) # [ True  True False False False  True  True False]
print(sol_cv.ranking_) # [1 1 2 5 4 1 1 3]
print(sol_cv.grid_scores_) # [ 0.7471  0.7588  0.7640  0.77187845  
                            #    0.77187845  0.7627451 0.77056277  0.77057126]

from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np

X_red = X.iloc[:,sol_cv.support_]
len(X_scaled.columns) #4
acc_lr= []
auc_lr = []
acc_rf = []
auc_rf = []
skf = StratifiedKFold(n_splits = 5)
target = 'Target'

def cross(clf,X_train,y_train,X_test,y_test,l_acc,l_auc, target):
    clf.fit(X_train,y_train[target])
    pred = clf.predict(X_test)
    pred_proba = clf.predict_proba(X_test)
    fpr, tpr, threshold = metrics.roc_curve(y_test, pred_proba[:,1])
    roc_auc = metrics.auc(fpr, tpr)
    l_acc.append(metrics.accuracy_score(y_test,pred))
    l_auc.append(roc_auc)

for train_index, test_index in skf.split(X_red,y):
    X_train = X_red.loc[train_index,:]
    X_test =  X_red.loc[test_index,:]
    y_train = Y.loc[train_index,:]
    y_test =  Y.loc[test_index,:]
    lr = LogisticRegression(random_state=123,solver='liblinear',max_iter=200)
    rf = RandomForestClassifier() 
    cross(lr,X_train,y_train,X_test,y_test,acc_lr,auc_lr, target)
    cross(rf,X_train,y_train,X_test,y_test,acc_rf,auc_rf, target)
    
print(np.mean(acc_lr)) # 0.771 > 0.770 (résultat précédent)
print(np.mean(acc_rf)) # 0.740 < 0.759
print(np.mean(auc_lr)) # 0.833 < 0.832
print(np.mean(auc_rf)) # 0.777 < 0.818

# ------------------------- #
# Feature importance - Exemple avec une forêt aléatoire
# ------------------------- #

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier


clf = RandomForestClassifier()
clf = clf.fit(X, Y['Target'])   
info = pd.DataFrame(index = X.columns.tolist())
info["Coeff_importance"] = clf.feature_importances_

# Ecart type (modèles à plusieurs arbres ) :
std = np.std([tree.feature_importances_ for tree in clf.estimators_],
             axis=0)
info['Ecart type'] = std
info.sort_values(by="Coeff_importance",ascending = False, inplace = True)

#                                                   Coeff_importance  Ecart type
# Plasma glucose concentration                           0.284138    0.057054
#Body mass index (weight in kg/(height in m)^2)          0.153848    0.031167
#Diabetes pedigree function                              0.135346    0.024858
#Age                                                     0.121143    0.030339
#Diastolic blood pressure                                0.087152    0.024849
#Number of times pregnant                                0.076997    0.022182
# 2-Hour serum insulin (mu U/ml)                         0.071377    0.028540
#Triceps skin fold thickness                             0.069999    0.022114

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(len(info)), info["Coeff_importance"],color="r", yerr=info['Ecart type'], align="center")
plt.show()

# ------------------------- #
# Select K-best 
# ------------------------- #

from sklearn.feature_selection import *
anova = SelectKBest(f_classif, k = 'all')
anova.fit_transform(X, Y['Target'])
score =anova.scores_
#array([  39.31428116,  212.03864104,    3.23399258,    4.12849461,
#         13.56233147,   71.67881257,   23.67113786,   45.28969585])
pval =anova.pvalues_
#array([  6.02764976e-10,   1.40914192e-42,   7.25187762e-02,
#         4.25119303e-02,   2.47006859e-04,   1.28668938e-16,
#         1.38808834e-06,   3.33255459e-11])
 

'''On souhaite selectionner 5 variables'''           
anova = SelectKBest(f_classif, k = 5)
X_trans2 = anova.fit_transform(X, Y['Target'])
score =anova.scores_  
#array([  39.31428116,  212.03864104,    3.23399258,    4.12849461,
#         13.56233147,   71.67881257,   23.67113786,   45.28969585])
mask = anova.get_support()
#array([ True,  True, False, False, False,
#  True,  True,  True], dtype=bool)

##############################################################################
##############################################################################
# 2.10 - OPTIMISATION DES HYPERPARAMETRES
##############################################################################
##############################################################################

# ------------------------- #
# Grid Search 
# ------------------------- #

import pandas as pd 
#Lecture de la table
df  = pd.read_csv(r'C:/Users/ADUBOIS/Desktop/Formation_Python/Sources/adult.csv', sep = ';')

y = df['income'].copy()
del df['income'] #df est maintenant composée que de la matrice des X

#Dummisation des variables catégorielles 
df = pd.get_dummies(df)

from sklearn.model_selection import train_test_split
#Séparation apprentissage/test
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3, random_state=123)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

# Grille de recherche
param_grid = {'bootstrap': [True],
     'max_depth': [6, 10],
     'max_features': ['auto', 'sqrt'],
     'min_samples_leaf': [3, 5],
     'min_samples_split': [4, 6],
     'n_estimators': [50, 100]
    }

from sklearn.model_selection import GridSearchCV
forest_grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy', return_train_score=True,n_jobs=-1)  

forest_grid_search.fit(X_train, y_train)
forest_grid_search.best_params_
forest_grid_search.best_score_ # 0.8572347831173769

# ------------------------- #
# Random Search 
# ------------------------- #

param_space = {"bootstrap": [True],
        "max_depth": [6, 8, 10, 12, 14],
        "max_features": ['auto', 'sqrt','log2'],
        "min_samples_leaf": [2, 3, 4],
        "min_samples_split": [2, 3, 4, 5],
        "n_estimators": [20, 50, 100, 150, 200, 300]
}

from sklearn.model_selection import RandomizedSearchCV
forest_rand_search = RandomizedSearchCV(rf, param_space, n_iter=30,
                                        scoring="accuracy", cv=3,
                                        n_jobs=-1, random_state=123)

forest_rand_search.fit(X_train, y_train)
forest_grid_search.best_params_
forest_grid_search.best_score_ # 0.8572347831173769

# ------------------------- #
# Optimisation bayésienne 
# ------------------------- #

from skopt.space import Real, Categorical, Integer

search_space = {"bootstrap": Categorical([True, False]), 
        "max_depth": Integer(6, 16), 
        "max_features": Categorical(['auto', 'sqrt','log2']), 
        "min_samples_leaf": Integer(2, 10),
        "min_samples_split": Integer(2, 10),
        "n_estimators": Integer(50, 300)
    }

from skopt import BayesSearchCV
forest_bayes_search = BayesSearchCV(rf, search_space, n_iter=30, random_state=123, 
                                    scoring="accuracy", n_jobs=-1, cv=3)

forest_bayes_search.fit(X_train, y_train)
forest_bayes_search.best_params_
forest_bayes_search.best_score_ # 0.8626751294275937

##############################################################################
##############################################################################
# 2.11 - MÉTRIQUES D'ÉVALUATION DE LA PERFORMANCE DES MODÈLES
##############################################################################
##############################################################################

# ------------------------- #
# AUC et courbe ROC
# ------------------------- #

import pandas as pd

# Création d'un dataset fictif
from sklearn.datasets import make_classification
X, Y = make_classification(n_samples=700)
# Partitionnement des index en train / test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, stratify = Y, random_state = 0)
# Régression logistique
from sklearn.linear_model import LogisticRegression
lm = LogisticRegression()
lm.fit(X_train, Y_train)     
Y_pred = lm.predict(X_test)
prob = lm.predict_proba(X_test)
print(lm.coef_,lm.intercept_) # Pour imprimer les coefficients
# Metrique AUC
from sklearn import metrics
fpr, tpr, threshold = metrics.roc_curve(Y_test, prob[:,1])
roc_auc = metrics.auc(fpr, tpr)

# Courbe ROC
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.grid(True)
plt.show()

# ------------------------- #
# Courbe de gain
# ------------------------- #

n = len(Y_test)
n1 = sum(Y_test)
n0 = n-n1
# Taille cumulée de la cible
taille = [(fpr[i]*n0+tpr[i]*n1)/n for i in range(len(fpr))] 

# titre principal et libellé des axes
plt.title('Courbe de gain')
plt.xlabel('Taille de la cible')
plt.ylabel('Rappel - Taux de vrais positifs') 
# limites en abscisse et ordonnée
plt.xlim(0,1) 
plt.ylim(0,1) 
# Courbe du ciblage aléatoire
plt.plot(taille,taille,color='grey',linestyle='dashed', label='Ciblage aléatoire')
# Courbe du modèle
plt.plot(taille,tpr, label='Ciblage Régression Logistique',)
# Courbe optimale
plt.plot([0, n1/n],[0,1],color='orange',linestyle='dashed', label='Ciblage parfait',)
# affichage de la légende et du quadrillage
plt.legend()
plt.grid(True)
plt.show()

# ------------------------- #
# Courbe de lift
# ------------------------- #

plt.title('Courbe de lift')
plt.xlabel('Taille de la cible')
plt.ylabel('Lift') 
# Calcul du lift
lift = tpr/taille
# limites en abscisse et ordonnée
plt.xlim(0,1) 
plt.ylim(0, max(lift[1:]) + 0.5) 
# Ciblage aléatoire
plt.plot([0,1], [1,1], color='grey', linestyle='dashed', label='Ciblage aléatoire')
# Ciblage du modèle
plt.plot(taille, lift, label='Ciblage Régression Logistique') 
# affichage de la légende et du quadrillage
plt.legend()
plt.grid(True)
plt.show()

# ------------------------- #
# Métriques
# ------------------------- #

'''importation de metrics - utilisé pour les mesures de performances'''
from sklearn import metrics
#matrice de confusion
#confrontation entre Y obs. sur l’éch. test et la prédiction
cm = metrics.confusion_matrix(Y_test,Y_pred)
print(cm)
#[[139  20]
# [ 31  41]]

'''taux de succès'''
acc = metrics.accuracy_score(Y_test,Y_pred)
print(acc) # 0.779 = (139 + 41)/ (139 + 20 + 31 + 41)
'''taux d'erreur'''
err = 1.0 - acc
print(err) # 0.221 
'''sensibilité (ou rappel)'''
se = metrics.recall_score(Y_test,Y_pred)
print(se) # 0.569 = 41 / (31+ 41)
'''précision'''
pr =metrics.precision_score(Y_test,Y_pred)
print(pr) # 0.672 = 41/(20 + 41)


df = pd.read_csv(r'C:\Users\MNOEL\SDXC\Documents\Supports Formation Python\Sources_ppt_2021\diabetes.csv',
                 sep =",")

#Ajouter le nom des colonnes absent dans le fichier d'origine

columns = ['Number of times pregnant',' Plasma glucose concentration',
           'Diastolic blood pressure','Triceps skin fold thickness',
           ' 2-Hour serum insulin (mu U/ml)','Body mass index (weight in kg/(height in m)^2)',
            'Diabetes pedigree function','Age','Target']

df.columns  = columns

Y =pd.DataFrame(df['Target'], index = df.index) # extraction de la variable cible au format DataFrame
X = df.copy()
del X['Target']
from sklearn import preprocessing

col = X.columns

X_scaled = preprocessing.scale(X)
X_scaled = pd.DataFrame(X_scaled, columns = col)

# ------------------------- #
# Cross validation
# ------------------------- #

# Option 1 : 
    
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
import numpy as np

nb_cross = 5
lr = LogisticRegression(random_state=123,solver='liblinear',max_iter=200)
rf = RandomForestClassifier()
lr.fit(X,Y['Target'])
rf.fit(X.values,Y['Target'])
y = list(Y['Target']) # Question de format

CV_lr = cross_validate(lr,X_scaled,y,cv=nb_cross,
                                         scoring='accuracy')

print(CV_lr['test_score'])# [0.77272727 0.74675325 0.75324675 0.81699346 0.76470588]
print(CV_lr['test_score'].mean()) # 0.7708853238265002

CV_rf = cross_validate(rf,X_scaled,y,cv=nb_cross,
                                         scoring='accuracy')

print(CV_rf['test_score']) # [0.76623377 0.72077922 0.76623377 0.83660131 0.75816993]
print(CV_rf['test_score'].mean()) # 0.7696035990153638

# Option 2 : 
    
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold

def cross(clf,X_train,y_train,X_test,y_test,l_acc,l_auc, target):
    clf.fit(X_train,y_train[target])
    pred = clf.predict(X_test)
    pred_proba = clf.predict_proba(X_test)
    fpr, tpr, threshold = metrics.roc_curve(y_test, pred_proba[:,1])
    roc_auc = metrics.auc(fpr, tpr)
    l_acc.append(metrics.accuracy_score(y_test,pred))
    l_auc.append(roc_auc)

k=5
skf = StratifiedKFold(n_splits = k)
#kf = KFold(n = k)

acc_lr= []
auc_lr = []
acc_rf = []
auc_rf = []
Y = pd.DataFrame(Y) # Question de format
target = 'Target'
for train_index, test_index in skf.split(X_scaled,y):
    X_train = X_scaled.loc[train_index,:]
    X_test =  X_scaled.loc[test_index,:]
    y_train = Y.loc[train_index,:]
    y_test =  Y.loc[test_index,:]
    lr = LogisticRegression()
    rf = RandomForestClassifier() 
    cross(lr,X_train,y_train,X_test,y_test,acc_lr,auc_lr, target)
    cross(rf,X_train,y_train,X_test,y_test,acc_rf,auc_rf, target)
    
print(np.mean(acc_lr)) #0.770
print(np.mean(acc_rf)) # 0.758
print(np.mean(auc_lr)) # 0.832
print(np.mean(auc_rf)) # 0.829
