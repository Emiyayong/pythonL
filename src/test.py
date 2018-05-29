def fib(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print(fib(10));
storage={}
storage['first']=[]
storage['second']=[]
storage['third']=[]
my_sister='Anne Lie Heland'
storage['first'].setdefault('Ane',[]).append(my_sister)