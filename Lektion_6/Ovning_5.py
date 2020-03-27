#Missuppfattade uppgiften enligt nedan.

first_list = [1, 5, 6, 8, 9]
second_list = [2, 4, 7, 9, 10]

for first, second in zip (first_list, second_list):
    print(f"{first},{second}",end=" ")

#Rätt svar.
third_list = [3, 7, 9, 2, 6]
fourth_list =[2, 3, 6, 7, 9]

combined_list = []
for number in fourth_list:
    combined_list.append((number, third_list.index(number)))
print(combined_list)