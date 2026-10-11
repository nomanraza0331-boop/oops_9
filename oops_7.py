class employee():
    def __init__(self,emp_id,emp_name,company):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.company=company

    def display(self):
        print("employee id:",self.emp_id)
        print("Employee name:",self.emp_name)
        print("company:",self.company)

class sales(employee):
    def __init__(self, emp_id, emp_name, company,profile,team):
        super().__init__(emp_id, emp_name, company)
        self.profile=profile
        self.team=team

    def display_sales(self):
        self.display
        print(self.profile,self.team)


class HR(employee):
    def __init__(self, emp_id, emp_name, company,managment_level):
        super().__init__(emp_id, emp_name, company)
        self.managment_level=managment_level

    def display_HR(self):
        self.display
        print(self.managment_level)

    class development(employee):
        def __init__(self, emp_id, emp_name, company,skills,project):
            super().__init__(emp_id, emp_name, company)
            self.skills=skills
            self.project=project

        def display_dev(self):
            self.display
            print (self.skills,self.project)

S1=sales(102,"sawez","TCS","junior sales executive","alpha")
H1=HR(103,"noman","infosys","HR manager")
D1=development()
        