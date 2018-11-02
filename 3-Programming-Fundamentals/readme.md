# 3: Python Programming Fundamentals
## Learning Objectives
* Conditions and Branching
* Loops
* Functions
* Objects and Classes

## Video: Conditions and Branch
### Logic Operators
```Python
not(True)
> False
```
![1](./1.png)  
![2](./2.png)

## Video: Loops & Range
### Range
```Python
# range(N)
A = [1,2,4,4,5]

```

```Python
squares = ["r","y","g","p","b"]

> squares: ['w', 'y', 'g', 'p', 'b']

for i in range(0,3):
    squares[i] = "w"
print(squares)
> ["w","w","w","p","b"]
```
```Python
for i in squares:
    squares[i] = "w"
print(squares)
> ["w","w","w","w","w"]
```

```Python
# enumerate()
for i, square in enumerate(squares):
    print(i,squares)
```

### While loop
```Python
values=['o','o','p','b']

Newsquares=[]
i=0

while(squares[i]=='o'):
    Newsquares.append(values[i])
    i++
print(Newsquares)
```
```Python
dates = [1982,1980,1973]
N=len(dates)

for i in range(N):
    print(dates[i])
```

```Python
for i in range(0,8);
    print(i)
```
## Video: Functions
* A chunk of code which takes input and produce output

### Built-in functions
```Python
A = [1,3,2,6,5]

L = len(A) # finds length of A
> 5

L = sum(A) #adds all elements
> 17

# Sorted vs sort
L = sorted(A)
> L: [1,2,3,5,6]

A.sort()
> A = [1,2,3,5,6]
```
* Making Functions

```Python
def add1(a):
    b = a + 1;
return(b)

add1(5)
> 6
```
* Triple-quote help attribute
```Python
def add1(a):
"""
this function takes input a, adds one, and outputs b
"""
    b = a + 1;
return b

---
help(add1)
> Help on function add1 in module _main_: add1(a) this function takes input a, adds one, and outputs b
```
* Multiple parameters

```Python
def Mult(a,b):
    c = a * b;
return c
---
Mult(2,3)
> 6
```
* No parameter function
```Python
def MJ()
    print('Michael Jackson')
---
MJ()
> 'Michael Jackson'
```
[Reference](http://www.astro.up.pt/~sousasag/Python_For_Astronomers/Python_qr.pdf)

## Video: Objects and Classes
### Built-in Types in Python
* Each data type is an **Object**
    * int
    * float
    * string
    * List
    * Dictionary
    * Bool
* Every object has:
    * a .type()
    * an internal data representation (blueprint)
    * a set of procedures for interacting with the object (methods)
* an object is an instance of a particular type

### Methods
* A class or type's methods are functions that every instance of that class or type provides
* It's how you interact with the data in an object
* Sorting is an example of a method that interacts with the data in the object

```Python
Ratings = [4,5,2,9,4]
Ratings.reverse()
# .reverse() is the method
# Ratings is the object
# [4,5,2,9,4] is the data
```
### Class
![3](./3.png)
* You can create your own classes
```Python
class Circle(object):
class Rectangle(object):
```
![4](./4.png)

* defining a class
```Python
def _init_(self,radius.color):
    self.radius = radius;
    self.color = color;
```
* Create an object of class circle:

```Python
RedCircle = Circle(10,"red")
```
* Change the attributes
```Python
C1=Circle(10,"red")
C1.color="blue"
```
### Methods
* define a method:
```py
def _init_(self,radius.color):
    self.radius = radius;
    self.color = color;
# define a method:
def add_radius(self,r):
    self.radius = self.radius + r
    return(self.radius)
```
* to call a method:
```py
# use dot (.) notation
C1.add_radius(8)
```
* dir() used to display data attributes and methods associated with the class

```py
dir(nameOfObject)
> _method_
```

