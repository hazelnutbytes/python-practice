class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def show_manager_info(self):
        print("Role: Manager")
        print("Team size:", self.team_size)

m1 = Manager("Mahek", 101, 8)
m1.show_details()
m1.show_manager_info()
