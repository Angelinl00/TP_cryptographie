#coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel , QVBoxLayout , QWidget , QLineEdit

def main () :
    app = QApplication(sys.argv)
    
    window = QMainWindow()
    window.setWindowTitle('codage de cesar')
    window.setGeometry(100 , 100 , 600 , 100)
    window.setFixedSize(600 , 100)
    
    container = QWidget(window)
    container.setStyleSheet("padding: 20px;")
    
    layout = QVBoxLayout(container)
    
    label = QLabel("Entrez le message à crypter")
    label.setStyleSheet("font-size: 22px; color: #000;")
    label.setWordWrap(True)
    
    message = QLineEdit()
    
    layout.addStretch()
    layout.setStyleSheet("background-color: #242938;")
    container.setStyleSheet("""
        QVBoxLayout {
            display : flex;
            flex-shrink : 0 ;
            justify-content : center;
            align-items : center;
            flex-direction : column;
        }    
    """)
    
    layout.addWidget(label)
    layout.addWidget(message)
    window.setCentralWidget(container)
    
    window.show()
    sys.exit(app.exec_()) # Main loop
    
def chiffrement(message, decalage):
    message_chiffre = ''
    decalage = parse(decalage)
    for lettre in message:
        if lettre.isalpha():
            decalage %= 26  # Assure un décalage dans l'intervalle [0, 25]
            if lettre.islower():
                ascii_debut = ord('a')
            else:
                ascii_debut = ord('A')
            lettre_chiffree = chr((ord(lettre) - ascii_debut + decalage) % 26 + ascii_debut)
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

def parse(decalage):
    if isinstance(decalage, str) and decalage.isalpha():  # Vérifie si le décalage est une lettre
        decalage = ord(decalage.lower()) - ord('a')  # Obtient la valeur numérique du décalage
        return decalage
    else:
        try:
            decalage = int(decalage)  # Tente de convertir en nombre entier
            return decalage
        except ValueError:
            print("Le décalage doit être une lettre ou un nombre entier.")
            return message_chiffre  # Retourne le message chiffré si le décalage n'est ni une lettre ni un nombre

def dechiffrement(message_chiffre, decalage):
    decalage = parse(decalage)
    return chiffrement(message_chiffre, -decalage)  # Utilise 26 - decalage pour inverser le décalage

message_original = "Bonjour, ceci est un exemple de message à chiffrer !"
decalage = 'C'  # Décalage en tant que caractère ou nombre

message_chiffre = chiffrement(message_original, decalage)
print("Message chiffré:", message_chiffre)

message_dechiffre = dechiffrement(message_chiffre, decalage)
print("Message déchiffré:", message_dechiffre)

if __name__ == '__main__' :
    main()