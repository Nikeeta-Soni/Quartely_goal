# Initializing list
element_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 20 exists in the list")
 
# number of times element exists in list
exist_count = element_list.count(20)
 
# checking if it is more than 0
if exist_count > 0:
    print("Yes, 20 exists in the list")
else:
    print("No, 20 does not exists in the list")