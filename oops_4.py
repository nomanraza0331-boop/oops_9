class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    print("this is my parent class")

    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)

class student(person):
    def __init__(self, name, age, gender,roll,marks,school):
        super().__init__(name, age, gender)
        self.roll=roll
        self.marks=marks
        self.school=school

    print("this is my child class")

    def display_data(self):
        print("roll",self.roll)
        print("mark",self.marks)
        print("school",self.school)

s1=student("noman",18,"male",101,243,"SMK")
s1.display()
s1.display_data()