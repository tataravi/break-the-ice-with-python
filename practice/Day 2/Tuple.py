# Tuples in python are immutable ordered collection of data. The primary difference between tuples and lists is that
# tuples are immutable as opposed to lists which are mutable.

lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
                          # method name split. ',' inside split function does split where it finds any ','
                          # and save the input as list in lst variable

tpl = tuple(lst)          # tuple method converts list to tuple

print(lst)
print(tpl)