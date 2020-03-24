X=1
Y=4    
addresses={"Adam":"Ormvägen 5",         
           "Bella":"Klockgatan 1",
           "Cornelia":"Vikingagatan 3"} 

#Uppgift 6
#cars = lista
cars=["Volvo","Opel","BMW"]
numbers1={1,2,3,X,6}
numbers2={Y,2,3,4,7}

addresses["Daniel"]="Prinsgränd 2"

#Uppgift 7/8
print(cars[X],"\n")
#print(cars[Y]) returnerar ett felmeddelande eftersom den hämtar platsen i listan
#från variabeln Y som är 4. Cars innehåller innehåller bara 3 objekt, 0-2.

#Uppgift 9
#Listan sorteras alfabetiskt.
cars.sort()
print(cars[0],"\n")

#Uppgift 10
#Båda listorna uppdateras.
cars_2=cars
cars_2.append("Saab")
print(cars_2)
print(cars,"\n")

