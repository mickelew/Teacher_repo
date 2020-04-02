My_File_Array = []

with open("Ovning_1_text.txt", "rt") as My_File:
    for line in My_File:
        My_File_Array = My_File.read().splitlines()
    
print(My_File_Array)
