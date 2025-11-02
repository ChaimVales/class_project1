class Student:
    def __init__(self,name:str, grades:list):
        self.name = name
        self.grades = grades

    def add_grade(self,grade):
        self.grades.append(grade)

    def average(self):
        average = 0
        for i in self.grades:
            average += i
        sum = average / len(self.average)
        return sum
    


        
