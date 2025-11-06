##Übung 1: Einfache Vergleiche
"""
num1 = int(input("bitte geben sie num1 ein:"))
num2 = int(input("bitte geben sie num2 ein:"))
if num1 > num2 :
   print ("num1 ist größer als num2.")
"""

##Übung 2: Stringvergleich:
"""
person_name = input("bitte geben Sie Ihren Name ein:")
if len(person_name) >= 6 :
  print(f"{person_name} ist länger Name!")
"""

##Wenn Sonst (if else)-Anweisungen
"""
print("Gib ein Zahl ein:")
a = int(input())
if a>0 :
   print (" a ist ein positive Zahl.")
else :
   print(" a ist negative Zahl.")
"""


##Übung 3: Gerade oder Ungerade
"""
num = int(input())
print("Gib eine ganze Zahl:")
if num % 2 == 0:
    print("num ist Gerade.")
else :
    print("num ist Ungerade.")  
"""

##Übung 4: Passwortprüfung
"""
passwort = "python123"
user_input = input("Gib Passwort ein:")

if user_input == passwort:
    print("Zugang Gewährt")
else :
    print("Zugang Verweigert")   
"""


##Wenn Sonst-wenn Sonst (if elif else)-Anweisungen
"""
print("Geben Sie eine Zahl ein:")
a = int(input())
if a>0:
    print(" a ist eine positive Zahl.")
elif a==0:
    print("a ist gleich 0 .")
else :
    print("a ist eine negative Zahl!")  
"""


##Übung 5: Notenklassifikation 
"""
Übung 5: NotenklassifikationFrage den Benutzer, eine numerische Note (0 bis 100) über input() einzugeben.
Konvertiere die Eingabe in eine Ganzzahl und klassifizieren Sie die Note wie folgt:
90 oder höher: "A"
80 bis 89: "B"
70 bis 79: "C"
60 bis 69: "D"
Unter 60: "F"
Drucke die Notenklassifikation aus.

print("Geben Sie eine numerische Note (0 bis 100) ein:")
a = int(input())
if a>=90:
    print("klassifizieren ist A")
elif a>=80:
    print("klassifizieren ist B")
elif a>=70:
    print("klassifizieren ist C")
elif a>=60:
    print("klassifizieren ist D")
else:
    print("klassifizieren ist F")
"""


##Übung 6: Ticketpreis
"""
Frage den Benutzer, sein Alter über input() einzugeben.
Konvertiere die Eingabe in eine Ganzzahl und bestimmen Sie den Ticketpreis basierend auf dem Alter:
0 bis 3 Jahre: Kostenlos
4 bis 12 Jahre: $10
13 bis 64 Jahre: $15
65 und älter: $5
Drucke den Ticketpreis aus.


alter = int(input("Sagen Sie bitte Ihr Alter:"))

if alter>=65:
    print("Ticketpreis ist 5$")
elif alter>=13:
    print("Ticketpreis ist 15$")
elif alter>=4:
    print("Ticketpreis ist 10$")
else:
    print("Ticketpreis ist kostenlos!")  

"""

##Übung 7:
"""
Verbessern Sie den folgenden Code, sodass, wenn ein Benutzer etwas anderes als Kaffee oder Tee möchte, Sie den Benutzer darauf hinweisen,
dass das benötigte Getränk nicht verfügbar ist:

print("Die Maschine wird eingeschaltet...")
getränk = input("Möchten Sie Tee oder Kaffee? ")
wenn getränk == "tee":
print("Tee wird zubereitet...")
elif getränk == "kaffee":
print("Kaffee wird zubereitet...")
print("Die Maschine wird ausgeschaltet.")

print("Die Kaffeemaschine wird eingeschaltet... ")
getränk = str(input("Möchten Sie Tee oder Kaffee? "))

if getränk == "Tee" or getränk == "tee":
    print("Tee wird zubereitet...")
elif getränk == "Kaffee" or getränk == "kaffee" :
    print("Kaffee wird zubereitet...")
else:
    print("Es tut mir leid, aber Getränk ist nicht verfügbar! \n Die Kaffeemaschine wird ausgeschaltet...")
"""  


##Übung 8: Logische Kombinationen
"""
Fragen Sie den Benutzer, eine Ganzzahl über input() einzugeben.
Konvertieren Sie die Eingabe in eine Ganzzahl und überprüfen Sie, ob sie zwischen 10 und 50 (einschließlich) oder weniger als 0 liegt.
Drucken Sie das Ergebnis der Bedingung aus.

Zahl = int(input("Geben Sie eine Ganzzahl ein:"))

if (Zahl >= 10 and Zahl <= 50)or Zahl <0:
    print("Das Ergebnis ist Wahr!")
else:
    print("Das Ergebnis ist Falsch!")    
"""


##Verschachtelte Wenn (if)-Anweisungen
"""
a = int(input())
if a>0 and a<5:
    if a==3:
        print("a ist gleich 3")
    else:
        print("a liegt zwischen 0 und 5")
elif a==0:
    print("a ist gleich 0") 
else:
    print("a ist eine negative Zahl") 
""" 


# Übung 9: Verschachtelte if-Anweisungen
"""
Bitten Sie den Benutzer, drei Ganzzahlen mit input() einzugeben und geben Sie das Minimum der drei Zahlen mit einer ordentlichen Print-Anweisung zurück.

a = int(input("Geben Sie erste Nummer:"))
b = int(input("Geben Sie zweite Nummer:"))
c = int(input("Geben Sie dritte Nummer:"))

if a < b and a < c:
    if b < c :
        print("a ist Minimum")
    elif c < a:
        print("c ist Minimum")
    else:
        print("b ist Minimum") 
elif b < a and b < c:           
            print("b ist Minimum")
else:
      print("c ist Minimum")
"""                  