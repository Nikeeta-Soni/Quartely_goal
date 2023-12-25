# initializing list
test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Join Tuples if similar initial element
# Using dictionary and list comprehension
temp_dict = {}
for x in test_list:
    temp_dict[x[0]] = temp_dict.get(x[0], []) + list(x[1:])
 
res = [(k,) + tuple(v) for k, v in temp_dict.items()]
 
# printing result
print("The extracted elements are: " + str(res))