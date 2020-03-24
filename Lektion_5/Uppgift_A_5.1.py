X=1
Y=4
#Ändrade ordning i dictionaryt för att tyddliggöra sorteringen i kommande steg.    
addresses={"Adam":"Ormvägen 5",         
           "Cornelia":"Vikingagatan 3",
           "Bella":"Klockgatan 1"} 
cars=["Volvo","Opel","BMW"]
numbers1={1,2,3,X,6}
numbers2={Y,2,3,4,7}
addresses["Daniel"]="Prinsgränd 2"

#Allt skrivs ut i dictionarys ordinarie ordning.
for k, v in addresses.items():
    print(k, v)

#Allt skrivs ut i alfabetisk ordning.
#dict(sorted(addresses.items() = initerar sortering för addresses
#key=lambda x: x[0])) = specificerar att sortering sker på index 0 och specificeras av lambda (namnlös funktion)
#i form av x: x[0]. 
print()
alfabetisk=dict(sorted(addresses.items(), key=lambda x: x[0])) #Blir överflödig efter hjälp från klassen.
print(sorted(alfabetisk.items())[-1][1])

#Uppgift 5.2
print()
addresses={v: k for k, v in addresses.items()}
print(sorted(addresses.items())[0][1])

