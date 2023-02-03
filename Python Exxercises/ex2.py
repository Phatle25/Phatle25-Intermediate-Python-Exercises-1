def combine_dicts(dict1, dict2):
    # Create a new dictionary to store the combined values
    combined = {}
    
    # Iterate over the keys in both dictionaries
    for key in dict1.keys():
        if key in dict2:
            # If the key is in both dictionaries, add the values
            combined[key] = dict1[key] + dict2[key]
    
    # Return the combined dictionary
    return combined

# Test the function with sample dictionaries
dict1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
dict2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
print(combine_dicts(dict1, dict2))