text = "hadoop map reduce is fun map reduce is powerful"

# Split text into words
words = text.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the result
for word, count in word_count.items():
    print(word, ":", count)
