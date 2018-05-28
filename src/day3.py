class Student(object):
    def __init__(self,name):
        self.name=name;
    def __str__(self):
        return "Student object(name) is %s" % self.name;
class Fib(object):
    def __getitem__(self,item):
        if isinstance(item,int):
            a,b=1,1;
            for x in range(item):
                a,b=b,a+b,
            return a;
        if isinstance(item,slice):
            start =item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1;
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                    a,b=b,a+b
            return l




