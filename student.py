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


student_id = int(input("Enter your Student ID number"))
student_name = input("Enter your name")
student_marks = int(input("Enter your marks"))

student_object = Student(student_id, student_name, student_marks)
student_object.pass_or_fail()
