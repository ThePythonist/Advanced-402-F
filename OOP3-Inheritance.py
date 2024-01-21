# class A:
#     def sayhello(self):
#         print("Hello")
#
#
# class B(A):
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()

# -------------------------------------------

class Father:
    def __init__(self, familyname, address, city, job):
        self.familyname = familyname
        self.address = address
        self.city = city
        self.job = job

    def sayhello(self):
        print("Hello")


class Child(Father):
    def __init__(self, familyname, address, city, university, fieldofstudy, job=None):
        super().__init__(familyname, address, city, job)
        self.uni = university
        self.field = fieldofstudy

    def saygoodbye(self):
        print("Goodbye")


ahmad = Father("Hosseini", "Ekbatan,Varzesh St", "Tehran", "Salesman")
ramin = Child("Hosseini", "Ekbatan,Varzesh St", "Tehran", "Sharif University", "Computer Engineering")

print(ramin.job)
