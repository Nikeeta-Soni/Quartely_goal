import re 
  
regex = re.compile(r'([\d]{2})-([\d]{2})-([\d]{4})') 
  
# search method 
print('compiled reg expr', regex.search('16-10-2023')) 
  
# sub method 
print(regex.sub(r'\1.\2.\3', '16-10-2023')) 