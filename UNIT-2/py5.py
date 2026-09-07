print("Break statement:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)
print("\nContinue statement:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nPass statement:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
