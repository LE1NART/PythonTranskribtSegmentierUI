import json 
import re
import tkinter

def segment(master,file,p=0):
    try:

        datei = open(file, 'r',encoding="utf-8")
        text = datei.read()
        datei.seek(0)
        datei.close()
        
        with open('options.json') as f:
            data = json.load(f)

        

        text = text.replace("\r\n", " ")
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        
        if (data['segmentOptions']['punktVal']['value']) == 1:
            text = text.replace(". ", ". \r")
            text = text.replace("? " or "?", "? \r")
            text = text.replace("! " or "!", "! \r")

        if (data['segmentOptions']['kommaVal']['value']) == 1:
            text = text.replace(", " or ",", ", \r")

        if (data['segmentOptions']['doppelPunktVal']['value']) == 1:
            text = text.replace(": " or ":", ": \r")
        
        
        # Für die Folgenden Ersätze nutzen wir re.sub, da wir damit raw Strings einlesen können.
        # Dadurch können wir den Vorsatz \b dazu nehmen um sicher zu stellen, dass wir keine Teilwörter Teilen wie z.B. Bund -> B\n und
        
        if (data['segmentOptions']['undVal']['value']) == 1:
            text = re.sub(r"\bund ", "\rund ", text)
        if (data['segmentOptions']['oderVal']['value']) == 1:
            text = re.sub(r"\boder ","\roder ", text)
        
        with open("seg.txt") as f:
            liste = f.read().splitlines() 

        if (data['segmentOptions']['abkVal']['value']) == 0:
            for l in liste:
                    l1 = re.sub(r"\." ,"\."  , l) #wir ersetzen die "." durch "\." damit die im folgenden bei r"" nicht als alles gelesen werden sondern wirklich als punkte
                    #in der vorderen bedingungen muss \. sein, weil sonst wieder alles gelten kann und hinten schreiben wir es nicht in raw also steht da wirklich "\."
                    #wir hatten sonst das Problem das zb die Abkürzung b.w. die abkürzung bzw. ersetzt hat, weil in der liste der "." als jedes zeichen im Raw code gelten konnte
                    c1 = r"\b"+l1+" \r"
                    c2 = l+" "
                    text = re.sub(c1 , c2 , text) #r"{}".format(c1) da nicht einfach r c1 oder ähnliches
            
        
        #segmentierter text wieder in die datei schreiben
        datei = open(file, 'w',encoding="utf-8")
        datei.write(text)
        datei.close()

        if p == 1:
            #clear the textfield
            master.textfield.delete(1.0, tkinter.END)

            #anpassen des Titels und der Statusbar
            name = file.split("/").pop()
            master.title(f'{name} - Transkriptionseditor')
            master.statusbar.status.config(text=f'Saved: {file}')
            #kopieren des textes aus der datei wieder in das textfeld
            text_file = open(file, "r",encoding="utf-8")
            master.textfield.insert(1.0,text_file.read())
            text_file.close()       


    except Exception as e:
        tkinter.messagebox.showwarning('warning', 'Beim Segmentieren ist ein unvorhergesehender Fehler aufgetreten.')
        print("Error in segMenu segmentieren: "+str(e))