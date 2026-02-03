class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        if self.__marks >= 86:
            return "A"
        elif self.__marks >= 72:
            return "B"
        elif self.__marks >= 64:
            return "C"
        elif self.__marks >= 50:
            return "D"
        else:
            return "F"

s1 = Student("Omer")
s2 = Student("Ahmed")
s1.set_marks(82)
s2.set_marks(91)
print("Name:", s1.name, "Marks:", s1.get_marks(), "Grade:", s1.calculate_grade())
print("Name:", s2.name, "Marks:", s2.get_marks(), "Grade:", s2.calculate_grade())
