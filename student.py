class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def pass_or_fail(self):
        if self.marks > 90:
            print(f"{self.name} got Distinction")
        elif self.marks > 75:
            print(f"{self.name} got First class")
        elif self.marks > 35:
            print(f"{self.name} Passed")
        else:
            print(f"{self.name} Failed")


john = Student(1, "John", 80)
john.pass_or_fail()
