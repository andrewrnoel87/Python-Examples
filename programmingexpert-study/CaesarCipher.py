#def caesar_cipher(string, offset):
offset = 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = [i for i in alphabet]

for i in range(len(shifted_alphabet)):
    shifted_alphabet[i] = alphabet[i - offset]
    
print(shifted_alphabet)





# slst = [[i, j] for i in 'abcdefghijklmnopqrstuvwxyz']


#print(slst)