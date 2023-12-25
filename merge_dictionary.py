def Merge(dict1, dict2):
    return(dict2.update(dict1))
 
dict1 = {'Jeff': 10, 'Brain': 8}
dict2 = {'Tiffeny': 6, 'Charles': 4}
 
print(Merge(dict1, dict2))
 
print(dict2)