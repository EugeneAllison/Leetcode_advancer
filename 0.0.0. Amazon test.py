import math
import os
import random
import re
import sys


def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))
    return result


if __name__ == "__main__":
    n = int(input().strip())

    fizzBuzz(n)


import math
import os
import random
import re
import sys


#
# Complete the 'makePowerNonDecreasing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY power as parameter.
#


def makePowerNonDecreasing(power):
    n = len(power)
    total_increase = 0

    for i in range(1, n):
        if power[i] < power[i - 1]:
            increase = power[i - 1] - power[i]
            for j in range(i, n):
                power[j] += increase
            total_increase += increase

    return total_increase


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    power_count = int(input().strip())

    power = []

    for _ in range(power_count):
        power_item = int(input().strip())
        power.append(power_item)

    result = makePowerNonDecreasing(power)

    fptr.write(str(result) + "\n")

    fptr.close()


import collections


def processQueriesOnCart(items, query):
    queue = collections.deque()
    for item in items:
        queue.append(item)

    for q in query:
        if q > 0:
            queue.append(q)
        else:
            abs_q = abs(q)
            for _ in range(abs_q):
                queue.popleft()
        items = queue
    return list(items)


from collections import deque


def processQueriesOnCart(items, query):
    cart = deque(items)
    for q in query:
        if q > 0:
            cart.append(q)
        else:
            abs_q = abs(q)
            try:
                cart.remove(abs_q)
            except ValueError:
                pass
    return list(cart)


def makePowerNonDecreasing(power):
    n = len(power)
    total_increase = 0
    increase = []

    for i in range(1, n):
        if power[i] < power[i - 1]:
            increase.append(power[i - 1] - power[i])
            power[i] = power[i - 1]
    total_increase += increase[0]    
    for i in range(1, len(increase)):
        num = increase[i] - increase[i - 1]
        total_increase += num

    return total_increase
