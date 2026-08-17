sample = "Python Programming is fun!"

print(f"\nOriginal String\t\t: ",sample)
print("First 6 character \t: ",sample[0:6])
print("Slice after index 7\t:",sample[7:])


name = "joshi"
marks = 98.552

F_string = f"Hello {name}, my marks is {marks:.2f}%."
print("F-string\t:",F_string)

Format = "Hello {}, my marks is {:.2f}%.".format(name,marks)
print(".format\t\t:",Format)

legacy = "Hello %s, my marks is %.2f%%."% (name,marks)
print("% Operator\t:",legacy)

text = "ArTifIcial IntElliGenCe"

print("\nText change to lower\t: ",text.lower())
print("Text change to upper\t: ",text.upper())
print("Check length of the text: ",len(text))
print("Replace new with text\t: ",text.replace("ArTifIcial","O"))
print("Capitalized\t\t: ",text.capitalize())
print("Title case\t\t: ",text.title())
print("Strip whitespace\t: "," Python   ".strip())
print("Find the position of 'i': ",text.find("i"))
print("Count of the 'i'\t: ",text.count("i"))
print("Split the string\t:",text.split(" "))
