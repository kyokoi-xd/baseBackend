x = int(input('x ='))
if x > 0:
    print("+")
elif x < 0:
    print("-")
else:
    print("0")

for i in range(1, 10):
    print(i, end=' ')

i = 5
print('\n')
while i > 0:
    print(i, end=' ')
    i -= 1
print('\n')
for i in range(1, 10):
    if i == 5:
        continue
    print(i, end=' ')

nums = [10,20, 50, 150, 30]
print('\n')
for i in nums:
    if i > 100:
        break
    print(i, end=' ')    