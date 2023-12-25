class Error(Exception):
    """Base class for other exceptions"""
    pass
 
class zerodivision(Error):
    """Raised when the input value is zero"""
    pass
 
try:
    i_num = int(input("Enter a number: "))
    if i_num == 0:
        raise zerodivision
except zerodivision:
    print("Input value is zero, try again!")
    print()