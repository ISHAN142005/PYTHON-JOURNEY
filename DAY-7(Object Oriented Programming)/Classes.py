# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). Eg. Form which contains the data for John Doe

class Employee:
    company="Google"

    def getSalary(self): # self is important here because self is a way to reference the object of the class which is being created
        return 34000
    
e1 = Employee() # An Object of class Employee is created here
print(e1.getSalary()) # Employee e's get salary method is called

e2= Employee()
print(e2.getSalary())
print(e2.company)

