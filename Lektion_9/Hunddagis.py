#Class
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
    
    #Method - Kräver '()' när den kallas på av programmet.
    def fullname(self):
        return "{} {}".format(self.first, self.last)


#Instance - Hämtar funktionen från 'class Employee'.
emp_1 = Employee("Michael", "Levin", 50000)
emp_2 = Employee("Siri", "Brattberg", 55000)

#print(emp_1)
#print(emp_2)

print(emp_1.fullname())
print(emp_2.fullname())
