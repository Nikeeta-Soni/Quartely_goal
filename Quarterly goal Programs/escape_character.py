# Python code to demonstrate printing 
# escape characters from "r" or "R"
 
# initializing target string 
ch = "I\nLike\tTesting"
 
print ("The string without r / R is : ")
print (ch)
 
print ("\r")
 
# using "r" to prevent resolution
ch1 = r"I\nLike\tTesting"
 
print ("The string after using r is : ")
print (ch1)
 
print ("\r")
 
# using "R" to prevent resolution
ch2 = R"I\nLike\tTesting"
 
print ("The string after using R is : ")
print (ch2)