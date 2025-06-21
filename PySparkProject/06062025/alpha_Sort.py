### Python program to sort words based on alphabetical order
sentence = input("Enter any sentence:")              # My name is satish, I am software employee
words = [item.upper() for item in sentence.split()]
print("BEFORE SORT:",words)
words.sort()
print("AFTER SORT:",words)
