print("Detta program ska göra om texten 'Jag tYcker om äGg' till texten 'jAG tYCKER iNTE oM SPAM'")

initial_string = "Jag tYcker om äGg"
inte_var = " inte "
spam_var = "SPAM"
space_var = " "

initial_string = initial_string.split(" ", 2)
initial_string = inte_var.join(initial_string)
initial_string = initial_string.title()
initial_string = initial_string.swapcase()

inte_var = inte_var.title()
inte_var = inte_var.swapcase()

initial_string = initial_string.replace(inte_var, space_var, 1)
print(initial_string)

