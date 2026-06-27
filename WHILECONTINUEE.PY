Question 1: Count Valid Ages
count = 0

while True:
    age = int(input())

    if age == -1:
        break

    if age < 1 or age > 120:
        continue

    count += 1

print("Valid ages count:", count)
 OUTPUT:
25
150
40
-5
18
-1
Question 2: Sum Multiples of 5
total = 0

while True:
    num = int(input())

    if num == 0:
        break

    if num % 5 != 0:
        continue

    total += num

print("Sum:", total)
OUTPUT:
Input
10
12
15
18
20
0
Sum: 45
Question 3: Count Uppercase Letters
text = "PyTHon ProGRAM"

count = 0

for ch in text:
    if ch < 'A' or ch > 'Z':
        continue
    count += 1

print("Uppercase letters count:", count)
OUTPUT:
Uppercase letters count: 8
Question 4: Total Sales Amount
sales = [500, 0, 1200, 0, 700]

total = 0

for amount in sales:
    if amount == 0:
        continue
    total += amount

print("Total sales amount:", total)
OUTPUT:
Total sales amount: 2400
