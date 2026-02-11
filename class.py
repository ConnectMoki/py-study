class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
        
lisa = Student('Lisa', 99)
print(lisa.get_grade())
bart = Student('Bart', 59)
print(bart.get_grade())

print(lisa._Student__name)