#Class
class Dog:
    

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
        self.bestFriend = []

    #Method - Kräver '()' när den kallas på av programmet.
    def add_breed(self, breed):
        self.breed = breed

    def add_best_friend(self, bestFriend):
        """ 'bestFriend' fylls i med dog_x.name för att lägga till en hund från instanserna. """
        
        if len(self.bestFriend) < 1:
            self.bestFriend = bestFriend
        elif len(self.bestFriend) >= 1 and self.breed == "Golden Retriever":
            self.bestFriend = bestFriend
        else:
            print("Too many friends.")

    def add_favoriteToy(self, favoriteToy):
        self.favoriteToy = favoriteToy

    def set_name(self, name):
        self.name = name 
    
    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner

    


#Instance - Hämtar funktionen från 'class Employee'.
dog_1 = Dog("Charlie", 7, "Michael Levin")
dog_2 = Dog("Hilda", 2, "Siri Brattberg")
dog_3 = Dog("Beppe", 10, "Karl Hermansson")
dog_4 = Dog("Walle", 5, "Tony Irving")

dog_1.add_breed("Newfoundland")
dog_1.add_best_friend(dog_2.name)
dog_1.add_best_friend(dog_3.name)

print(dog_1.__dict__)