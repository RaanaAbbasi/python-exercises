
# Passwortgenerator Programm von Raana Abbasi
# Dieses Programm generiert ein zufälliges Passwort basierend auf den Benutzereingaben.
# Der Benutzer kann die Länge des Passworts und die Arten von Zeichen auswählen, die enthalten sein sollen.
# Das Programm stellt sicher, dass die Eingaben gültig sind und gibt das generierte Passwort aus.

import random

def generiere_passwort(länge, klein, groß, zahl, symbole):
    zeichen = ""
    if klein:
        zeichen += "abcdefghijklmnopqrstuvwxyz"
    if groß:
        zeichen += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if zahl:
        zeichen += "0123456789"
    if symbole:
        zeichen += "!@#$%^&*()_-+=<>?/{}~|"

    if zeichen == "":
      return "Fehler: Es wurden keine Zeichen ausgewählt!"
    #passwort erzeugen
    passwort = "".join(random.choice(zeichen) for _ in range(länge))
    return passwort

#Eingabe des Benutzers
## Wenn die Eingabe ungültig ist, wird die Schleife wiederholt.(Länge mit Fehlerabfang)
while True:   
    benutzer_input = input("Geben Sie die gewünschte Passwörtlänge ein: ")
    try:                       #Versuch, die Eingabe in eine Ganzzahl umzuwandeln
         länge = int(benutzer_input)
         if länge <= 0:
              print("Fehler: Die Länge muss eine positive Zahl sein!")
              continue         #Wenn die Eingabe gültig ist, wird die Schleife beendet
         break                 #Schleife beenden
    except ValueError:         #Wenn die Eingabe ungültig ist, wird eine Fehlermeldung ausgegeben
        print("Fehler: Ungültige Eingabe! Bitte gib nur Zahlen ein.")       

# Eingaben für Zeichentypen (j/n)
##wir vergleichen die Eingabe mit 'j' (ja) und speichern das Ergebnis als Boolean
klein = input("Kleine Buchstaben? (j/n): ").lower() == 'j'
groß = input("Große Buchstaben? (j/n): ").lower() == 'j'
zahl = input("Zahlen? (j/n): ").lower() == 'j'
symbole = input("Sonderzeichen? (j/n): ").lower() == 'j' 

# Wir rufen die Funktion auf und generieren das Passwort an.
passwort = generiere_passwort(länge, klein, groß, zahl, symbole)
print("Dein zufälliges Passwort lautet:", passwort)
print("\nViel Spaß beim Verwenden deines neuen Passworts!\nAbschlussprojekt_FITA_Herbst 2025\nAutor: Raana Abbasi")
print("Vielen Dank an Redi School, alle Lehrerinnen, Lehrer und Mentoren für ihre Unterstützung!\U0001F60A \u2764")

##Beispielausgaben:
#1.
#Geben Sie die gewünschte Passwörtlänge ein: abc
#Fehler: Ungültige Eingabe! Bitte gib nur Zahlen ein.
#Geben Sie die gewünschte Passwörtlänge ein: 8
#Kleine Buchstaben? (j/n): J
#Große Buchstaben? (j/n): J
#Zahlen? (j/n): n
#Sonderzeichen? (j/n): n
#Dein zufälliges Passwort lautet: GUPkwrQp

#2.
#Geben Sie die gewünschte Passwörtlänge ein: 12
#Kleine Buchstaben ? (j/n): j
#Große Buchstaben ? (j/n): j
#Zahlen ? (j/n): j
#Sonderzeichen ? (j/n): j
#Dein zufälliges Passwort lautet: 89Vv7!<&%9*us

#3.
#Geben Sie die gewünschte Passwörtlänge ein: 6
#Kleine Buchstaben? (j/n): n
#Große Buchstaben? (j/n): n
#Zahlen? (j/n): n
#Sonderzeichen? (j/n): n
#Dein zufälliges Passwort lautet: Fehler: Es wurden keine Zeichen ausgewählt!

#4.
#Geben Sie die gewünschte Passwörtlänge ein: -2
#Fehler: Die Länge muss eine positive Zahl sein!
#Geben Sie die gewünschte Passwörtlänge ein:

#5.
#Kleine Buchstaben ? (j/n): j
#Große Buchstaben ? (j/n): j
#Zahlen ? (j/n): j
#Sonderzeichen ? (j/n): n
#Dein zufälliges Passwort lautet: isJF0GJh

#Viel Spaß beim Verwenden deines neuen Passworts
#Abschlussprojekt_FITA_Herbst 2025
#Autor: Raana Abbasi
#Vielen Dank an Redi School, alle Lehrerinnen, Lehrer und Mentoren für ihre Unterstützung!😊 ❤


