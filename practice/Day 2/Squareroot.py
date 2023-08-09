from math import sqrt # import specific functions as importing all using *
                      # is bad practice

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input().split(',')] # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

#print (D) # print as list ex: ['4', '6', '7']
print(",".join(D)) # print as string ex: 4,6,7

from math import * # importing all math functions
C,H = 50,30

# another version using map
def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')
D = list(map(calc,D))   # map is applying calc function on every element in D (iterable list) and storing as a list
print(",".join(D))