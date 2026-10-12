def func(x):
    return x+5
func2 = lambda x,y: x+y
print(func2(3,4))
d=func(2)
print(d)

a=[1,2,3,4,5,6,7,8,9,10]

newList= list(map(lambda x:x+5,a))
print(newList)

b=[1,2,3,4,5,6,7,8,9,10]

newlist= list(filter(lambda x:x%2==0,b))
print(newlist)