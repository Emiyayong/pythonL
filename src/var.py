'*一个星号表示收集剩余参数 ** 两个星号可收集关键字参数'
def story(**kwds):
    return 'Once upon a time,there was a {job} called {name}.'.format_map(kwds)
def power(x,y,*other):
    if other:
        print('Received redundant parameters',other)
    return pow(x,y)
def insterval(start,stop=None,step=1):
    if stop is None:
        start,sotp=0,start
    result=[]
    i=start
    while i<step:
        result.append(i)
        i+=step
    return result
print(story(job='programor',name='gouyong',girlfrend='wangyun'))
print(power(1,2,'power',"I love you wangyun"))
print(insterval(10))
'递归函数'
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5));
def powerf(x,n):
    if n==0:
        return 1
    else:
        return x*powerf(x,n-1)
print(powerf(5,2))