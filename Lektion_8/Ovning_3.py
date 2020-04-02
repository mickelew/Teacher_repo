with open("Ovning_1_text.txt", "a") as My_File:
    My_File.write("\nPrövar att lägga till text.")

with open("Ovning_1_text.txt", "r") as My_File:
    print(My_File.read())
