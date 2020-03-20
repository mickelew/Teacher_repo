from math import sqrt
print("Detta program räknar ut hypotenusan av en triangel.")
triangel_bas = int(input("Skriv in triangelns bas: "))
triangel_höjd = int(input("Skriv in triangelns höjd: "))
triangel_hypo = sqrt(triangel_bas**2 + triangel_höjd**2)
print(f"Hypotenusan är: {triangel_hypo}")