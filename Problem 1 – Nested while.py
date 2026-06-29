Problem 1 – Nested while
What is the problem asking?
Generate all pairs from 1–5 and print only pairs whose sum is even.
i = 1

while i <= 5:
    j = 1
    while j <= 5:
        if (i + j) % 2 == 0:
            print("(", i, ",", j, ")", sep="")
        j += 1
    i += 1
OUTPUT:
(1,1)
(1,3)
(1,5)
(2,2)
(2,4)
(3,1)
(3,3)
(3,5)
(4,2)
(4,4)
(5,1)
(5,3)
(5,5)
Problem 2 – Nested while
What is the problem asking?
Generate all pairs from 1–10 and print only pairs whose product is greater than 30. Also count total
pairs.
i = 1
count = 0

while i <= 10:
    j = 1
    while j <= 10:
        if i * j > 30:
            print("(", i, ",", j, ") ->", i * j, sep="")
            count += 1
        j += 1
    i += 1

print("Total pairs:", count)
OUTPUT:
(4,8) ->32
(4,9) ->36
(4,10) ->40
...
Total pairs: 53
Problem 3 – For inside While
What is the problem asking?
Keep asking user for numbers until 0 is entered. For each number, find factors and their sum.
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total = 0

    print("Factors:", end=" ")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            total += i

    print("\nSum:", total)

    num = int(input("\nEnter a number (0 to stop): "))
OUTPUT:
Enter a number (0 to stop): 12
Factors: 1 2 3 4 6 12
Sum: 28

Enter a number (0 to stop): 8
Factors: 1 2 4 8
Sum: 15

Enter a number (0 to stop): 0
Problem 4 – While inside For
What is the problem asking?
Given numbers=[12,7,20,9], for each number print values from 1 to that number and count evens.
numbers = [12, 7, 20, 9]

for num in numbers:
    print("Number:", num)

    i = 1
    even_count = 0

    while i <= num:
        print(i, end=" ")

        if i % 2 == 0:
            even_count += 1

        i += 1

    print("\nEven count:", even_count)
    print()
 Output:

Number: 12
1 2 3 4 5 6 7 8 9 10 11 12
Even count: 6

Number: 7
1 2 3 4 5 6 7
Even count: 3

Number: 20
1 2 3 ... 20
Even count: 10

Number: 9
1 2 3 4 5 6 7 8 9
Even count: 4
