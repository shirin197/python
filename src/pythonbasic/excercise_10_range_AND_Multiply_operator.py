k = 1
for i in range(1, 2): # i = 1, range ausgabe = 1
    for j in range(1, 3):
        k *= j + i

print("--- Rechnung ---")
print(k)

"""
1. Durchgang der for schleige range j
    Rechnung: k = k * j + i
    1. k *= 1 + 1 / k = 2
       k = 2 -> k wird neu abgespeichert

2. Durchgang der for schleife range j
    Rechnung: k *= 2 + 1 
    k *= 3 , weil (k = 2 -> 2 * 3 = 6)
"""

print("--- Durchgang zwei Darstellung ---")
k = 2
k *= 3
print(k)
