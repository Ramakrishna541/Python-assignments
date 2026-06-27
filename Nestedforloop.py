Question 1: Student Marks Total

n=int(input("Enter noof students : "))
for i in range(0,n):
     totalmarks=0
     for j in range(3):
        marks=int(input())
        totalmarks+=marks
     print(f'The total marks of student {i+1} : {totalmarks}')
OUTPUT:
Enter noof students : 2
50
45
50
The total marks of student 1 : 145
89
45
65
The total marks of student 2 : 199
Question 2: Shop Sales Report
for i in range(4):   # 4 products
    total_sales = 0

    print(f"Enter sales for Product {i+1}: ")

    for j in range(7):   # 7 days
        sales = int(input())
        total_sales += sales

    print(f"Product {i+1} Total Sales = {total_sales}")
OUTPUT:
Enter sales for Product 1: 
120
450
120
320
450
895
369
Product 1 Total Sales = 2724
Enter sales for Product 2: 
780
501
410
203
896
410
213
Product 2 Total Sales = 3413
Question 3: Find Highest Mark in Each Student Record
for i in range(4):   # 4 students
    print(f"Enter marks for Student {i+1}: ")

    highest = 0  # stores maximum mark for each student

    for j in range(5):  # 5 subjects
        marks = int(input())

        if marks > highest:
            highest = marks

    print(f"Highest Mark = {highest}")
OUTPUT:
Enter marks for Student 1: 
45
56
86
96
98 
Highest Mark = 98
Enter marks for Student 2: 
13
45
86
89
97
Highest Mark = 97
Enter marks for Student 3: 
45
12
36
87
95
Highest Mark = 95
Enter marks for Student 4: 
45
56
12
45
56
Highest Mark = 56
Question 4: Theatre Seat Booking Status
for i in range(5):   # 5 rows
    booked = 0

    print(f"Enter seat status for Row {i+1} (6 seats): ")

    for j in range(6):   # 6 seats in each row
        seat = int(input())

        if seat == 1:
            booked += 1

    print(f"Row {i+1} Booked Seats = {booked}")for i in range(5):   # 5 rows
    booked = 0

    print(f"Enter seat status for Row {i+1} (6 seats): ")

    for j in range(6):   # 6 seats in each row
        seat = int(input())

        if seat == 1:
            booked += 1

    print(f"Row {i+1} Booked Seats = {booked}")
OUTPUT:
Enter seat status for Row 1 (6 seats): 
1
1
0
1
1
1
Row 1 Booked Seats = 5
Enter seat status for Row 2 (6 seats): 
0
0
0
1 
0
0
Row 2 Booked Seats = 1
Enter seat status for Row 3 (6 seats): 
0
1
0
1
0
1
Row 3 Booked Seats = 3
Enter seat status for Row 4 (6 seats): 
0
10
0
0
0
0
Row 4 Booked Seats = 0
Enter seat status for Row 5 (6 seats): 
0      
1
1
1
1
1
Row 5 Booked Seats = 5
