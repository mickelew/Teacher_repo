My_File_List = []

with open("Ovning_1_text.txt", "rt") as My_File:
    for line in My_File:
        My_File_List.append(line.rstrip())
    
print(My_File_List)
