#Int
X=1
Y=4    

#Dict
addresses={"Adam":"Ormvägen 5",         
           "Bella":"Klockgatan 1",      #Dict
           "Cornelia":"Vikingagatan 3"} 
cars=["Volvo","Opel","BMW"]
numbers1={1,2,3,X,6}
numbers2={Y,2,3,4,7}

#Uppgift 3
print(addresses["Bella"],"\n")

#Uppgift 4
#Lägger till Daniel : Prinsgränd 2 i addresses
addresses["Daniel"]="Prinsgränd 2"
print(addresses,"\n")

#Uppgift 5
print("Antal keys i variabeln 'addresses':")
print(len(addresses))
