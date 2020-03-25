from statistics import median

print("This program will ask you for name, age and shoe size of three different people.")

person1_name=str(input("Please enter the first persons name: "))
person1_age=int(input("Please enter the first persons age: "))
person1_shoe=int(input("Please enter the first persons shoe size: "))

person2_name=str(input("Please enter the second persons name: "))
person2_age=int(input("Please enter the second persons age: "))
person2_shoe=int(input("Please enter the second persons shoe size: "))

person3_name=str(input("Please enter the third persons name: "))
person3_age=int(input("Please enter the third persons age: "))
person3_shoe=int(input("Please enter the third persons shoe size: "))

person_list=[person1_name, person1_age, person1_shoe,
             person2_name, person2_age, person2_shoe,
             person3_name, person3_age, person3_shoe]

all_ages=[person1_age, person2_age, person3_age]
all_ages_sorted=(sorted(all_ages))
oldest_person=all_ages_sorted[-1]

all_shoes=[person1_shoe, person2_shoe, person3_shoe]
all_shoes_sorted=(sorted(all_shoes))
median_shoe=median(all_shoes_sorted)

#För att få reda på vilket index den äldsta personen har görs följande.
oldest_person_index=person_list.index(oldest_person)

#När indexet hämtats vet jag sedan tidigare att namn ligger ett steg innan i listan och skostorlek ligger ett steg efter.
name_index=oldest_person_index-1
shoe_index=oldest_person_index+1
print("The oldest person is",person_list[name_index],"and has size",person_list[shoe_index],"shoes.")

#Print av namn och ålder för den som har median skostorlek.
median_shoe_index=person_list.index(median_shoe)

name_index2=median_shoe_index-2
age_index2=median_shoe_index-1
print("The person with median shoe size is",person_list[name_index2],"and he is",person_list[age_index2],"old.")