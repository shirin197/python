values = input("Input some comma seprated numbers : ")
# The split() method splits a string into a list
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)