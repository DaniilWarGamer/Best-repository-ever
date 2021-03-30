import random as rand
def randomim(a):
    for _ in range(rand.randint(1, 10)):
        a.append(rand.randint(1, 100))
def compress(a, n):
    for i in range(len(a)):
        if a[len(a)-i-1] == n:
             a.pop(len(a)-i-1)
l = []
randomim(l)
print(l)
a = int(input("Enter number to delete "))
compress(l, a)
print(l)