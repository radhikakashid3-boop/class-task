#Task1
class Student:
    def __init__(self, r, n, m, a):
        self.roll = r
        self.name = n
        self.marks = m
        self.address = a

class Teacher:
    def __init__(self, n, s, d, a):
        self.name = n
        self.salary = s
        self.dep = d
        self.address = a

class College:
    def __init__(self, s, t):
        self.student = s
        self.teacher = t

s1 = Student(101, "Radhika", 90, "Nashik")
t1 = Teacher("Amit", 50000, "Computer", "Pune")
c1 = College(s1, t1)

print(c1.student.roll)
print(c1.student.name)
print(c1.student.marks)
print(c1.student.address)

print(c1.teacher.name)
print(c1.teacher.salary)
print(c1.teacher.dep)
print(c1.teacher.address)

#Task2
class Student:
    def __init__(self, n, a, *s):
        self.name = n
        self.age = a
        self.subjects = s


sub = ["python", "java", "DataAnalytics"]

num2 = Student("Radhika", 20, sub)

print(num2.name)
print(num2.age)
print(num2.subjects)
print(num2)
print(num2, type(num2), id(num2))