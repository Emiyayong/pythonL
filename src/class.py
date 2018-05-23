class Student(object):
    def __init_(self,name,score):
        self.__name=name
        self.__score=score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_srore(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError(score)
    def get_grage(self):
        if self.__score>=95 :
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

my=Student('gouyong',59)
print(my.get_name())
print(my.get_score())
my.set_srore(200)
print(my.get_score())