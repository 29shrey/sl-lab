class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.age = input("Enter student age: ")
        self.marks = []

    def accept(self):
        for i in range(3):
            self.marks.append(input("Enter subject " + str(i+1) + " marks: "))


    def display(self):
        print("Name: "+ self.name)
        print("Age: "+ self.age)
        print("Marks: ", self.marks)


print("Student 1:")
s1 = Student()
s1.accept()

print("Student 2:")
s2 = Student()
s2.accept()

print("Student 1::")
s1.display()
print("STudent 2::")
s2.display()