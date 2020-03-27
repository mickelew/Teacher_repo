first_list = [5, 7, 1, 4, 8]
second_list = [1, 5, 8, 7, 4]

combined_list = [(number, first_list.index(number)) for number in second_list]

print(combined_list)