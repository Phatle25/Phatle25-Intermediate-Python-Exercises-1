def letter_count(s):
    # Create a new dictionary to store the letter count
    count = {}
    
    # Iterate over each character in the string
    for char in s:
        # Convert the character to lowercase and check if it's a letter
        char = char.lower()
        if char.isalpha():
            # If it's a letter, add it to the count dictionary or increment its value
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    
    # Return the letter count dictionary
    return count

# Get a string from the user
s = input("Enter a string: ")

# Call the letter_count function and print the result
print(letter_count(s))