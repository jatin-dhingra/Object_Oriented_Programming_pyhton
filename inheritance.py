class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.mark=[]

    def avg(self):
        return sum(self.mark)/len(self.mark)

class  Workingstudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)

        self.salary=salary


jatin=Workingstudent('jatin','VIT',15)
print(jatin.name,jatin.school)
jatin.mark.append(99)
jatin.mark.append(98)
jatin.mark.append(98)
print(jatin.avg())
