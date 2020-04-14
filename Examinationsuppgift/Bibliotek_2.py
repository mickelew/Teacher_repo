#Imports
from datetime import date






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
    return value

def valueMovie(purchasePrice, purchaseYear, condition):
    """ Gör en beräkning av värdet utifrån filmens inköpspris, ålder 
        och vilket skick den var i vid inlämnandet. """
        
    currentYear = date.today().year
    age = currentYear-purchaseYear

    value = purchasePrice*0.9**age*(condition/10)
    return value

print("Enter your library's name and city.\n")
name = input(str("Name: "))
city = input(str("City: "))
temp_library = Library(str(name), str(city))
    

temp_library.add_book("Alfons Åberg", "Sven Melander", 100, 1970, 240)
temp_library.add_cd("Ride the lightning", "Metallica", 100, 1984, 18)
temp_library.add_cd("Ride the lightning", "Metallica", 100, 1984, 18)
temp_library.add_cd("Black Album", "Metallica", 199, 1984, 18)
temp_library.add_movie("Indiana Jones", "Steven Spielberg", 100, 2000, 135, 5)

print(f"\n{temp_library.name}, {temp_library.city}\n")

print(f"These are the books currently in {temp_library.name}:")
for book in temp_library.bookRegister:
    print(f"Title: {book.title}, Author: {book.author}, Purchase price: {book.purchasePrice}:-, Purchase year: {book.purchaseYear}, Number of pages: {book.numberOfPages}, Value: {book.value:.2f}:-\n")

print(f"These are the CD's currently in {temp_library.name}:")
for cd in temp_library.cdRegister:
    print(f"Title: {cd.title}, Author: {cd.author}, Purchase price: {cd.purchasePrice}:-, Purchase year: {cd.purchaseYear}, Number of pages: {cd.numberOfTracks}, Value: {cd.value}:-\n")

print(f"These are the movies currently in {temp_library.name}:")
for movie in temp_library.movieRegister:
    print(f"Title: {movie.title}, Author: {movie.author}, Purchase price: {movie.purchasePrice}:-, Purchase year: {movie.purchaseYear}, Length in minutes: {movie.lengthMinutes}, Condition: {movie.condition}, Value: {movie.value:.2f}:-\n")