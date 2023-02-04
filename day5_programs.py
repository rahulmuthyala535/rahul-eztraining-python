# import random as r
# x = 'i love sweets'

# print(r.sample(x, 4))  # prints any 4 letters

# a = [1, 2, 3, 4, 5, 6]
# r.shuffle(a)
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# print(r.choice(a))
# b = "welcome back"
# print(r.choice(b))

# a = r.random()
# print(a)
# # will returns randoms between 0.0 to 1.0 excludes 1.0

# print(r.randint(20, 30))

# a = [1, 2, 3, 4, 5, 6]
# print(r.choices(a, k=8))

# n = 'i love sweets'
# print(r.choices(n,k=3))

'''
import calendar
print("full calendar")
print(calendar.calendar(2022))

print("particular month")
print(calendar.month(2023, 2))

print("first day of the week")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2023, 2))
'''
# prg=display date time
# import datetime
# a = datetime.datetime.now()
# print(a)

# mv = a.strftime('xy')
# fv = a.strftime('yx')

# ##functions

# def sample():       #without arg without result
#     print("eacca")
#     print("sdcdc")


# sample()
# # print("wxsx")
# sample()
# '''
# def multi():        #without arg with return

#     a = int(input('enter a num :'))
#     b = int(input('enter a num :'))
#     c = int(input('enter a num :'))
#     d = a*b*c
#     # print(d)
#     return d

# # multi()
# res = multi()
# print(res)'''


# def mul(a, b, c):  # with arg without return
#     d = a*b*c
#     print(d)


# mul(0, 2, 5)


# def mul(a, b, c):
#     d = a*b*c
#     return (d)


# res = mul(4, 2, 5)
# print(res)

# def multi(l):
#     d = 1
#     for i in l:
#         if i % 2 == 0:
#             d = d*i
#     return d


# a = multi([1, 2, 3, 4, 5])
# print(a)

# find factors of the given number using func type2
# print multiplicatin table of given num by type3
# find out sum of digits of the given number using func type 4


# def lemon():
#     a = 21
#     b = int(input('enter no of lemons :'))
#     if a > b:
#         print(a-b)
#     else:
#         print(b-a)


# lemon()


# def factor() -> list:
#     a = int(input('enter a num :'))
#     l = []
#     for i in range(1, a+1):
#         if a % i == 0:
#             l.append(i)
#     return l


# print(factor())

# def mul_table(n):
#     for i in range(1, 11):
#         print(n, '*', i, '=', n*i)


# n = int(input('enter a number:'))
# mul_table(n)

'''
def sum_digits(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum = sum+rem
        n = n//10
    return sum


n = int(input('enter the number '))
res = sum_digits(n)
print(res)'''


# def display():
#     n = int(input('enter a num :'))
#     if n == 1:
#         display()
#     else:
#         print('once')


# display()


# # factorial
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)


# a = fact(2)
# print(a)


# n = int(input('enter number :'))
# a = 0
# b = 1
# sum = 0
# count = 1
# while (count < +n):
#     print(sum, end=' ')
#     count()
