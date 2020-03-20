#
# Obs!
# Märkte när ni visade er lösning att den här är onödigt krånglig, 
# men låter den vara för att ni ska se hur jag tänkte.
#
print("Detta program ska göra om texten 'Jag tYcker om äGg' till texten 'jAG tYCKER iNTE oM SPAM'")

initial_string = "Jag tYcker om äGg"
inte_var ="inte"
spam_var = "SPAM"
space_var =" "
inte_space = space_var+inte_var+space_var

initial_string = initial_string.rsplit(" ", 2)
initial_string = inte_space.join(initial_string)

print("\nInte läggs till med .join")

print(initial_string)
initial_string = initial_string.title()
initial_string = initial_string.swapcase()

inte_var = inte_var.title()
inte_var = inte_var.swapcase()

print("\nFormatering av bokstäver görs med .title och .swapcase")
print(initial_string)

correct_string, inte_remove, agg_remove = initial_string.rsplit(" ", 2)
print("\niNTE och äGG lyfts ut med .rsplit och ersätts med SPAM.")
print(correct_string, spam_var)



