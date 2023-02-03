def unique_list(lst):
    # Use the set built-in function to remove duplicates from the list
    # Since sets only allow unique elements, calling set on the input list
    # will eliminate any duplicates
    unique_elements = set(lst)
    
    # Convert the set back to a list using the list built-in function and return it
    return list(unique_elements)

# Test the function with a sample list
test_list = [1, 2, 3, 2, 1, 4]
print(unique_list(test_list))