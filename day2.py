import math
n = 30
nums = list(range(2, n + 1))


nums2 = []
sqrt = int(math.sqrt(n))

for i in range(2, sqrt+1):
    for x in nums:
        if x != i and x % i == 0:
            if x not in nums2:
                nums2.append(x)

nums3 = [x for x in nums if x not in nums2]
print(nums3)

nums = [4, 7 ,5]
sum1 = 0
x = 0
for i in nums:
    sum1 += i
print(sum1)
while 2**x < sum1:
    x += 1
print(x)


def hello(name):
    print("Hello, " + name + "!")

hello1 = hello('Alice')


def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

def numbers(*args):
    return sum(args)

print(numbers(1, 2, 3, 4, 5))  # Output: 15


def key_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


key_arguments(name="Alice", age=30, city="New York")

lam = lambda x: x * x
print(lam(5))  # Output: 25