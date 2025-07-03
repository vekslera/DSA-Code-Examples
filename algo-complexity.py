import math
def is_primary(n):
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def complexity_examples():


    num = 128


    #numbers = [i for i in range(num)]


    numbers = []
    for i in range(num):
        numbers.append(i)


    print(numbers)


    #multi_table = [[(i +1) * (j + 1) for j in range(num)]
    #                                for i in range(num)]


    table = []
    for i in range(num):
        row = []
        for j in range(num):
            row.append(i * j)
        table.append(row)


    for row in table:
        print(row)


    while num > 1:
        num = num / 2


def factorial_without_recursion(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


def factorial_with_recursion(n):
    if n == 0:
        return 1
    return n * factorial_with_recursion(n - 1)





if __name__ == '__main__':
    n = 1
    #while n:
    #    n = int(input('Enter a number (0 to exit): '))
    #    print(f"{n} is a primary number: {is_primary(n)}")

    #complexity_examples()

    while n:
        n = int(input("Enter a number to calculate its factorial (0 to exit): "))
        print(f"{n}! = {factorial_without_recursion(n)} without recursion")
        print(f"{n}! = {factorial_with_recursion(n)} with recursion")