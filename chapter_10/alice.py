filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
