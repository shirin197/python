filename = input("Input the Filename: ")
# The split() method splits a string into a list
f_extns = filename.split(".") 
# The repr() function returns a printable string of the given object
print ("The extension of the file is : " + repr(f_extns[-1]))