list_numbers = [2,4,6,8,10,11,12,15,16]

for numbers in list_numbers:
    if numbers % 2 == 0:
        print(numbers)
        continue
    elif numbers % 2 == 1:
        print("Not allowed!")
        break
