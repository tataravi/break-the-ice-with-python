lst = []

while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)

# version 2
def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s #generator function that suspends, packs and sends all return values to the caller

for line in map(str.upper, user_input()):
    print(line)

# version 3
def inputs():
    while True:
        string = input()
        if not string:
            return
        yield string

print(*(line.upper() for line in inputs()),sep='\n')