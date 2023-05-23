# List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.
sentence = "This is a common of an example sentence in a Python exercise"
words = sentence.split()
word_lenghts = [len(word) for word in words if word != "This"]
print(words)
print(word_lenghts)