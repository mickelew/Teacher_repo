#Class
class Dog:
    
    multiple_friends = "Golden Retriever"

    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
        self.bestFriend = []

    #Method - Kräver '()' när den kallas på av programmet.
    def add_breed(self, breed):
        self.breed = breed

    def add_best_friend(self, name):
        """ 'name' fylls i med dog_x.name för att lägga till en hund från instanserna. """
        
        if len(self.bestFriend) < 1:
            self.bestFriend.append(name)
        
        elif len(self.bestFriend) >= 1 and self.breed.casefold() == self.multiple_friends.casefold():
            self.bestFriend.append(name)
        
        else:
            print(f"Your dog already has a best friend, {self.bestFriend[0]}.")

    def add_favoriteToy(self, favoriteToy):
        self.favoriteToy = favoriteToy

    def set_name(self, name):
        self.name = name 
    
    def set_age(self, age):
        self.age = age

    def set_owner(self, owner):
        self.owner = owner

    
class Dog_daycare:
    
    def __init__(self, name_daycare, name_manager):
        self.name_daycare = name_daycare
        self.name_manager = name_manager
        self.namelist_dogs = []
    
    def add_dog(self, name):
        self.namelist_dogs.append(name)

    def remove_dog(self, name):
        self.namelist_dogs.remove(name)
        
    def set_boss_name(self, name):
        self.name_manager = name
    


#Instance - Hämtar funktionen från 'class Dog/Dog_daycare'.
daycare_1 = Dog_daycare("Vacker Tass", "Geraldo Milan")

dog_1 = Dog("Charlie", 7, "Michael Levin")
dog_2 = Dog("Hilda", 2, "Siri Brattberg")
dog_3 = Dog("Beppe", 10, "Karl Hermansson")
dog_4 = Dog("Walle", 5, "Tony Irving")

dog_1.add_breed("golden retriever")
dog_1.add_favoriteToy("Big balls")
dog_1.add_best_friend(dog_2.name)
dog_1.add_best_friend(dog_3.name)
dog_1.add_best_friend(dog_4.name)

dog_2.add_breed("Newfoundland")
dog_2.add_favoriteToy("Small balls")
dog_2.add_best_friend(dog_3.name)

daycare_1.add_dog(dog_1.__dict__)
daycare_1.add_dog(dog_2.__dict__)
daycare_1.add_dog(dog_3.__dict__)

print(daycare_1.__dict__)

print(dog_1.bestFriend)
print(dog_2.bestFriend)