# Detta program skapar en lista av heltal och väljer ut ett element i listan som får variabeln "p".
# Därefter testas resten av listan mot "p" och sorterar ut de tal som är mindre/större 
# och läggs i varsin egen lista. 
# Slutligen sammanförs alla listor till en och resultatet presenteras.

import random

unsorted_list = []
smaller_list = []
larger_list = []


def list_of_numbers(list_length = 10):
    """Skapar en lista med 10 heltal."""
    for i in range (0, list_length):
        x = random.randint(0, 99)
        unsorted_list.append(x)

#Initiera funktionen.
list_of_numbers()

#Ge "p" ett värde.
p = unsorted_list[5]

def sort(name_list):
    """Funktion som sorterar och lägger till element i nya listor utefter givna förhållanden."""
    
    #Skapa nya listor.
    for element in name_list:
        if element < p:
            smaller_list.append(element)
        elif element > p:
            larger_list.append(element)

    #Sortering.
    if len(smaller_list) > 1:
        smaller_list.sort()

    if len(larger_list) > 1:
        larger_list.sort()

#Initierar funktionen.
sort(unsorted_list)

#Gör om p till en lista.
p = [p]

def sort_smaller_larger():
    """Sammanfogar det redan sorterade smaller,larger samt p-listorna."""

    sorted_list = [smaller_list] + [p] + [larger_list]
    return sorted_list

print()
print(f"Sorterad lista: {sort_smaller_larger()[0]} -> {sort_smaller_larger()[1]} -> {sort_smaller_larger()[2]}")



