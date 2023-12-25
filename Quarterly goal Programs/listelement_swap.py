def swapPositions(list, ele1, ele2):
     
    list[ele1], list[ele2] = list[ele2], list[ele1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
ele1, ele2  = 1, 3
 
print(swapPositions(List, ele1-1, ele2-1))