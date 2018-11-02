# Video: Loops and Range
squares = ["r","y","g","p","b"]


''' Iteration over range

for i in range(0,3):
    squares[i] = "w"
print(squares)
'''
'''
for i in squares:
        squares[i] = "w"
print(squares)
'''
values=['o','o','p','b']

Newsquares=[]
i=0

while(squares[i]=='o'):
    Newsquares.append(values[i])
    i = i+1
print(Newsquares)