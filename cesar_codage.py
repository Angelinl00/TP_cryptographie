#coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel , QVBoxLayout , QWidget , QLineEdit , QPushButton

def main () :
    app = QApplication(sys.argv)
    
    def on_chiffrement_button_clicked() :
        text_a_chiffrer = message.text()
        cle_ = cle.text()
        encrypted_text = chiffrement(text_a_chiffrer , cle_) # Résultat du chiffrement
        
        result = "Message chiffré : "+encrypted_text
        result = QLabel(result)
        result.setStyleSheet("""
            font-size : 15px;
            color : #a9a9a9;
        """)
        layout.addWidget(result)
    
    window = QMainWindow()
    window.setWindowTitle('codage de cesar')
    window.setStyleSheet("""
        min-width: 400px;
        background : #000;
        height : auto;
    """)
    
    container = QWidget(window)
    container.setStyleSheet("background-color: #fff; padding: 20px;")
    
    layout = QVBoxLayout(container)
    
    labelMessage = QLabel("Entrez le message à crypter")
    labelMessage.setStyleSheet("font-size: 15px; color: #fff ;font : bold")
    labelMessage.setWordWrap(True)
    
    message = QLineEdit()
    message.setStyleSheet("""
        border-radius : 5px;
        background : #232323;
        font-size : 18px;
        color : #c0c0c0;
        padding-left : 3px ;
        padding-right : 3px;
        margin-bottom : 7px;
    """)
    
    labelCle = QLabel("Entrez le décalage")
    labelCle.setStyleSheet("""
        QLabel {
            font-size: 15px;
            color: #fff ;
            font : bold;
        }
    """)
    
    cle = QLineEdit()
    cle.setStyleSheet("""
        border-radius : 5px;
        background : #232323;
        font-size : 18px;
        color : #c0c0c0;
        padding-left : 3px ;
        padding-right : 3px;
        margin-bottom : 7px;
    """)
    
    button = QPushButton("chiffrer ?")
    button.setStyleSheet("""
        margin-top : 7px;
        border-radius : 5px;
        background : #FFF;
        font-size : 18px;
        color : #000;
    """)
    
    button_dechiffrement = QPushButton("Déchiffrer ?")
    button_dechiffrement.setStyleSheet("""
        border-radius : 5px;
        background : #202020;
        border : 2px solid #fff;
        font-size : 18px;
        color : #fff;
        padding-left : 3px;
        padding-right : 3px;
        margin-top : 7px;
    """)
    
    button.clicked.connect(on_chiffrement_button_clicked)
    
    layout.addStretch()
    container.setStyleSheet("""
        QVBoxLayout {
            display : flex;
            flex-shrink : 0 ;
            flex-direction : column;
            justify-content : start ;
            align-items : start;
        }    
    """)
    
    layout.addWidget(labelMessage)
    layout.addWidget(message)
    layout.addWidget(labelCle)
    layout.addWidget(cle)
    layout.addWidget(button)
    layout.addWidget(button_dechiffrement)
    window.setCentralWidget(container)
    
    window.show()
    sys.exit(app.exec_()) # Main loop
    
def chiffrement(message, decalage):
    message_chiffre = ''
    decalage = parse(decalage)
    for lettre in message:
        if lettre.isalpha():
            decalage %= 26
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
    if isinstance(decalage, str) and decalage.isalpha():
        decalage = ord(decalage.lower()) - ord('a')
        return decalage
    else:
        try:
            decalage = int(decalage)
            return decalage
        except ValueError:
            print("Le décalage doit être une lettre ou un nombre entier.")
            return message_chiffre

def dechiffrement(message_chiffre, decalage):
    decalage = parse(decalage)
    return chiffrement(message_chiffre, -decalage)

message_original = "ce message est secret"
decalage = 'w'

message_chiffre = chiffrement(message_original, decalage)
print("Message chiffré:", message_chiffre)

message_dechiffre = dechiffrement(message_chiffre, decalage)
print("Message déchiffré:", message_dechiffre)

if __name__ == "__main__" :
    main()
    