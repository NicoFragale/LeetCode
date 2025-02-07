'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
'''

def decodeMessage(key, message):

    #aggiusto la chiave
    stringa = key.replace(" ", "")
    s = ''
    for lettera in stringa: 
        if lettera not in s: 
            s += lettera
    print(s)

    #assegno 
    valori = "abcdefghijklmnopqrstuvwxyz"
    dizionario = dict()
    for i,c in enumerate(s):
        dizionario[c] = valori[i%26]
    print(dizionario)
    
    #cifratura
    output = ""
    for lettera in message:
        if lettera == " ":
            output += " "
        else:
            output += dizionario[lettera]

    return output

print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))