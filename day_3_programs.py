# lists

# list basic
l = [2, 4, 2, 3, 3.2, "ram"]
print(l)

print(l[2])
print(l[1:3])
print(len(l))
print(l.count(2))
l.append(30)
print(l)
l.remove(2)
print(l)
print(l.pop(-1))
l.remove("ram")
print(l)
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(3))

# program1
l = [2, 3, 4, 7, 8, 9, 1, 4, 5, 6]

for i in range(len(l)):
    print(l[i])

for j in l:
    print(j)


l = [2.3, 4.2, 9.2, 7.6, 15.4]

l = [input("enter the nubers :")]
print(l)

# program2
l = list(map(float, input("enter 5 float numbers :").split()))
sum = 0
avg = 0
for k in l:
    sum += k
print("sum: ", sum)
print("average :", sum/len(l))

# program3
l = list(map(int, input("enter 6 elements :").split()))
for i in l:
    if i % 2 == 0:
        print("even", i)


l = list(map(int, input("enter the numbers :").split()))
prod = 1
sum = 0
for k in l:
    prod *= k
    sum += k
if prod < 750:
    print("prod :", prod)
else:
    print("sum :", sum)


# creating a polindram number using string


a = input("enter a string :")
n = len(a)
l = n//2
x = 0
for i in range(l):
    if a[i] != a[n-1-i]:
        x = 1
        break
if x == 1:
    print("not a palindrom")
else:
    print("palindrom")


# lists


l = [2**i for i in range(1, 10)]
print(l)


l1 = ["vizag", "hyd", "chennai", "vijaywada"]
city = []
for i in l1:
    if "v" in i:
        city.append(i)
print(city)

l2 = [i for i in range(100, 201, 20)]
print(l2)


# sets


s1 = {1, 2, 3, 4}
s2 = {2, 4, 6, 8}
print(s1 | s2)
print(s1-s2)
print(s2-s1)

s3 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3}
print(s3.issuperset(s4))


# dictionary

d = {1: "one", 2: "two"}
print(d)
print(d.keys())
print(d.values())
print(dict.fromkeys(d))
print(dict.fromkeys(d, 40))
print(dict.fromkeys(d, 100))
print(d.items())
d.update({3: "three"})
print(d)
print(d.pop("one"))
