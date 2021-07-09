def sum(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(sum((8, 2, 3, -1, 7)))