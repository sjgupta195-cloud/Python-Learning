# easy way to create a list

nums = [x for x in range(5)] 
print(nums)

square = [x*x for x in range(4)]
print(square)

evens = [x for x in range(10)  if x%2 ==0]
print(evens)

words = ["python", "sql"]
upper_words = [words.upper() for words in words  ]
print (upper_words)