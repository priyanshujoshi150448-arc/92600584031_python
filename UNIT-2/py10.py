

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

numbers = generate_numbers(5)

print("Sequence of numbers:")
for number in numbers:
    print(number)
