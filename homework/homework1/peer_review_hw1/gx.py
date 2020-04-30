import sys


totalPalindromes = 0
file = open('/users/abrick/resources/english', 'r')
for word in file.readlines():
    word = word.strip()
    reversedWord = word[::-1]
    if (word == reversedWord):
        totalPalindromes += 1
print(totalPalindromes)
