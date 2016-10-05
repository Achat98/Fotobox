# coding: utf8


#Variablen
#Speicherort der Datei
pfad = "./"
global webadress
#Datei, welche auf Server für Senden verantwortlich ist (senden.php)
webadress ="******your web adress******"

#Import von Bibliotheken
import os
import random


#Funktion für Picture name
def picturename():
    pic_title = random.randint(1,9999999)
    return pic_title

#QR Code erstellen
def qrcode(code):
    cmd = "qrencode -o "+ code + "_qrcode.png " + webadress + "?code=" + code
    os.system(cmd)

#Bild aufnehmen
def bild():
    name = str(picturename())
    path_picture = pfad+name+".jpg"
    if os.path.exists(path_picture) == False:
        cmd = "gphoto2 --capture-image-and-download --filename="+name+".jpg"
        os.system(cmd)
        filename = name+".jpg"
    else:
        filename = bild()
    #QR Code Generieren
    qrcode(name)
    return filename




#Pogrammablauf
finished = False
while not finished:
    try:
        #Abfrage Eingabe
        print("Eingabe?"),
        input = raw_input()
        #Bild aufnehmen bei leerer Eingabe (nur Enter gedrückt)
        if input == "":
            bild()
        if input == "q":
            print("quit")
            finished = True
    except (KeyboardInterrupt, SystemExit):
        finished = True
