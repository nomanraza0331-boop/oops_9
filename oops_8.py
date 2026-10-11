class person:
    def __init__(self,name,city):
        self.name=name
        self.city=city

class sports(person):
    def __init__(self, name, city,sports_name):
        super().__init__(name, city)

        self.sports_name=sports_name
  
class acedemics(person):
    def __init__(self,name,city,education,grade):
        super().__init__(name,city)
        self.education=education
        self.garde=grade

class skills(person):
    def __init__(self, name, city,skill_set):
        super().__init__(name, city)
        self.skill_set=skill_set

class employee(skills,acedemics):
    def __init__(self, name, city, skill_set):
        super().__init__(name, city, skill_set)

    


        