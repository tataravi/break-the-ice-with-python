print('Enter a number:', end='')
n = int(input())
ans = {}
for i in range(1, n + 1):
    ans[i] = i * i
print(ans)

'''Solution Using: Dict
'''

try:
    num = int(input("Enter a number: "))
except ValueError as err:
    print(err)

dictio = dict()
for item in range(num + 1):
    if item == 0:
        continue
    else:
        dictio[item] = item * item
print(dictio)
