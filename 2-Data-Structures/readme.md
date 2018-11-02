# 2: Python Data Structures
## Learning Objectives
* Lists and tuples
* Sets
* Dictionaries

## Video: Lists and tuples
### Tuples
* Ordered sequence
* "Ratings" are values inside parenthesis
* Written as comma-separated elements within parenthesis

```Python
Ratings = ('disco', 2, 3.23)
```
```Python
Ratings[0]: "disco"
```
```
Ratings[0:2]: ("disco", 2)
```

methods:
* .extend(): add as separate elements
* .append(): add  elements nested as one
* del(A[0])
* .split(","): splits
* A = [a, b, c]  
B=A[:] copy A
```Python
#Upper/lower
A: ['a','b','c']
A = A.upper([1])
A: ['a','B','c']

A = A.lower([1])
A: ['a','b','c']
```
## Video: Sets
### Sets
* A type of collection
    * You can input different Python types like lists, tuples
* Unlike lists and tuples, they are unordered
    * they do not record element position
* Only have unique elements, therefore only one of a particular element in a set

```Python
# Creating a set
Set1 = {0,'a',2.1,0,2}
Set1: {0,'a',2,2.1}
```
* Converting to set
```Python
# .set()
A = ['a','b','a','c']
A = set(A)
A: {'a','b','c'}
```
### Set operations
```Python
# .add()
A = {'a','b','c'}
A.add("NSYNC")
A: {'a','b','c','NSYNC'}
```
```Python
#.remove()
A: {'a','b','c','NSYNC'}
A = A.remove("NSYNC")
A: {'a','b','c'}
```
```Python
# find item
A: {'a','b','c'}
"a" in A
> True

"d" in A
> False
```
### Math Operations
```Python
# Venn-diagram
A = {'a','b','c','d'}
B = {'c','d','e','f'}

# Intersect: "&"
C = A & B
> C: {'c','d'}

# .union()
D = A.union(B)
> D = {'a','b','c','d','e','f'}
```
```Python
# .issubset()
C.issubset(A)
> True

# .issuperset()
A.issuperset(C)
> True
```
```Python
# .difference
A.difference(B)
> {'a','b'}
```
## Video: Dictionaries
![1](./1.png)
* Dictionaries are denoted by curly brackets {}
* The keys have to be immutable and unique
* The values can be immutable, mutable, and duplicates
* Each key and value pair is separated by a comma
```Python
Dic1 = {"key 1":1, "key 2": "a", "key 3": [2,'a',2.11], "key 4": 3.1415}

> Dic1: {'key 1': 1, 'key 2': 'a', 'key 3': [2, 'a', 2.11], 'key 4': 3.1415}
```
```Python
# ."name"[]
Dic1["key 3"]
> [2, 'a', 2.11]

Dic1["key 2"]
> 'a'
```
```Python
# Add new
Dic1['key blah']='blah entry'
> Dic1: {'key 1': 1, 'key 2': 'a', 'key 3': [2, 'a', 2.11], 'key 4': 3.1415, 'key blah': 'blah entry'}
```
```Python
# delete entry
del(Dic1['key 1'])
> Dic1: {'key 2': 'a', 'key 3': [2, 'a', 2.11], 'key 4': 3.1415, 'key blah': 'blah entry'}
```
```Python
# check indexes
"key blah" in Dic1
> True
```
```Python
# .keys() 
Dic1.keys()
> dict_keys(['key 2', 'key 3', 'key 4', 'key blah'])
```
```Python
# .values
Dic1.values()
> dict_values(['a', [2, 'a', 2.11], 3.1415, 'blah entry'])
```
## Lab - Dictionaries