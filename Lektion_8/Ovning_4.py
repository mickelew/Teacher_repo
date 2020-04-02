
def read_last_lines(filename, no_of_lines):
    with open(filename,'r') as MyFile:
	    lines = MyFile.readlines()
	    last_lines = lines[-no_of_lines:]
	    for line in last_lines:
		    print(line)

#Gör ett test för att se om filen är importerad i python eller ej.
#Om filen körs direkt i python kommer __name__ == __main__,
#vid import blir __name__ == imports filnamn. 
if __name__ == "__main__":
	filename = "Ovning_1_text.txt"
	read_last_lines(filename,2)

