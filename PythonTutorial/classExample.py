class Person:
    def __init__(this, firstName, lastName, age):
        this.firstName = firstName
        this.lastName = lastName
        this.age = age

    def printName(this):
        print(this.firstName, this.lastName, this.age)

    def toString(this):
        line1 = "My name is: " + this.firstName + " " + this.lastName + ", age: {}"
        return line1.format(this.age)

# Child class
class Student(Person):
    def __init__(self, firstName, lastName, age, grade):
        super().__init__(firstName, lastName, age)
        self.grade = grade

    def show(self):
        print(f"My name is {self.firstName}, {self.age}  , grade: {self.grade}")

p1 = Person("John", "Lee", 36)
print(p1.toString())
p1.printName()

student1 = Student("Mike", "Olsen", 12, 6)
student1.show()

