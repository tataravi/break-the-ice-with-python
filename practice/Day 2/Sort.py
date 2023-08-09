# takes list of comma separated words as input and generates sorted list
# input: test, ping, order, fast, quick
# output: fast, order, ping, quick,test

lst = input().split(',')
lst.sort()
print(",".join(lst))

# another version
def my_func(e):
    return e[0]

my_list = input('Enter a comma separated string: ').split(",")
my_list.sort(key=my_func)
print(",".join(my_list))