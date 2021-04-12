"""
@Nadina Shirin Amsler (shirin197)
@2021-05-03
"""

# Hello World
print("Hello world")
print("\n") # line break

# ---------------------------------------------------------------------------------------------------------------------

print("Drawing a triangle")
# Drawing a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

print("\n")

# ---------------------------------------------------------------------------------------------------------------------

print("Variable")
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

# ---------------------------------------------------------------------------------------------------------------------

print("String")
#string
print("formula1")
#or
word = "formula1"
print(word)
print(word + " is a nice Sport") #i can add another String

print("\n")

# ---------------------------------------------------------------------------------------------------------------------

print("Function")
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

# ---------------------------------------------------------------------------------------------------------------------

print("Numbers")
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
my_num= -5
print(abs(my_num))
print(pow(5, 6)) # calculat for example 5 hoch (^) 6/ 6 tmes 5 (5x5x5x5x5x5)
print(max(45, 23)) # max tells us which number is higher
print(min(45, 23)) # min tells us which number is lower
print(round(3.5)) # round our number down or up to a "normal" number

print("\n")

# ---------------------------------------------------------------------------------------------------------------------

print("functions with imports")
# functions with imports
# for math functions import -> from math import *

from math import *
print(floor(3.8)) # floor grab the lowest number, so basically its chop of the decimal point (3)
print(ceil(3.8)) # floor grab the higher number, so basically its the opposite from floor   (4)
print(sqrt(49)) # sqrt print out the square root of a number


print("\n")

# ---------------------------------------------------------------------------------------------------------------------

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
# ---------------------------------------------------------------------------------------------------------------------





