# private access modifier
class Employe:
    def __init__(self):
        self.__name = "Mushfikur"

e = Employe()
# print(e._Employe__name)

# protected access modifier

class Student:
    def __init__(self):
        self.name = "Mushfikur"
    def _funname():
        print("Code with Mushfikur")

s = Student()
print(s._funname())