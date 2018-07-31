import random

if __name__ == '__main__':
    a = list()
    b = list()
    for i in range(10, random.randint(10, 100)):
        a.append(random.randint(1, 100))
    for i in range(10, random.randint(10, 100)):
        b.append(random.randint(50, 150))
    print(set(a + b))
