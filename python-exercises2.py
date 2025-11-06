"""
Aufgabe 3b:
Erweitere jetzt das Programm und frage nach der Temperatur in 2 Städten.
1. Frage den Benutzer nach den Namen von zwei Städten und den aktuellen Temperaturen in Fahrenheit.
2. Wandel die Temperaturen in Celsius um.
3. Wenn die Temperatur in beiden Städten unter dem Gefrierpunkt (32 °F) liegt, drucke eine Warnmeldung aus: 
"Warnung: Die Temperaturen in beiden Städten liegen unter dem Gefrierpunkt." 
Andernfalls, wenn die Temperatur nur in einer der Städte unter dem Gefrierpunkt liegt, drucke eine Warnmeldung aus: 
"Warnung: Die Temperatur in einer der Städte liegt unter dem Gefrierpunkt." 
Andernfalls drucke eine Nachricht aus: "Die Temperaturen in beiden Städten liegen über dem Gefrierpunkt."
4. Schließlich drucke die Temperaturen in Celsius aus (max. 1 Dezimalstelle).



"""

Stadt1 = input("Bitte geben Sie den Namen der ersten Stadt ein: ")
Stadt2 = input("Bitte geben Sie den Namen der zweiten Stadt ein: ")

F1 = float(input(f"Geben Sie die aktuelle Temperatur in Fahrenheit in {Stadt1} ein:"))
F2 = float(input(f"Geben Sie die aktuelle Temperatur in Fahrenheit in {Stadt2} ein:"))

C1 = (float(F1) - 32 ) * 5/9    # Die Temperatur in Celsius umwandeln
C2 = (float(F2) - 32 ) * 5/9 

if F1 < 32 and F2 < 32:
    print("Warnung: Die Temperaturen in beiden Städten liegen unter dem Gefrierpunkt.")
elif F1 < 32 or F2 < 32:
    print("Warnung: Die Temperatur in einer der Städte liegt unter dem Gefrierpunkt.")
else:
    print("Die Temperaturen in beiden Städten liegen über dem Gefrierpunkt.")

print(f"Die aktuelle Temperatur in {Stadt1} beträgt: {C1:.1f} Grad Celsius.")
print(f"Die aktuelle Temperatur in {Stadt2} beträgt: {C2:.1f} Grad Celsius.")



