def word_count(text):
    words = text.split()
    return len(words)

# Manual input from user
input_text = input("Enter a text string: ")

# Call the word_count function with the user-input text
result = word_count(input_text)

# Display the result
print(f"Number of words: {result}")