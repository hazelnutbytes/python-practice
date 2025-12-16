class Student:
    name = ''
    rollnumber = 0

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollnumber)

s1 = Student()
s1.name = "Hazel"
s1.rollnumber = 42
s1.display()
