test_dict = {'month' : [7, 8, 9],
            'name' : ['July', 'August', 'Sept']}
 
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
 
# Convert key-values list to flat dictionary
x=list(test_dict.values())
a=x[0]
b=x[1]
d=dict()
for i in range(0,len(a)):
    d[a[i]]=b[i]
# printing result
print("Flattened dictionary : " + str(d))