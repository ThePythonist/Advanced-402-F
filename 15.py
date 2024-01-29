class Human:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.heigth = height
        self.weight = weight

    def talk(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


class Student(Human):
    def __init__(self, name, age, height, weight, studentcode, uni, fieldofstudy):
        super().__init__(name, age, height, weight)
        self.studentcode = studentcode
        self.uni = uni
        self.fieldofstudy = fieldofstudy

    def study(self):
        pass

    def get_to_university(self):
        pass


farzad = Human("Farzazd", 24, 183, 75)
kian = Student("kian", 21, 175, 70,"42423","Amir Kabir","Chemical Engineering")

kian.study()
