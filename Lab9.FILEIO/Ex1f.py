import os

namesfilepath = "names.txt"
if os.path.exists(namesfilepath):
    with open('names.txt', 'r') as file_obj:
        names = file_obj.readlines()
    print("".join(names)) # we can't do names.join() due the nature of lists not having the attribute of the join. We have to use strings
    print(f'There are {len(names)} names')
else:
    print(f'{namesfilepath} does not exist')