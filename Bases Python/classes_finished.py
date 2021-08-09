#
# Fichier d'exemple pour les classes for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")

    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")


#Class avec COnstructeur
class Velo:
    roues = 2

    def __init__(self, marque, prix, poids):
        self.marque = marque
        self.prix = prix
        self.poids = poids

    def rouler(self):
        print("Wouh, ça roule mieux avec un vélo {} !".format(self.marque))



def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()


if __name__ == "__main__":
    main()
