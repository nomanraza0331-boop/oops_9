class person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
print("person class")

class acedmics():
    def __init__(self,education,marks):
        self.education=education
        self.marks=marks
  
 
print("acedmics class")

class skills():
    def __init__(self,skillset):
        self.skillset=skillset
print("skills class")


class employe(person,acedmics,skills):
    def __init__(self, name, age, gender,education,marks,skillset,empid,dept,company,salary):
        person.__init__(self,name,age,gender)
        acedmics.__init__(self,education,marks)
        skills.__init__(self,skillset)
        self.empid=empid
        self.dept=dept
        self.company=company
        self.salary=salary

    def display_empdata(self):
        print(self.name,self.age,self.gender,self.education,self.marks,self.skillset,self.empid,self.dept,self.company,sep="\n")

E1=employe("noman",18,"male","BCA","A",["C","C++","Python"],[85,75,79,98],"develpment","google")
E1.display_empdata()

        

