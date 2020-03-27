fruits = ['apple','orange', 'pear', 'banana', 'grapes']
my_basket = []
room_basket = int(input("How much space for fruit do you have in your basket? Answer must be an integer: "))

while len(my_basket) < room_basket:
    for fruit in fruits:
        if len(my_basket) < room_basket:
            my_basket.append(fruit)

print("These are the fruits in your basket: ",my_basket)


    