cls = lambda: print("\033[2J\033[;H", end='')
cls()
# str = []
# n = 6
# for i in range(0,n):
#     str += ['_ ']
# print(str)

# str[3] = 'p'
# print(str)

# final = ''
# for i in str:
#     final += i[0:2]

# print(final)

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

listi = []
for i in secretWord:
    listi += i
print(listi)
length = len(listi)

for idx,val in enumerate(listi):
    if val not in lettersGuessed:
        listi[idx] = '_ '
print(listi)

final = ''
for i in listi:
    final += i[0:2]

print(final)
        