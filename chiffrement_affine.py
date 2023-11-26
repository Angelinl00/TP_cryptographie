#coding:utf-8

def chiffrement(text, a, b):
    message_chiffre = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                lettre_chiffree = (a * x + b) % 26 + ord('a')
                message_chiffre += chr(lettre_chiffree)
            elif char.isupper():
                x = ord(char) - ord('A')
                lettre_chiffree = (a * x + b) % 26 + ord('A')
                message_chiffre += chr(lettre_chiffree)
        else:
            message_chiffre += char
    return message_chiffre


def inverse_modulaire(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def dechiffrement(text, a, b):
    message_dechiffre = ""
    a_inverse = inverse_modulaire(a, 26)
    if a_inverse is not None:
        for char in text:
            if char.isalpha():
                if char.islower():
                    y = ord(char) - ord('a')
                    lettre_dechiffree = (a_inverse * (y - b)) % 26 + ord('a')
                    message_dechiffre += chr(lettre_dechiffree)
                elif char.isupper():
                    y = ord(char) - ord('A')
                    lettre_dechiffree = (a_inverse * (y - b)) % 26 + ord('A')
                    message_dechiffre += chr(lettre_dechiffree)
            else:
                message_dechiffre += char
        return message_dechiffre
    else:
        return "Inverse modulaire non trouvé."

message = "Message a chiffrer"
cle_a = 5
cle_b = 6

encrypted_message = chiffrement(message, cle_a, cle_b)
print("Message chiffré:", encrypted_message)

decrypted_message = dechiffrement( "YM QMGGKAM MGN GMYZMN", 7, 10)
print("Message déchiffré:", decrypted_message)

print(len("mon message"))