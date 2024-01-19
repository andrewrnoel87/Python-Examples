def get_n_longest_unique_words(words, n):

    frequency_dict = {}
    list_of_unique_words = []

    for word in words:  # make a dictionary that tracks the frequency of each word.
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    for key in frequency_dict:  # make a list of words with frequency 1.
        if frequency_dict.get(key) == 1:
            list_of_unique_words.append(key)

    list_of_unique_words.sort(key=len, reverse=True)  # sort the list by word length in descending order.

    n_words = list_of_unique_words[0:n]  # return a list of the first n words.
    return n_words




