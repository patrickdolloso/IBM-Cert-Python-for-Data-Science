# 4: Working with Data in Python
## Learning Objectives
* Reading files with open
* Writing files with open
* Loading data with Pandas
* Working with and Saving data with Pandas

## Video: Reading files with open
[link to test.py file](./test.py)  
* In shell:  
```py
File1 = open("./path/file.txt","w")

# "w" is the mode for appending
# "r" is the mode for reading
# 'a' for appending
'''
Always close the file object using 
File1.close()
'''
```
```py
# to see file path
File1.name
>>> './path/file.txt'
# to see what mode
>>> 'r'
```
* Automatically close files
```py
with open("Example1.txt,"r") as File1:
    file_stuff=File1.read()
    print(file_stuff)
print(file_stuff)
print(File1.closed)
print(file_stuff)
```
* Place components into list
* as the program reads, it progresses to the end of the file

```py
# print the entire file
with open("Example1.txt"."r") as File1:
    file_stuff = File1.readline()
    print(file_stuff)

# each line is an element in a list
with open("Example1.txt"."r") as File1:
    file_stuff = File1.readlines()
    print(file_stuff)

# print out each line individually
with open("Example1.txt"."r") as File1:
    for line in File1:
        print(line)

# print out characters
with open("Example1.txt"."r") as File1:
    file_stuff=File1.readlines(4)
    print(file_stuff)
```


## Video: Writing files with open
[link to test2.py file](./test2.py)
```py
# create a file (if file exists, it will be overwritten)
File1 = open("./path/file2.txt","w")

# Write text to a file (\n is new line)
File1.write("This is line 1\n")

# Writes list L in as a loop
Lines = ["This is line A\n","This is line B\n","This is line C\n"]
with open("./test2a.txt","w") as File2:
    for line in Lines:
        File2.write(line)

# Append - Write this is line D in same file test2a.txt
with open("./test2a.txt","a") as File2:
    File2.write("This is line D")

# copy test2a.txt contents to a new file test2b.txt
with open("./test2a.txt","r") as readfile:
    with open("./test2b.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)
```
## Video: Loading Data with Pandas
[link to test3.py file](./test3.py)  
* pandas library functions  
![pic1](./pic1.png)
```py
# import pandas library
import pandas

# load csv file
csv_path='file1.csv'

```
## Video: Working with and saving Data

```py
# all the unique elements in a df
import pandas as pd
df['Released'].unique()

# for finding elements using inequalities

# all albums released after 1979
df['Released']>=1980 #check

df1=df[df['Released']>=1980]

# save to csv
df1.to_csv('new_songs.csv')
```