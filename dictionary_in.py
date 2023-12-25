test_dict = {"Annapurna": 22, "Nikeeta": 25, "Megha": 21, "Pooja": 26}
print(test_dict)
 
# empty the dictionary d
y = {}
# eliminate the unrequired element
for key, value in test_dict.items():
    if key != 'Annapurna':
        y[key] = value
print(y)