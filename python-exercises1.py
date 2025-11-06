"""
Aufgabe 3a
Erweitere das Programm von letzter Woche, um die Temperatur von Fahrenheit in Celsius wie folgt zu konvertieren:

1. Frage den Benutzer nach dem Namen einer Stadt und der aktuellen Temperatur in Fahrenheit.
2. Wandel die Temperatur in Celsius um.
3. Wenn die Temperatur unter dem Gefrierpunkt (0 °C) liegt, drucke eine Warnmeldung aus, die sagt: 
"Warnung: Die Temperatur liegt unter dem Gefrierpunkt." 
Andernfalls drucke eine Nachricht aus, die sagt: "Die Temperatur liegt über dem Gefrierpunkt."
4. Schließlich drucke immer die Temperatur in Celsius aus (bis zu einer Dezimalstelle).

PS: Die Formel zur Umrechnung von Fahrenheit in Celsius lautet:
C = (F - 32) * 5/9

"""


Stadt = input("Geben Sie den Namen einer Stadt ein:")
Fahrenheit = input(f"Geben Sie die aktuelle Temperatur in Fahrenheit in {Stadt} ein:")
Celsius = (float(Fahrenheit) - 32 ) * 5/9    # Die Temperatur in Celsius umwandeln
T = float(Celsius)     #Temperatur ## Die Temperatur in einen Float-Wert umwandeln

if T < 0:
    print("Warnung: Die Temperatur liegt unter dem Gefrierpunkt.")
else:
    print("Die Temperatur liegt über dem Gefrierpunkt.")
print(f"Die aktuelle Temperatur in {Stadt} beträgt: {T:.1f} Grad Celsius.")