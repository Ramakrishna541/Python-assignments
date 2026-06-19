print("Please enter a positive integer:")
user_input = input()

while user_input.isdigit() == False or user_input == "0":
    print("Error: That is not a positive integer. Please try again:")
    user_input = input()

number = int(user_input)

current_number = 1
total_sum = 0

while current_number <= number:
    total_sum = total_sum + current_number
    current_number = current_number + 1

print("The sum of all numbers from 1 up to your number is:")
print(total_sum)

OUTPUT :-
Please enter a positive integer:
-5
Error: That is not a positive integer. Please try again:
abc
Error: That is not a positive integer. Please try again:
0
Error: That is not a positive integer. Please try again:
5
The sum of all numbers from 1 up to your number is:
15
