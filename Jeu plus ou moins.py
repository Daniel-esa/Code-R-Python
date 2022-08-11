###Jeu

from random import randrange
from random import randint

def Jeu_PLus_moins(nombreMystere=randrange(1, 10),nombrePropose=0,Liste=list()): 

    print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")
 
    Nom=str(input("\nComment tu t'appelles: \n"))
    print(f'\nBienvenue dans le jeu du Plus ou moins {Nom}')
    print("\nDevine le mot mystère")
    i=0
    
    while nombrePropose != nombreMystere:
        x=randint(0,len(Liste))
        y=randint(0,1)

        nombrePropose = int(input("\nDevinez un nombre ?"))
      
        if nombrePropose < nombreMystere:
            print("C'est Plus !\n")#si nombre trop petit
            i+=1
            
            if y==0:
                print (f"\ntu t'es trompé {i} fois. Tu es vraiment éclaté au sol ",Liste[x])
               
                
            #Sinon si le nombre est trop grand...
        elif nombrePropose > nombreMystere:
            print("C'est Moins !\n")#si nombre trop grand
            i+=1
            if y==0 :
                print (f"\ntu t'es trompé {i} fois. tu es vraiment éclaté au sol ",Liste[x])
            
        else:
            print(f"\nFélicitations {Nom}, t'es le best. Tu l'as fait en",i," coups !!!\n")#Bien joué

#ou print(names+",Voici la regle")
Jeu_PLus_moins(Liste=["Hello","Bonjour","Hola","Salut","NI Hao","Guten tag"])
