x,y = map(int,input().split(','))
lst = []

for i in range(x): # looping till x
    tmp = []
    for j in range(y): # looping till y
        tmp.append(i*j) # fill the array
    lst.append(tmp)

print(lst)

# another version
x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)