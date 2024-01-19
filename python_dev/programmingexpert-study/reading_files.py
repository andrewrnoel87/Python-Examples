text = ""

with open("file.txt", "r") as file:
    text = file.read()

escape_characters_removed = text.replace("\n", " ").replace("\t", " ")
punctuation_removed = escape_characters_removed.replace(
    ",", "").replace("-", "").replace(".", "")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)