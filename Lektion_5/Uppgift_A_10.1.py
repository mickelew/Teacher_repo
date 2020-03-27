X=1
Y=4    
addresses={"Adam":"Ormvägen 5",         
           "Bella":"Klockgatan 1",
           "Cornelia":"Vikingagatan 3"} 

cars=["Volvo","Opel","BMW"]
numbers1={1,2,3,X,6}
numbers2={Y,2,3,4,7}

addresses["Daniel"]="Prinsgränd 2"

#Uppgift 10.1
cars_3=cars.copy()
print(cars_3,"\n")

#Uppgift 10.2
cars.extend(["BMW","Opel","Volvo"])
cars.sort(reverse=True)
print(cars,"\n")

#Uppgift 10.3
#Omvandla lista till set med set()
unique_cars=set(cars)
print(unique_cars,"\n")

#Uppgift 11
#numbers1 / numbers2 = set

#Uppgift 12
#De innehåller 1,2,3,6 och 2,3,4,7

#Uppgift 13
numbers_intersec=numbers1 & numbers2
print(numbers_intersec,"\n")

#Uppgift 14
numbers_union=numbers1 | numbers2
print(numbers_union,"\n")

#Uppgift 15
numbers_difference=numbers1.difference(numbers2)
print(numbers_difference)
