print ('Enter n:', end='')
n = int(input()) #input() function takes input as string type
                #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

# Solution using Lambda function
print ('Enter n:', end='')
n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))