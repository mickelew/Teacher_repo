# Uppdaterad Övning 1.3.1/1.3.2

def integer_to_string(integer):
    print("Svar:",str(integer)*integer)

user_number_input = int(input("Pick a number. Must be an integer: "))

if user_number_input <= 5:
    for num in range(user_number_input+1):
        for i in range(num):
            print(num, end="")
        print()
elif user_number_input > 5:
    integer_to_string(user_number_input)