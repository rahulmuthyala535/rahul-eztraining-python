# #dictionary with keys and values
# d = {n: n*n for n in range(1, 5)}
# print(d)

# #calu
# old = {'rice': 10, 'dall': 28, 'oil': 36}
# new = {product: price*5 for (product, price) in old.items()}
# print(new)

# real = {'ram': 20, 'sai': 32, 'suresh': 18}
# now = {name: age for (name, age) in real.items()
#        if age > 20}
# print(now)

# ##create a list with 8 costomer names ,display a dictionary which has costomers names along with discounts for them from a particular shop

# import random
# #print(random.randint(1, 40))
# l1 = ['ram', 'sai', 'sri', 'pal', 'hari', 'ghh', 'err', 'cfrf']
# d = {}
# for i in l1:
#     discount = random.randint(1, 40)
#     d.update({i: discount})
# print(d)

# import random
# l1 = {'a', 'b', 'c'}
# l1_dict = {names: random.randint(1, 100) for names in l1}
# print(l1_dict)

# # l1 = ['a', 'b', 'c', 'd', 'e']
# l1 = list(map(str, input("enter the names :").split()))
# l2 = [455, 475, 450, 400, 444]
# d = {names: (marks/500)*100 for (names, marks) in zip(l1, l2)}
# # d2 = {names: (marks/500)*100 for (names, marks) in d.items()}
# #  for i in l2:
# #  percentage = (marks/500)*100}
# print(d)
# # print(d2)

# n = "hi i\'am \"sylvia\""
# print(n)

# #concatination -> s1+s2
# #reputation -> s1*3
# s = 'Rahul kanna'
# print('a' > 'b')
# print('a' < 'b')
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.casefold())
# print(s.center(10, '#'))
# print(s.count('r'))
# print(s.find('h'))
# print(format(s))
# print(s.replace('a', 'b'))
# print(s.isspace())
# print(s.removeprefix)

# x = 20
# print(id(x))
# x = 30
# print(id(x))
# l = [1, 2, 3]
# print(id(l))
# l.append(4)
# print(id(l))

'''mutable & immutable
mutable : can be changed after creation
eg: list, 
set, 
dictionary
immutable: can be changed after creation
eg: int, 
float '''
# ______________________Problems___________________________
# Get one string as input along with a character find out and
# display whether the particular character is in the string or not.
# s = list(map(str, input('Enter a string along with a character: ').split(', ')))
# print(s[0])
# print(s[1])
# givenStr = s[0]
# givenChar = s[1]
# if givenStr.find(givenChar, 0, len(givenStr)) != -1:
#     print('The string contains the character')
# else:
#     print('The string doesnt contains the character')

# Check whether the given string is palindrome or not.
# import math
# a = input("enter a string :")
# n = len(a)
# l = n//2
# x = 0
# for i in range(l):
#     if a[i] != a[n-1-i]:
#         x = 1
#         break
# if x == 1:
#     print("not a palindrom")
# else:
#     print("palindrom")

# after entering one string as input check if the string contains space or not
# if yes count no of spaces in the string.
# s2 = input('Enter a string: ')
# spaceChar = ' '
# if spaceChar in s2:
#     print('There are', s2.count(' '), 'spaces')
# else:
#     print('There are no spaces')

# create a list with vowels get one string as input count no of vowels from the string
# display the result.
# l = ['a', 'e', 'i', 'o', 'u']
# s = input('Enter a string: ')
# count = 0
# for i in l:
#     count += s.count(i)
# print(count)

# _________________Math module___________________
# print(math.ceil(2.4))
# print(math.floor(2.4))
# print(math.sqrt(25))
# print(math.factorial(6))
# print(math.pow(2, 4))
# print(math.fmod(10, 3))
# a, b = divmod(10, 3)
# print(a, b)
