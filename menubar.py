import tkinter
from tkinter import filedialog
from tkinter import *

import os

class menubar(tkinter.Menu):

    def __init__(self, master):
        super().__init__(master)
        
        #create all menus+submenus in their own functions
        self.__create_filemenu(master)
        self.__create_editmenu(master)
        self.__create_searchmenu(master)
        self.__create_segmenu(master)
        self.__create_transmenu(master)
        
       
        


    def __create_filemenu(self, master):
        #create the first submenu for "Datei"
        filemenu = tkinter.Menu(self,tearoff=0)
        self.add_cascade(label="Datei", menu=filemenu)
        
        #adding the commands to the filemenu
        filemenu.add_command(label="Neu" ,command=lambda: self.newFile(master), accelerator="Ctrl+n")
        filemenu.add_command(label="Öffnen", command=lambda: self.openFile(master), accelerator="Ctrl+O")
        filemenu.add_command(label="Speichern", command=lambda: self.saveFile(master), accelerator="Ctrl+S")
        filemenu.add_command(label="Speichern unter...", command= lambda: self.saveFileUnder(master), accelerator="Ctrl+Alt+S")
        
    def __create_editmenu(self, master):
        #create the edit menu
        editmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Bearbeiten", menu=editmenu)
        
        #adding commands to the edit menu
        editmenu.add_command(label="Rückgängig") #,command=TODO)
        editmenu.add_command(label="Wiederherstellen") #,command=TODO)
        editmenu.add_separator()
        editmenu.add_command(label="Ausschneiden")#,command=TODO)
        editmenu.add_command(label="Kopiere")#,command=TODO)
        editmenu.add_command(label="Einfügen")#,command=TODO)
        editmenu.add_command(label="Löschen")#,command=TODO)
        editmenu.add_command(label="Alles auswählen")#,command=TODO)
        
    def __create_searchmenu(self, master):
        #create the search menu
        searchmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Suchen", menu=searchmenu)
        
        #adding commands to the searchmenu
        searchmenu.add_command(label="Suchen...") #,command=TODO)
        
    def __create_segmenu(self, master):
        #ceate the segmentation menu
        segmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Segmentieren", menu=segmenu)
        
        #adding commands to the segmentation menu
        segmenu.add_command(label="Einzeltext")#,command=TODO)
        segmenu.add_command(label="Multitext")#,command=TODO)
    
    
    def __create_transmenu(self, master):
        #creating the transcribtion menu
        transmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Transkription", menu=transmenu)
        
        #adding commands to the transcribtion menu
        transmenu.add_command(label="Einzeltranskription")#,command=TODO)
        transmenu.add_command(label="Multitranskription")#,command=TODO)
        transmenu.add_separator()
        transmenu.add_command(label="Einstellungen")#,command=TODO)
        transmenu.add_command(label="Hilfe")#,command=TODO)
        
        
    def saveFileUnder(self,master) -> bool:
        #es wird ein Boolean zurück gegeben, True wenn das speichern erfolgreich war, False wenn nicht
        try:
            #getting a name path
            text_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text File","*.txt"),("All files", "*.*")))
            if text_file:
                #seperate only the name
                name = text_file.split("/").pop()
                master.title(f'{name} - Transkriptionseditor')
                master.statusbar.status.config(text=f'Saved: {text_file}')
                
                #create and open the file
                text_file = open(text_file, 'w')
                text_file.write(master.textfield.get(1.0,'end'))
                text_file.close()
                
                return True
                
            else: raise Error
               
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim Speichern ist ein unvorhergesehender Fehler aufgetreten.')
            print("Error in saveFileUnder: "+str(e))
            return False
            
    def saveFile(self,master) -> bool:
        #es wird ein Boolean zurück gegeben, True wenn das speichern erfolgreich war, False wenn nicht
        try: #try block für generelle fehler
            #speichert den pfad von eventuellen dateien zwischen aus der statusbar
            status = master.statusbar.status.cget("text").split("Saved: ").pop().replace('/','\\')
            try: #try block für das öffnen
                if os.path.exists(status): #checkt ob es die datei gibt
                    #überschreibt inhalt mit dem aus dem textfeld
                    text_file = open(status, mode ='w')
                    text_file.write(master.textfield.get(1.0,'end'))
                    text_file.close()
                    return True
                    
                else: raise OSError
            except Exception as e:
                print("Error in saveFile: "+str(e))
                #falls speichern nicht möglich ist, wird speichern unter aufgerufen um neue datei zu erstellen
                if self.saveFileUnder(master):
                    return True
                else: return False
            
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim Speichern ist ein unvorhergesehender Fehler aufgetreten.')
            print("Error in saveFile: "+str(e))
            return False
            
            
    def newFile(self, master):
        try:
            status = master.statusbar.status.cget("text").split("Saved: ").pop().replace('/','\\')
            #wir überprüfen als erstes ob kein Dateipfad hinterlegt ist.
            if status == 'Ready':
                if len(master.textfield.get(1.0,'end'))!=1: #wir schauen ob überhaupt was im textfeld steht
                    awnser = tkinter.messagebox.askyesnocancel("Speichern", "Wollen Sie speichern?")
                else: awnser = False
            else:
                #wir überprüfen, ob die texte identisch sind, wenn ja muss nicht gespeichert werden.
                text_file = open(status, mode ='r')
                text_file_text = text_file.read()
                text_file.close()
                if text_file_text == master.textfield.get(1.0,'end'):
                    awnser = False
                else:
                    awnser = tkinter.messagebox.askyesnocancel("Speichern", "Wollen Sie speichern?")
            
            if awnser:
                #wenn ja, dann wird versucht zu speichern, wenn das nicht klappt wird innerhalt der saveFile funtion saveFileUnder aufgerufen
                if self.saveFile(master):
                    #wenn das speichern erfolgreich war
                    master.textfield.delete(1.0,'end')
                    #update statusbar und Titel
                    master.statusbar.status.config(text="Ready")
                    master.title('Transkriptionseditor')
                else:
                    return
            if awnser == False:
                #wenn nein, wird nur der textbereich gecleart
                master.textfield.delete(1.0,'end')
                #update statusbar und Titel
                master.statusbar.status.config(text="Ready")
                master.title('Transkriptionseditor')
            else:
                #wenn cancel gedrückt wird, dann passiert nichts und der Text bleibt stehen
                pass
        
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim erstellen ist ein unvorhergesehender Fehler aufgetreten.')
            print("Error in newFile: "+str(e))
            
    def openFile(self, master):
        try:
            #wir rufen newFile auf, da uns so das eventuelle abspeichern etc abgenommen wird
            self.newFile(master)
            
            text_file = filedialog.askopenfilename()
            name = text_file.split("/").pop()
            master.title(f'{name} - Transkriptionseditor')
            master.statusbar.status.config(text=f'Saved: {text_file}')
            text_file = open(text_file, "r")
            master.textfield.insert(1.0,text_file.read())
            text_file.close()
            
            
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim öffnen ist ein unvorhergesehender Fehler aufgetreten.')
            print("Error in openFile: "+str(e))
            
 