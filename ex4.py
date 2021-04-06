class Student():
    def __init__(self, name , surname, group, mark):
        self.name = name
        self.surname = surname
        self.group = group
        self.mark = mark
    
    def Scholarship(self):
        if self.mark == 5:
            return 100
        else:
            return 80

class Aspirant(Student):
    def __init__(self, name, surname, group, mark, article_name):
        super().__init__(name, surname, group, mark)
        self.article_name = article_name
    def Scholarship(self):
        if self.mark == 5:
            return 200
        else:
            return 180

Ivan = Student('Ivan', 'Pupkin', 'FM-11', 2)
Petya = Aspirant('Petya', 'Pupkin', 'FM-21', 5, 'Global warming')

a = [Ivan, Petya]
for i in range(len(a)):
    print(a[i].Scholarship())