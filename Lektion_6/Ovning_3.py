correct_answer = 30
user_input = 0

while user_input != correct_answer:
    user_input = int(input("Guess the correct number: "))
    print()
    
    if user_input < correct_answer:
        print("That's too low. Try again!")
    elif user_input > correct_answer:
        print("That's too high. Try again!")
else:
    print("That's the correct number!")