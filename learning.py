"""
@Nadina Amsler (shirin197)
@2021-05-03 - still in working progess
"""
# Hello World
print("Hello world")
print("\n") # line break

# Drawing a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("\n")

# Variable
# separading word for a variable with _
# for a number i dont need "", only when i make a String

person_name = "Lynn" # string
person_age = "20"
person_country = "Italy"
is_Female = True # boolean

print("Hello there, my name is " + person_name + ", ")
print("i am " + person_age + " and from " + person_country + " ")
# its possible to change the name in the half of the story, i updated my variable inside of the programm
person_name = "Phoebe"
print("I really like my name " + person_name + ", ")
print("but i didn't like being " + person_age + ".")

print("\n")

#string
print("formula1")
#or
word = "formula1"
print(word)
print(word + " is a nice Sport") #i can add another String

print("\n")

#Functions
word = "Python"
       # 012345 -> positions in the string
# word = "Python is nice" is also a string
# list of functions -> https://www.w3schools.com/python/python_ref_functions.asp

print(word.lower()) #lower put all letters in Lower case letters
print(word.upper()) #upper put all letters in UPPER case letters
print(word.isupper()) # control (in this case) the String is entirely in Uppercase /true or false print /
print(word.upper().isupper()) # (word.upper() runs first then (put everything in uppercase then control with isupper()
print(len(word)) # print whats the lengtn of the string ( python = 6)
print(word[0]) #print(word[index of the charakter i want]) string start wth 0
print(word.index("h")) # retun us the index of our specific letter(capitol) inside of the string
print(word.index("thon")) # shows me where this starts (here 2 bc. thats where "thon" starts
print(word.replace("Python", "Java")) # replace specific words in the string

print("\n")

#Numbers
print(1)
print(1.908)
print(-2)
print(1 + 8) # all types of calculations are possible
print(5 * (3 + 6))
print(10 % 3)
my_num = 5
print(my_num)
my_num =5
print(str(my_num) + " my fav. number")
# my_num will be convertet into a string -> useful when u want to print out a number next to a string

print("\n")

# if abfrage
a = 1
if a == 1:
    print("a is true")
print("\n")

# Addition von zwei Zahlen
nummer1 = 2
nummer2 = 4

summe = nummer1 + nummer2

# Ausgabe der Variable Summe
print(summe)






