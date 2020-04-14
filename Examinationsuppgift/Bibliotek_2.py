
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

class Book(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt numberOfPages. 
        Används när en ny bok ska läggas till i registret. """

    def __init__(self, title, author, purchasePrice, purchaseYear, numberOfPages):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.numberOfPages = numberOfPages

class Movie(mediaAttributes):
    """ Kräver de fyra gemensamma attributen från mediaAttributes, samt lengthMinutes och condition. 
        Används när en ny film ska lägas till i registret. 
        Condition anges i ett värde mellan 1-10 där 1 = mycket sliten och 10 = mycket gott skick. """

    def __init__(self, title, author, purchasePrice, purchaseYear, lengthMinutes, condition):
        super().__init__(title, author, purchasePrice, purchaseYear)
        self.lengthMinutes = lengthMinutes
        self.condition = condition



print("Enter your library's name and city.\n")
name = input(str("Name: "))
city = input(str("City: "))
temp_library = Library(str(name), str(city))
    

temp_library.add_book("Alfons Åberg", "Sven Melander", 129, 1988, 240)
temp_library.add_cd("Ride the lightning", "Metallica", 199, 1984, 18)
temp_library.add_movie("Indiana Jones", "Steven Spielberg", 149, 1986, 135, 5)

print(f"{temp_library.name}, {temp_library.city}\n")

print(f"These are the books currently in {temp_library.name}:")
for book in temp_library.bookRegister:
    print(f"Title: {book.title}, Author: {book.author}, Purchase price: {book.purchasePrice}:-, Purchase year: {book.purchaseYear}, Number of pages: {book.numberOfPages}\n")

print(f"These are the CD's currently in {temp_library.name}:")
for cd in temp_library.cdRegister:
    print(f"Title: {cd.title}, Author: {cd.author}, Purchase price: {cd.purchasePrice}:-, Purchase year: {cd.purchaseYear}, Number of pages: {cd.numberOfTracks}\n")

print(f"These are the movies currently in {temp_library.name}:")
for movie in temp_library.movieRegister:
    print(f"Title: {movie.title}, Author: {movie.author}, Purchase price: {movie.purchasePrice}:-, Purchase year: {movie.purchaseYear}, Number of pages: {movie.lengthMinutes}, Condition: {movie.condition}\n")