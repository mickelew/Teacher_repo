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
    
    def add_dog(self, name, age, owner):
        temp_dog = Dog(str(name), int(age), str(owner))
        self.namelist_dogs.append(temp_dog)

    def remove_dog(self, name):
        self.namelist_dogs.remove(name)
        
    def set_boss_name(self, name):
        self.name_manager = name

def selectionMenu(name):
    selection = 0
    while selection != 7:
                
        selection=int(input("Enter choice: "))
    
        if selection == 1:
            print("Enter name, age and owner of the dog you wish to add.")
            name = input("Name: ")
            age = input("Age: ")
            owner = input("Owner: ")
            daycare_1.add_dog(name, age, owner)
            mainMenu(name)
    
        elif selection == 2:
            input_remove = input("Enter name of dog you wish to remove: ")
            daycare_1.remove_dog(input_remove)
            mainMenu(name)
        
        elif selection == 3:
            input_change = input("Enter dog's name you wish to change: ")
            daycare_1.set_name(input_change)
            mainMenu(name)
        
        elif selection == 4:
            input_owner = input("Enter name of owner: ")
            daycare_1.remove_dog(input_owner)
            mainMenu(name)
        
        elif selection == 5:
            for dog in daycare_1.namelist_dogs:
                print(dog.name)
            mainMenu(name)
       
        elif selection == 6:
            input_manager = input("Enter manager's name: ")
            daycare_1.name_manager(input_manager)
            mainMenu(name)
       
        elif selection == 7:
            exit
        
        else:
            print("\n- Invalid choice. Enter 1-7 -")
            mainMenu(name)
        break

def mainMenu(name):
    print(f"\nWelcome to {name} daycare.\nWhat would you like to do?\n")
    print("1. Add a dog to the daycare.")
    print("2. Remove dog from the daycare.")
    print("3. Change a dog's name.")
    print("4. Change the owner of a dog.")
    print("5. Show all dogs currently at the daycare.")
    print("6. Change manager.")
    print("7. Exit")
    selectionMenu(name)



#Instance - Hämtar funktionen från 'class Dog/Dog_daycare'.
daycare_1 = Dog_daycare("Vacker Tass", "Geraldo Milan")

dog_1 = Dog("Charlie", 7, "Michael Levin")
dog_2 = Dog("Hilda", 2, "Siri Brattberg")
dog_3 = Dog("Beppe", 10, "Karl Hermansson")
dog_4 = Dog("Walle", 5, "Tony Irving")

#daycare_1.add_dog(dog_1.name)
#daycare_1.add_dog(dog_2.name)
#daycare_1.add_dog(dog_3.name)
#daycare_1.add_dog(dog_4.name)

print(mainMenu(daycare_1.name_daycare))