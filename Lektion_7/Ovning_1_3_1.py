
# Denna uppgift är att ta emot ett tal från användaren och beroende på om talet
# är högre eller lägre än fem, skriva ut två olika resultat.

user_number_input = int(input("Pick a number. Must be an integer: "))

if user_number_input <= 5:
    for num in range(user_number_input+1):
        for i in range(num):
            print(num, end="")
        print()
elif user_number_input > 5:
    print(str(user_number_input)*user_number_input)