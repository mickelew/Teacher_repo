#Imports
from datetime import date
import os.path



#Class and methods for creation and maintenance of library.
class Library:
    """ Låter användaren skapa sitt biblioteket med namn samt stad.
        Sparar även alla cd-skivor, böcker och filmer användaren registrerar. """
            
    def __init__(self, name, city):
        
        self.name = name
        self.city = city
        self.cdRegister = []
        self.bookRegister = []
        self.movieRegister = []
        

    #Methods
    def add_cd(self, title, author, purchasePrice, purchaseYear, numberOfTracks):
        
        temp_cd = CD(str(title), str(author), int(purchasePrice), int(purchaseYear), int(numberOfTracks))
        self.cdRegister.append(temp_cd)
    
    def add_book(self, title, author, purchasePrice, purchaseYear, numberOfPages):
        
        temp_book = Book(str(title), str(author), int(purchasePrice), int(purchaseYear), int(numberOfPages))
        self.bookRegister.append(temp_book)     

    def add_movie(self, title, author, purchasePrice, purchaseYear, lengthMinutes, condition):

        temp_movie = Movie(str(title), str(author), int(purchasePrice), int(purchaseYear), int(lengthMinutes), int(condition))
        self.movieRegister.append(temp_movie)
    

#Superclass
class mediaAttributes:
    """ Används av mediatyp-klasserna för inhämtning av gemensamma attribut. """

    def __init__(self, title, author, purchasePrice, purchaseYear):
        self.title = title
        self.author = author
        self.purchasePrice = purchasePrice
        self.purchaseYear = purchaseYear


#Subclasses
class CD(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt numberOfTracks. 
        Används när en ny CD ska läggas till i registret. """
    
    def __init__(self, title, author, purchasePrice, purchaseYear, numberOfTracks):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.numberOfTracks = numberOfTracks
        self.value = valueCD(title, author, purchasePrice)

class Book(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt numberOfPages. 
        Används när en ny bok ska läggas till i registret. """

    def __init__(self, title, author, purchasePrice, purchaseYear, numberOfPages):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.numberOfPages = numberOfPages
        self.value = valueBook(purchasePrice, purchaseYear)

class Movie(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt lengthMinutes och condition. 
        Används när en ny film ska lägas till i registret. 
        Condition anges i ett värde mellan 1-10 där 1 = mycket sliten och 10 = mycket gott skick. """

    def __init__(self, title, author, purchasePrice, purchaseYear, lengthMinutes, condition):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.lengthMinutes = lengthMinutes
        self.condition = condition
        self.value = valueMovie(purchasePrice, purchaseYear, condition)


#Functions for determining value of object.
def valueBook(purchasePrice, purchaseYear):
    """ Gör en beräkning av värdet utifrån bokens ålder och inköpspris. """

    currentYear = date.today().year
    age = currentYear-purchaseYear
    
    if age <= 50:
        value = purchasePrice*0.9**age
    elif age > 50:
        value = purchasePrice*1.08**(age-50)
    return value

def valueCD(title, author, purchasePrice):
    """ Letar efter dubbletter i cd-registret och gör en beräkning av värdet
        utifrån hur många kopior av samma cd som redan finns lagrat. """

    duplicateCD = 1
    for cd in temp_library.cdRegister:
        if cd.title.casefold() == title.casefold() and cd.author.casefold() == author.casefold():
            duplicateCD += 1
    
    value = purchasePrice // duplicateCD

    for cd in temp_library.cdRegister:
        cd.value = value
    
    return value

def valueMovie(purchasePrice, purchaseYear, condition):
    """ Gör en beräkning av värdet utifrån filmens inköpspris, ålder 
        och vilket skick den var i vid inlämnandet. """
        
    currentYear = date.today().year
    age = currentYear-purchaseYear

    value = purchasePrice*0.9**age*(condition/10)
    return value


#Functions for showing all content for each media type
def storedBooks():
    for book in temp_library.bookRegister:
        print((f"Title: {book.title}, "
                f"Author: {book.author}, "
                f"Purchase price: {book.purchasePrice}:-, "
                f"Purchase year: {book.purchaseYear}, "
                f"Number of pages: {book.numberOfPages}, "
                f"Current value: {book.value:.2f}:-"))
    print()

def storedCDs():  
    for cd in temp_library.cdRegister:
        print((f"Title: {cd.title}, "
                f"Author: {cd.author}, "
                f"Purchase price: {cd.purchasePrice}:-, "
                f"Purchase year: {cd.purchaseYear}, "
                f"Number of tracks: {cd.numberOfTracks}, "
                f"Current value: {cd.value:.2f}:-"))
    print()

def storedMovies():
    for movie in temp_library.movieRegister:
        print(f"Title: {movie.title}, "
                f"Director: {movie.author}, "
                f"Purchase price: {movie.purchasePrice}:-, "
                f"Purchase year: {movie.purchaseYear}, "
                f"Length in minutes: {movie.lengthMinutes}, "
                f"Condition: {movie.condition}, "
                f"Current value: {movie.value:.2f}:-")
    print()

def storedMedia():
    
    print("Books: \n")
    storedBooks()

    print("CD's: \n")
    storedCDs()

    print("Movies: \n")
    storedMovies()


#Functions for the menu
def selectionMenu(name, city):
   
    selection = 0

    while selection != 8:

        selection = int(input("\nEnter choice: "))
        if selection == 1:
            print("Enter the title, author, purchase price, year of purchase and number of pages.")
            title = str(input("Title: "))
            author = str(input("Author: "))
            purchasePrice = int(input("Purchase price: "))
            purchaseYear =  int(input("Year of purchase: "))
            numberOfPages = int(input("Number of pages: "))

            temp_library.add_book(title, author, purchasePrice, purchaseYear, numberOfPages)
            print(f"\n{title} has been added to the registry.")
        
        elif selection == 2:
            print("Enter the title, artist, purchase price, year of purchase and number of tracks.")
            title = str(input("Title: "))
            author = str(input("Artist: "))
            purchasePrice = int(input("Purchase price: "))
            purchaseYear =  int(input("Year of purchase: "))
            numberOfTracks = int(input("Number of tracks: "))

            temp_library.add_cd(title, author, purchasePrice, purchaseYear, numberOfTracks)
            print(f"\n{title} has been added to the registry.")

        elif selection == 3:
            print("Enter the title, director, purchase price, year of purchase, length in minutes and condition.")
            title = str(input("Title: "))
            author = str(input("Director: "))
            purchasePrice = int(input("Purchase price: "))
            purchaseYear =  int(input("Year of purchase: "))
            lengthMinutes = int(input("Length in minutes: "))
            condition = int(input("Condition 1-10 (1 is bad, 10 is mint): "))

            temp_library.add_movie(title, author, purchasePrice, purchaseYear, lengthMinutes, condition)
            print(f"\n{title} has been added to the registry.")                        
            
        elif selection == 4:
            print("These are the books currently in the registry:\n")
            storedBooks()
        
        elif selection == 5:
            print("These are the CD's currently in the registry:\n")
            storedCDs()

        elif selection == 6:
            print("These are the movies currently in the registry:\n")
            storedMovies()

        elif selection == 7:
            print("This is everything currently in the registry:\n")
            storedMedia()
        
        elif selection == 8:
            
            with open("my_cd_library.txt", "w") as My_File:
                for cd in temp_library.cdRegister:
                    My_File.write(f"{cd.title},{cd.author},{cd.purchasePrice},{cd.purchaseYear},{cd.numberOfTracks}\n") 

            with open("my_book_library.txt", "w") as My_File:
                for book in temp_library.bookRegister:
                    My_File.write(f"{book.title},{book.author},{book.purchasePrice},{book.purchaseYear},{book.numberOfPages}\n")

            with open("my_movie_library.txt", "w") as My_File:
                for movie in temp_library.movieRegister:
                    My_File.write(f"{movie.title},{movie.author},{movie.purchasePrice},{movie.purchaseYear},{movie.lengthMinutes},{movie.condition}\n")
            
            print("\nCD's, books and movies have been successfully saved.\n")

            exit()

        else:
            print("Invalid choice. Enter 1-8.")
        
        mainMenu(name, city)


def mainMenu(name, city):
    
    print(f"\nWelcome to {name} in {city}.\nWhat would you like to do?\n")
    print("1. Register a book.")
    print("2. Register a CD.")
    print("3. Register a movie.")
    print("4. Show all books currently in the registry.")
    print("5. Show all CD's currently in the registry.")
    print("6. Show all movies currently in the registry.")
    print("7. Show everything currently in the registry.")
    print("8. Save and Exit.\n")
    selectionMenu(name, city)
    

#Functions for import of file.
def importCD():

    if os.path.isfile("my_cd_library.txt"):
        print("\nCD-register found.\nWould you like to import the data?\n\n1. Yes\n2. No\n")
        
        importAnswer = int(input("Choose 1 or 2: "))
        
        if importAnswer == 1:
            with open("my_cd_library.txt", "r") as My_File:
                for line in My_File:
                    title, author, purchasePrice, purchaseYear, numberOfTracks = line.split(",")
                    temp_library.add_cd(title, author, purchasePrice, purchaseYear, numberOfTracks)
        
        elif importAnswer == 2:
            print("\nStarting with a fresh register.")

        else:
            print("\nInvalid choice. Enter 1 or 2.")
            importCD()        
    
    else:
        print("No such file.")

def importBook():

    if os.path.isfile("my_book_library.txt"):
        print("\nBook-register found.\nWould you like to import the data?\n\n1. Yes\n2. No\n")
        
        importAnswer = int(input("Choose 1 or 2: "))
        
        if importAnswer == 1:
            with open("my_book_library.txt", "r") as My_File:
                for line in My_File:
                    title, author, purchasePrice, purchaseYear, numberOfPages = line.split(",")
                    temp_library.add_book(title, author, purchasePrice, purchaseYear, numberOfPages)
        
        elif importAnswer == 2:
            print("\nStarting with a fresh register.")
        
        else:
            print("\nInvalid choice. Enter 1 or 2.")
            importBook()

    else:
        print("No such file.")

def importMovie():

    if os.path.isfile("my_movie_library.txt"):
        print("\nMovie-register found.\nWould you like to import the data?\n\n1. Yes\n2. No\n")
        
        importAnswer = int(input("Choose 1 or 2: "))
        
        if importAnswer == 1:
            with open("my_movie_library.txt", "r") as My_File:
                for line in My_File:
                    title, author, purchasePrice, purchaseYear, lengthMinutes, condition = line.split(",")
                    temp_library.add_movie(title, author, purchasePrice, purchaseYear, lengthMinutes, condition)

        elif importAnswer == 2:
            print("\nStarting with a fresh register.")
        
        else:
            print("\nInvalid choice. Enter 1 or 2.")
            importMovie()

    else:
        print("No such file.")



#Initializing program
print("Enter your library's name and city:\n")
name = input(str("Name: "))
city = input(str("City: "))
temp_library = Library(str(name), str(city))


importCD()
importBook()
importMovie()
mainMenu(temp_library.name, temp_library.city)
