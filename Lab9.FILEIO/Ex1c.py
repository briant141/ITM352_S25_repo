with open('names.txt', 'r') as file_obj:
    names = file_obj.read()
print(names)
# without the .split("\n") we will just get the letters for each character, and not counting the names
print(f'There are {len(names.split("\n"))} names')