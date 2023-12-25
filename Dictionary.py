sentence = "@here, Here! Here?"  
# sentence = 6273839383 
char_count={}
if sentence==str:
   for char in sentence:
    if  char.isalpha():
        if char in char_count:
           char = char.lower()
           char_count[char]+=1
        else:
           char_count[char]=1
for key, value in char_count.items():    
  print(f"{key} {value}")