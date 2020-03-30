# Detta program skapar en randomiserad lista med helta och ger talen på index 0 och 1 namnen A och B.
# Sedan testas om A > B och om det är sant byter värdena plats i listan. 
# Detta görs tills hela listan gåtts igenom.

import random
original_list = []

def random_numbers_list(list_length = 10):
    """Låter användaren välja ett heltal som bestämmer hur lång lista som skapas.
      
       Om inget heltal väljs, görs listan 10 heltal lång. """

    for i in range (0,list_length):
        x = random.randint(0, 99)
        original_list.append(x)


def name_element_A(name_list):
    """Ger siffran på index 0 i random_numbers_list namnet A. """

    A = int(original_list[0])
    return A


def name_element_B(name_list):
    """Ger siffran på index 1 i random_numbers_list namnet A. """

    B = int(original_list[1])
    return B


def A_bigger_then_B(element_A, element_B):
    """Kontrollerar om name_element_A är större än name_element_B """
        
    if element_A > element_B:
        original_list[0], original_list[1] = original_list[1], original_list[0]
        original_list.append(original_list[0])
        original_list.append(original_list[1])
        original_list.remove(original_list[0])
        original_list.remove(original_list[0])  

    elif element_A < element_B:
        original_list.append(original_list[0])
        original_list.append(original_list[1])
        original_list.remove(original_list[0])
        original_list.remove(original_list[0])
        
        
random_numbers_list()

print("Listan innan sortering:")
print(original_list,"\n")

i = 0
while i < len(original_list):

    A_bigger_then_B(name_element_A(original_list), name_element_B(original_list))
    
    i += 1

print("Listan är nu sorterad så variabeln B alltid kommer före variabeln A:")
print(original_list)




