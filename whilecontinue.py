# Initialize the counter
num = 1

# Loop through numbers from 1 to 10
while num <= 10:

    # Stop the loop when the number reaches to 8
    if num == 8:
        print("Encountered 8.")
        break  # Exits the loop 

    # Check if the number is odd
    if num % 2 != 0:
        num += 1
        continue  # Skip the rest of  the loop and move to the next number

    # Print only even numbers
    print(num)

    # Increment the counter
    num += 1
OUTPUT:
2
4
6
Encountered 8. Stopping the loop.
