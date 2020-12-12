# Map definition: Return an iterator that applies a function to every item of iterable, 
# yielding the results. If additional iterable arguments are passed,
#  the function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, 
# the iterator stops when the shortest iterable is exhausted.

# applying map on a single iterable
def square(x):
    return x**2
a = list(range(0,10))
print(a)
b = list(map(square,a))
l = list(map(lambda x: x**2 ,a))
print(b)

print(l)

# applying map on a more than one iterable
def mul(x,y):
    return x*y
a = list(range(0,10))
c = list(range(10,21))
b = list(map(mul,a,c))
print(b)

# Applying a function to more iterables of different lengths using the map() function
# [INFO] If multiple iterables given are of different lengths, the map iterator stops when the shortest iterable is exhausted.
def multiply(x,y,z):
    return x*y*z
num1=[1,2,3,4,5,6,7,8,9,10]
num2=[2,4]
num3=[2,3,4,5,6]
s=map(multiply,num1,num2,num3)
print (list(s))

# Accessing elements in the map object using the next() function
a = list(range(0,11))
l = map(lambda x: x**2 ,a)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

# Applying a built-in function to an iterable (string) using the map() function
colors=['red','yellow','blue']
print(list(map(str.capitalize, colors)))
print(list(map(str.upper, colors)))

# Make an iterator that computes the function using arguments obtained from the iterable. 
# Used instead of map() when argument parameters are already grouped in tuples from a single iterable
from itertools import starmap
a = list((1,2,3))
b = list((1,2,3))
c = []
for i in list(range(len(a))):
    c.append((a[i],b[i]))
c = tuple(c)
print(c)
def mul(x,y):
    return x*y

a = starmap(mul, c)
print(list(a))

num=starmap(lambda x,y:x+y,[(0,1),(1,2),(2,3)])
print(list(num))