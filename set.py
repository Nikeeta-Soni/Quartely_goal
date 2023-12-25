# Python program to demonstrate differences
# between normal and frozen set
 
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])
 
print("Normal Set")
print(normal_set)
 
# A frozen set
frozen_set = frozenset(["e", "f", "g"])
 
print("\nFrozen Set")
print(frozen_set)