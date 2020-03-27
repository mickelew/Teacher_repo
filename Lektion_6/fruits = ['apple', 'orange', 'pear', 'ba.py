fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket_space = int(input("Hur många frukter får plats i korgen?: "))
my_basket = []

while len(my_basket) <= basket_space-1:
    for x in fruits:
        if len(my_basket) < basket_space:
            my_basket.append(x)
print(my_basket)