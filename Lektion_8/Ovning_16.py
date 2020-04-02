def test_open_closed():
    if My_File.closed:
        print("Filen är stängd.")
    else:
        print("Filen är fortfarande öppen.")

with open("Ovning_1_text.txt", "rt") as My_File:
    test_open_closed()

test_open_closed()