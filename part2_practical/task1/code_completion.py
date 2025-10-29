students = [
    {"name": "Alice", "age": 30},
    {"name": "Bob",   "age": 25},
    {"name": "Cara",  "age": 27}
]
# Manual function implementation
def sort_dict(key_name, list_name): 
    key_values = []

   # Get the key item and the index of the list item
    for index,item in enumerate(list_name):
        # Store a tuple of the key value and the index of the dictionary
        key_values.append((item[key_name], index))
    
    # Sort the key values 
    key_values.sort(key=lambda x: x[0])

    # Rebuild the list
    sorted_dicts = [list_name[i] for _, i in key_values]

    return sorted_dicts

print("Running...")
print(sort_dict("age", students))

# AI implementation
# Write a function that sorts a list of dictionaries by a specified key 
def sort_dict_ai(key_name, list_name):
    return sorted(list_name, key=lambda x: x[key_name])

print("Running AI...")
print(sort_dict_ai("age", students))