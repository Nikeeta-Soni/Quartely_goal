letter_frequencies = {}

# Get the input string from the user
user_input = input("Enter a string: ")

# Iterate through each character in the input string
for char in user_input:
    # Get the ASCII value of the character
    ascii_value = ord(char)

    # Check if the ASCII value corresponds to a letter (A-Z or a-z)
    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
        # Convert the character to uppercase (to count both upper and lower case together)
        char = char.upper()

        # Increment the frequency of the letter in the dictionary
        letter_frequencies[char] = letter_frequencies.get(char, 0) + 1

# Print the letter frequencies
print("Letter frequencies in the ASCII representation:")
for letter, frequency in letter_frequencies.items():
    print(f"{letter}: {frequency}")