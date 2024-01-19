def create_strings_from_characters(frequencies, string1, string2):

    frequencies_copy = frequencies.copy()  # create copy of frequencies so we do not modify it
    string1_dict = string_to_dict(string1)  # create dictionaries for comparing frequencies
    string2_dict = string_to_dict(string2)
    string1_and_string2_dict = string_to_dict(string1 + string2) 

    frequencies_contains_string1 = dict1_contains_dict2(frequencies_copy, string1_dict)  # assign bool values based on a comparison of the frequencies
    frequencies_contains_string2 = dict1_contains_dict2(frequencies_copy, string2_dict)
    frequencies_contains_string1_and_string2 = dict1_contains_dict2(frequencies_copy, string1_and_string2_dict)
    

    if frequencies_contains_string1_and_string2:  # return a value based on the relationship between the strings and the original provided dictionary
        return 2
    
    if frequencies_contains_string1 or frequencies_contains_string2:
        return 1
    
    else:
        return 0

def string_to_dict(string):  # takes in a string and returns a dict with {'char': frequency} values made from the string
    string_dict = {}
    for i in string:
        string_dict[i] = string_dict.get(i, 0) + 1
    return string_dict

def dict1_contains_dict2(dict1, dict2):  #  returns False if the char frequencies in dict1 < frequencies in dict2
    for key in dict2:
        if dict1.get(key, 0) < dict2[key]:
            return False
    return True