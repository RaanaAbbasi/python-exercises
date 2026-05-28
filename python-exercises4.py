"""
    Aufgabe_3a_Lektion_8
"""
#1.Verbessere dein Programm von letzter Woche, um mehrere Städte zu verarbeiten.
#2.Der Benutzer sollte in der Lage sein, die Namen und Temperaturen so vieler Städte einzugeben,
# # wie er möchte Verwende eine Schleife, um dies zu erleichtern, 
#3.gib alle Städte zusammen mit ihrer Temperatur in Celsius und Fahrenheit aus.
# 4.Gib erneut eine Warnung aus, wenn die Temperatur unter dem Gefrierpunkt liegt.
# #5.Um die Schleife zu beenden, sollte der Benutzer in der Lage sein, „exit“ als Stadtnamen einzugeben.
"""
Beispielausgabe:
Bitte geben Sie den Namen einer Stadt ein: München
Bitte geben Sie die aktuelle Temperatur in Fahrenheit in München ein: 14
Die aktuelle Temperatur in München beträgt 14°F oder -10°C.
Warnung: Die Temperatur liegt unter dem Gefrierpunkt.
"""

Stadt_Name = input("Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:")

while Stadt_Name != "exit":
       Fahrenheit = input(f"Bitte geben Sie die aktuelle Temperatur in Fahrenheit in {Stadt_Name} ein:")
       Celsius = (float(Fahrenheit) - 32 ) * 5/9    # Die Temperatur in Celsius umwandeln
       print(f"Die aktuelle Temperatur in {Stadt_Name} beträgt {Fahrenheit}°F oder {Celsius:.2f}°C.")
       if Celsius < 0:
        print("Warnung: Die Temperatur liegt unter dem Gefrierpunkt.")
       Stadt_Name = input("Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:")

print("***geshrieben von Raana Abbasi!***") 



#zum Beispiel:

#Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:München
#Bitte geben Sie die aktuelle Temperatur in Fahrenheit in München ein:14
#Die aktuelle Temperatur in München beträgt 14°F oder -10.00°C.
#Warnung: Die Temperatur liegt unter dem Gefrierpunkt.

#Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:Paris
#Bitte geben Sie die aktuelle Temperatur in Fahrenheit in Paris ein:35
#Die aktuelle Temperatur in Paris beträgt 35°F oder 1.67°C.

#Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:Teheran ( Hauptstadt im Iran)
#Bitte geben Sie die aktuelle Temperatur in Fahrenheit in Teheran ( Hauptstadt im Iran) ein:70
#Die aktuelle Temperatur in Teheran ( Hauptstadt im Iran) beträgt 70°F oder 21.11°C.

#Bitte geben Sie den Namen einer Stadt ein oder exit zum beenden:exit
#***geshrieben von Raana Abbasi!***

