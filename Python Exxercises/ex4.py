# Initialize a variable to keep track of the sum
sum = 0

# Repeat the process for 5 inputs
for i in range(5):
    # Try to get an int from the user
    try:
        num = int(input("Enter an integer: "))
        sum += num
    except ValueError:
        # If the input is not a valid int, print an error message and try again
        print("Invalid input. Please enter an integer.")
        i -= 1

# Print the resulting sum
print("The sum of the integers is:", sum)