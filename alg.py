# Initialize counters
length = 0
words = 0
vowels = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Input the sentence
sentence = input("Enter a sentence ending with a period: ")

# Ensure the sentence ends with a period
if not sentence.endswith('.'):
    print("The sentence must end with a period.")
else:
    # Iterate through each character
    for char in sentence:
        length += 1  # Count each character
        if char in vowel_set:  # Check if the character is a vowel
            vowels += 1
        if char == ' ':  # Check for spaces to count words
            words += 1

    # Account for the last word (if sentence isn't just a period)
    if length > 1:
        words += 1

    # Output the results
    print("Length of the sentence:", length)
    print("Number of words:", words)
    print("Number of vowels:", vowels)
 
