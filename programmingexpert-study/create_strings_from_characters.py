frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}

string1 = "hello"

string2 = "world"

# the_plan
# build dictionary out of strings and compare to provided frequencies
def create_strings_from_characters(frequencies, string1, string2):

    frequencies_contains_string1 = False  #set default values
    frequencies_contains_string2 = False
    frequencies_contains_string1_and_string2 = False

    string1_dict = string_to_dict(string1)  #create dictionaries for comparing frequencies
    string2_dict = string_to_dict(string2)
    string1_and_string2_dict = string_to_dict(string1 + string2) 

    frequencies_contains_string1 = compare_char_frequencies(frequencies, string1_dict)  #compare the frequencies
    frequencies_contains_string2 = compare_char_frequencies(frequencies, string2_dict)
    frequencies_contains_string1_and_string2 = compare_char_frequencies(frequencies, string1_and_string2_dict)

    if frequencies_contains_string1_and_string2:  # return a value based on the relationship between the strings and the original provided dictionary
        return 2
    
    elif frequencies_contains_string1 or frequencies_contains_string2:
        return 1
    
    else:
        return 0

def string_to_dict(string):  # takes in a string and returns a dict with {'char': frequency} values made from the string
    string_dict = {}
    for i in string:
        string_dict[i] = string_dict.get(i, 0) + 1
    return string_dict

def compare_char_frequencies(dict1, dict2):  #  returns True if the char frequencies in dict1 >= frequencies in dict2


print(create_strings_from_characters(frequencies, string1, string2))
#print(string_to_dict(string1))
#print(string_to_dict(string2))