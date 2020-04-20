#Importer
from datetime import date
import os.path
from operator import attrgetter


#Klasser och metoder för att skapa och underhålla biblioteket.
class Library:
    """ Låter användaren skapa sitt biblioteket med namn samt stad.
        Sparar även alla cd-skivor, böcker och filmer användaren registrerar. """
            
    def __init__(self, name, city):
        
        self.name = name
        self.city = city
        self.cdRegister = []
        self.bookRegister = []
        self.movieRegister = []
        

    #Metoder
    def add_cd(self, title, author, purchasePrice, purchaseYear, numberOfTracks):
        
        temp_cd = CD(str(title), str(author), int(purchasePrice), int(purchaseYear), int(numberOfTracks))
        self.cdRegister.append(temp_cd)
    
    def add_book(self, title, author, purchasePrice, purchaseYear, numberOfPages):
        
        temp_book = Book(str(title), str(author), int(purchasePrice), int(purchaseYear), int(numberOfPages))
        self.bookRegister.append(temp_book)     

    def add_movie(self, title, author, purchasePrice, purchaseYear, lengthMinutes, condition):

        temp_movie = Movie(str(title), str(author), int(purchasePrice), int(purchaseYear), int(lengthMinutes), int(condition))
        self.movieRegister.append(temp_movie)
    

#Superklass
class mediaAttributes:
    """ Används av mediatyp-klasserna för inhämtning av gemensamma attribut. """

    def __init__(self, title, author, purchasePrice, purchaseYear):
        self.title = title
        self.author = author
        self.purchasePrice = purchasePrice
        self.purchaseYear = purchaseYear


#Subklasser
class CD(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt numberOfTracks. 
        Används när en ny CD ska läggas till i registret. """
    
    def __init__(self, title, author, purchasePrice, purchaseYear, numberOfTracks):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.numberOfTracks = numberOfTracks
        self.copies = copiesCD(title, author)
        self.value = purchasePrice // self.copies

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


#Funktioner för att fastställa värdet av ett objekt.
def valueBook(purchasePrice, purchaseYear):
    """ Gör en beräkning av värdet utifrån bokens ålder och inköpspris. """

    currentYear = date.today().year
    age = currentYear-purchaseYear
    
    if age <= 50:
        value = purchasePrice*0.9**age
    elif age > 50:
        value = purchasePrice*1.08**(age-50)
    return value

def copiesCD(title, author):
    """ Letar efter dubbletter i cd-registret och returnerar
        hur många kopior av samma cd som redan finns lagrat. """

    duplicateCD = 1
    for cd in temp_library.cdRegister:
        if cd.title.casefold() == title.casefold() and cd.author.casefold() == author.casefold():
            duplicateCD += 1

    return duplicateCD

def valueMovie(purchasePrice, purchaseYear, condition):
    """ Gör en beräkning av värdet utifrån filmens inköpspris, ålder 
        och vilket skick den var i vid inlämnandet. """
        
    currentYear = date.today().year
    age = currentYear-purchaseYear

    value = purchasePrice*0.9**age*(condition/10)
    return value


#Funktioner för att visa innehållet av respektive medietyp.
def storedBooks():
    """ Visar de specificerade värdena för böckerna i bookRegister. """
    
    #Val av sortering.
    print("\nWould you like to sort books by Title or Current Value?\n\n1. Title\n2. Current Value")
    
    selection = int(input("\nEnter choice: "))
    if selection == 1:
        
        print("\nThese are the books currently in the registry:\n")
        
        sortbyTitle = sorted(temp_library.bookRegister, key=attrgetter('title'))
        for sorted_book in sortbyTitle:
            print((f"| Title: {sorted_book.title} | "
                    f"Author: {sorted_book.author} | "
                    f"Purchase price: {sorted_book.purchasePrice}:- | "
                    f"Purchase year: {sorted_book.purchaseYear} | "
                    f"Number of pages: {sorted_book.numberOfPages} | "
                    f"Current value: {sorted_book.value:.2f}:- |"))
    
    elif selection == 2:        
        print("\nThese are the books currently in the registry:\n")
        
        sortbyValue = sorted(temp_library.bookRegister, key = attrgetter('value'), reverse=True)
        for sorted_book in sortbyValue:
            print((f"| Title: {sorted_book.title} | "
                    f"Author: {sorted_book.author} | "
                    f"Purchase price: {sorted_book.purchasePrice}:- | "
                    f"Purchase year: {sorted_book.purchaseYear} | "
                    f"Number of pages: {sorted_book.numberOfPages} | "
                    f"Current value: {sorted_book.value:.2f}:- |"))
    
    else:
        print("Invalid choice. Enter 1 or 2.")
        storedBooks()

    print()

def storedCDs():  
    """ Visar de specificerade värdena för cd's i cdRegister.
        Gör också ett test mot antal kopior i registret, som uppdateras om ny dubblett hittas
        samt räknar ut värdet utifrån inköpspris och antal kopior."""

    #Kontroll av kopior samt uträkning.    
    for cd in temp_library.cdRegister:
        cd.copies = copiesCD(cd.title, cd.author)-1        
    
    for cd in temp_library.cdRegister:
        cd.value = cd.purchasePrice // cd.copies
    
    #Val av sortering.            
    print("\nWould you like to sort cd's by Title or Current Value?\n\n1. Title\n2. Current Value")
    
    selection = int(input("\nEnter choice: "))
    if selection == 1:
        print("\nThese are the cd's currently in the registry:\n")
        
        sortbyTitle = sorted(temp_library.cdRegister, key=attrgetter('title'))
        for sorted_cd in sortbyTitle:
            print((f"| Title: {sorted_cd.title} | "
                    f"Author: {sorted_cd.author} | "
                    f"Purchase price: {sorted_cd.purchasePrice}:- | "
                    f"Purchase year: {sorted_cd.purchaseYear} | "
                    f"Number of tracks: {sorted_cd.numberOfTracks} | "
                    f"Current value: {sorted_cd.value:.2f}:- |"))
    
    elif selection == 2:
        print("\nThese are the cd's currently in the registry:\n")
        
        sortbyValue = sorted(temp_library.cdRegister, key = attrgetter('value'), reverse=True)
        for sorted_cd in sortbyValue:
            print((f"| Title: {sorted_cd.title} | "
                    f"Author: {sorted_cd.author} | "
                    f"Purchase price: {sorted_cd.purchasePrice}:- | "
                    f"Purchase year: {sorted_cd.purchaseYear} | "
                    f"Number of tracks: {sorted_cd.numberOfTracks} | "
                    f"Current value: {sorted_cd.value:.2f}:- |"))
    
    else:
        print("Invalid choice. Enter 1 or 2.")
        storedCDs()
    
    print()

def storedMovies():
    """ Visar de specificerade värdena för filmerna i movieRegister. """

    #Val av sortering.
    print("\nWould you like to sort movies by Title or Current Value?\n\n1. Title\n2. Current Value")
    
    selection = int(input("\nEnter choice: "))
    if selection == 1:
        
        print("\nThese are the movies currently in the registry:\n")
        
        sortbyTitle = sorted(temp_library.movieRegister, key=attrgetter('title'))
        for sorted_movie in sortbyTitle:
            print((f"| Title: {sorted_movie.title} | "
                    f"Director: {sorted_movie.author} | "
                    f"Purchase price: {sorted_movie.purchasePrice}:- | "
                    f"Purchase year: {sorted_movie.purchaseYear} | "
                    f"Length in minutes: {sorted_movie.lengthMinutes} | "
                    f"Condition: {sorted_movie.condition} | "
                    f"Current value: {sorted_movie.value:.2f}:- |"))
    
    elif selection == 2:
        print("\nThese are the movies currently in the registry:\n")
        
        sortbyValue = sorted(temp_library.movieRegister, key = attrgetter('value'), reverse=True)
        for sorted_movie in sortbyValue:
            print((f"| Title: {sorted_movie.title} | "
                    f"Director: {sorted_movie.author} | "
                    f"Purchase price: {sorted_movie.purchasePrice}:- | "
                    f"Purchase year: {sorted_movie.purchaseYear} | "
                    f"Length in minutes: {sorted_movie.lengthMinutes} | "
                    f"Condition: {sorted_movie.condition} | "
                    f"Current value: {sorted_movie.value:.2f}:- |"))
    
    else:
        print("Invalid choice. Enter 1 or 2.")
        storedMovies()
    
    print()

def storedMedia():
    
    storedBooks()

    storedCDs()

    storedMovies()


#Menyfunktioner
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
            storedBooks()
        
        elif selection == 5:
            print("These are the CD's currently in the registry:\n")
            storedCDs()

        elif selection == 6:
            print("These are the movies currently in the registry:\n")
            storedMovies()

        elif selection == 7:
            storedMedia()
        
        elif selection == 8:
            
            with open("my_cd_library.txt", "w") as My_File:
                for cd in temp_library.cdRegister:
                    My_File.write(f"{cd.title},"
                                    f"{cd.author},"
                                    f"{cd.purchasePrice},"
                                    f"{cd.purchaseYear},"
                                    f"{cd.numberOfTracks}\n") 

            with open("my_book_library.txt", "w") as My_File:
                for book in temp_library.bookRegister:
                    My_File.write(f"{book.title},"
                                    f"{book.author},"
                                    f"{book.purchasePrice},"
                                    f"{book.purchaseYear},"
                                    f"{book.numberOfPages}\n")

            with open("my_movie_library.txt", "w") as My_File:
                for movie in temp_library.movieRegister:
                    My_File.write(f"{movie.title},"
                                    f"{movie.author},"
                                    f"{movie.purchasePrice},"
                                    f"{movie.purchaseYear},"
                                    f"{movie.lengthMinutes},"
                                    f"{movie.condition}\n")
            
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
    

#Funktioner för import av fil.
def importCD():
    """ Testar om fil finns, om svaret är sant får användaren välja om de vill importera filen eller ej. """

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
    """ Testar om fil finns, om svaret är sant får användaren välja om de vill importera filen eller ej. """

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
    """ Testar om fil finns, om svaret är sant får användaren välja om de vill importera filen eller ej. """

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



#Initialisering av program.
print("Enter your library's name and city:\n")
name = input(str("Name: "))
city = input(str("City: "))
temp_library = Library(str(name), str(city))

importCD(), importBook(), importMovie()
mainMenu(temp_library.name, temp_library.city)
