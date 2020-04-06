#Class
class Dog:
    
    multiple_friends = "Golden Retriever"

    def __init__(self, name, age, owner, breed):
        self.name = name
        self.age = age
        self.owner = owner
        self.breed = breed
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

    
class Dog_daycare(Dog):
    
    def __init__(self, name_daycare, name_manager):
        self.name_daycare = name_daycare
        self.name_manager = name_manager
        self.namelist_dogs = []
    
    def add_dog(self, name, age, owner, breed):
        temp_dog = Dog(str(name), int(age), str(owner), str(breed))
        self.namelist_dogs.append(temp_dog)

    def remove_dog(self, name):
        """ Går igenom listan 'namelist_dogs' och matchar input från användaren mot objekt i listan,
            för att returnera dess placering och sedan radera. """

        for i, dog in enumerate(daycare_1.namelist_dogs):
            if dog.name == name:
                del daycare_1.namelist_dogs[i]
                break
                
    def set_boss_name(self, name):
        self.name_manager = name

def loop_throughList():
    for dog in daycare_1.namelist_dogs:
        print(dog.name)
    print()

def loop_throughEverything():
    for dog in daycare_1.namelist_dogs:
        print(dog.__dict__)
    print()

def loop_throughOwners():
    for dog in daycare_1.namelist_dogs:
        print(dog.owner)
    print()

def selectionMenu(name):
    
    daycare_name = name
    selection = 0
        
    while selection != 9:
                
        selection=int(input("\nEnter choice: "))
    
        if selection == 1:
            print("Enter name, age, owner and breed of the dog you wish to add.")
            name = input("Name: ")
            age = input("Age: ")
            owner = input("Owner: ")
            breed = input("Breed: ")
            
            daycare_1.add_dog(name, age, owner, breed)
            mainMenu(daycare_name)
    
        elif selection == 2:
            print("\nThese are the dogs currently in the daycare: ")
            loop_throughList()
            
            name = str(input("Enter name of dog you wish to remove: "))
            daycare_1.remove_dog(name)
            mainMenu(daycare_name)
        
        elif selection == 3:
            print("These are the dogs currently in the daycare: ")
            loop_throughList()
            
            name = input("Enter dog's name you wish to change: ")
            newName = input("Enter new name of said dog: ")
            
            for i, dog in enumerate(daycare_1.namelist_dogs):
                if dog.name == name:
                    dog.set_name(newName)
                    break
            
            mainMenu(daycare_name)
        
        elif selection == 4:
            loop_throughOwners()

            owner = input("Enter name of owner you wish to change: ")
            newOwner = input("Enter name of new owner: ")
            
            for i, dog in enumerate(daycare_1.namelist_dogs):
                if dog.owner == owner:
                    dog.set_owner(newOwner)
                    break
                        
            mainMenu(daycare_name)
        
        elif selection == 5:
            loop_throughOwners()
            mainMenu(daycare_name)
        
        elif selection == 6:
            loop_throughList()
            mainMenu(daycare_name)
       
        elif selection == 7:
            print("This is everything you need to know about the dogs at this daycare: \n")
            loop_throughEverything()
            mainMenu(daycare_name)

        elif selection == 8:
            print(f"The current manager is: {daycare_1.name_manager}")
            name = input("Enter the new manager's name: ")
            
            daycare_1.set_boss_name(name)
            print(f"\nThe new manager is {daycare_1.name_manager}")
            
            mainMenu(daycare_name)
       
        elif selection == 9:
            exit
        
        else:
            print("\n- Invalid choice. Enter 1-9 -")
            mainMenu(daycare_name)
        break

def mainMenu(name):
    print(f"\nWelcome to {name} daycare.\nWhat would you like to do?\n")
    print("1. Add a dog to the daycare.")
    print("2. Remove dog from the daycare.")
    print("3. Change a dog's name.")
    print("4. Change the owner of a dog.")
    print("5. Show all owners to dogs currently at the daycare.")
    print("6. Show all dogs currently at the daycare.")
    print("7. Show everything about the dogs at the daycare.")
    print("8. Change manager.")
    print("9. Exit")
    selectionMenu(name)
        


#Instance - Hämtar funktionen från 'class Dog/Dog_daycare'.
daycare_1 = Dog_daycare("Vacker Tass", "Geraldo Milan")

mainMenu(daycare_1.name_daycare)