name = "Alice"
print(name[0])  # print the first character of the string, output will be "A"

print (len(name))  # print the length of the string, output will be 5

print (name.upper())  # print the string in uppercase, output will be "ALICE"

print (name.lower())  # print the string in lowercase, output will be "alice"

print (name*3)  # print the string repeated 3 times, output will be "AliceAliceAlice"

text = "I love Python programming"
words = text.split()  # split the string into a list of words
print(words)  # output will be ['I', 'love', 'Python', 'programming']

texts = " ".join(words)  # join the list of words back into a string
print(texts)  # output will be "I love Python programming"

phrase = "I love java programming"
statement = phrase.replace("java", "python")  # replace "java" with "python" in the string
print(statement)  # output will be "I love python programming"

city = "     delhi     "
print(city.strip())  # output will be "delhi"