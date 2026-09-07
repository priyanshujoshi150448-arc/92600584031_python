
squares = [x * x for x in range(1, 6)]
print("List comprehension:", squares)


squares_dict = {x: x * x for x in range(1, 6)}
print("Dictionary comprehension:", squares_dict)

squares_set = {x * x for x in range(1, 6)}
print("Set comprehension:", squares_set)
