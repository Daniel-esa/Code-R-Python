
class Myclass_old :
    number = 5 # attribut
    string ="Hello!" # attribut

new_object = Myclass_old() # objet/instance
Myclass_old.number = 27 # le fait de changer l'élément ici entraine une synchronisation de tous les objets
new_object.number = 27 # si je ne faisais pas le truc au dessus, modifier l'un entraine pas la modification de l'autre
# print(new_object.number)
# print(new_object.string)
second_new_object = Myclass_old()
# print(new_object.number == second_new_object.number)


class Myclass :
    number = 5 # attribut
    string ="Hello!" # attribut

    def __init__(self, location):
        self.location_x = location[0]# instance ou propriété d'objets ou attribut ou variable
        self.location_y = location[1] # le fait d'avoitr créer ces instances fait que les objets qui seront créés seront uniques
    
    @classmethod # décorateur. Classe méthode a pour particularité d'agir sur toute la classe et pas d'être lié à une instance/objets spécifiques.
    def increment_number (cls) : 
        cls.number +=1
        return cls.number # ==> j'ai pas encore assez de recule mais au final si j'avais faire return Myclass.number=+1 ça aurait été pareil
    
    # une autre utilisation incroyable du décorateur est qu'on a pas besoin d'avoir défini l'objet ppour qu'il puisse être utilise dans la classe
    # Can be called without first making an instance of the class.
    @classmethod
    def change_string(cls, new_string):
        #Class attributes are referred to with cls.
        cls.string = new_string
        return cls.string
    
    def change_location(self, amount) :
        self.location_x += amount
        self.location_y +=amount
        return self.location_x, self.location_y
    
    def pending_functionality(self):
        pass

new_object_one = Myclass((1, 2))
new_object_two = Myclass((-8, -9))
print(new_object_one.location_x, new_object_two.location_x)

print(new_object_one.change_location(4))


# exemple d'utilisation du décorateur classmethod. Pour rappel agit sur toute la classe partagés par toutes les instances
print(Myclass.increment_number())
print(Myclass.increment_number())
print(Myclass.increment_number())
print(Myclass.change_string("Hello World"))

