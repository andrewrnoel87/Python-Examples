#def caesar_cipher(string, offset):
string = "apple"
string_list = [i for i in string]
offset = 5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = [i for i in alphabet]

for i in range(len(shifted_alphabet)):
    shifted_alphabet[i] = alphabet[i - offset]

for i in range(len(string_list)):
    char = string_list[i]
    target_char = shifted_alphabet[alphabet.index(char)]
    string_list[i] = target_char

coded_string = ""

for elem in string_list:
    coded_string += elem
    
print(coded_string)





# slst = [[i, j] for i in 'abcdefghijklmnopqrstuvwxyz']


#print(slst)