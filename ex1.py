import random as rand
def randomim(a):
    for _ in range(rand.randint(1, 10)):
        a.append(rand.randint(1, 100))

def print_list(a):
    print('list = ')
    for i in range(len(a)):   
        print(f'{a[i]}, ', end="")
a = []
b = []
randomim(a)
print_list(a)
randomim(b)
print_list(b)