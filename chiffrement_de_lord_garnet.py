#coding: utf-8

def get_first_list (key) :
    key = key.upper()
    line = []
    for letter in key :
        if letter not in line :
            line.append(letter.upper())
    
    for i in range (26) :
        if i == 9 : # retire la lettre J
            pass
        elif chr(i+ord('A')) not in line:
            line.append(chr(i+ord('A')))
            
    return line

def get_second_list (first_line) :
    line = first_line.copy()
    line.reverse()
    return line

def chiffrement(message , key) :
    message_chiffre = ""
    message = message.upper()
    first_line = get_first_list(key)
    second_line = get_second_list(first_line)
    
    for lettre in message :
        if lettre.isalpha() :
            message_chiffre += second_line[first_line.index(lettre)]
        else :
            message_chiffre += lettre
            
    return message_chiffre
    
def dechiffrement (message , key) :
    message_dechiffre = ""
    message = message.upper()
    first_line = get_first_list(key)
    second_line = get_second_list(first_line)
    for lettre in message :
        if lettre.isalpha() :
            message_dechiffre += first_line[second_line.index(lettre)]
        else :
            message_dechiffre += lettre
            
    return message_dechiffre

message = "HQWWNQ ZQ UQBU"
key = 'dolait'

print(chiffrement(message , key))
print(dechiffrement(message , key))