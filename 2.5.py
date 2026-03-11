# Program to read a file and count number of words

filename = input("Enter the file name: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        
        print("\nFile Contents:\n")
        print(content)

        # Count words
        words = content.split()
        word_count = len(words)

        print("\nTotal number of words in the file:", word_count)

except FileNotFoundError:
    print("File not found. Please check the file name.")
