class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show(self):
        print(self.name, self.course)

s1 = Student("Jacob Sugun", "CSDS")
s1.show()
