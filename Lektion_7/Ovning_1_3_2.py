
# Denna uppgift är att ta emot ett tal från en funktion och beroende på om talet
# är högre eller lägre än fem, skriva ut två olika resultat.

def integer_to_string(integer):
    print(str(integer)*integer)

user_number_input = int(input("Pick a number. Must be an integer: "))

if user_number_input <= 5:
    for num in range(user_number_input+1):
        for i in range(num):
            print(num, end="")
        print()
elif user_number_input > 5:
    integer_to_string(user_number_input)