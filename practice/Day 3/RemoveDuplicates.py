'''Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
'''
word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))

# version 2
word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))

#version 3
word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort
print(" ".join(word))