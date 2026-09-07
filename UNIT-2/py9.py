
# List is an iterable
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
for number in numbers:
    print(number)

# Creating an iterator from the list
iterator = iter(numbers)

print("\nIterator:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
