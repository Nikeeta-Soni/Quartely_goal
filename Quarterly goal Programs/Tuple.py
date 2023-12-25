Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("QA", "Rohit", "QA2", "Aditya", "QA3", "Rahul")
Tuple3 = ((1, "Pooja"), ( 2, "Megha"), (3, "Anu"), (4, "Ruchita"))
 
# print the sizes of sample Tuples
print("Size of Tuple1: " + str(Tuple1.__sizeof__()) + "bytes")
print("Size of Tuple2: " + str(Tuple2.__sizeof__()) + "bytes")
print("Size of Tuple3: " + str(Tuple3.__sizeof__()) + "bytes")