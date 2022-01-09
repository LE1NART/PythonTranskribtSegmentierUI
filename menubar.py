import tkinter
from tkinter import filedialog

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
        filemenu.add_command(label="Neu") #,command=TODO)
        filemenu.add_command(label="Öffnen")#, command=TODO)
        filemenu.add_command(label="Speichern", command=lambda: self.saveFile(master))
        filemenu.add_command(label="Speichern unter...", command= lambda: self.saveFileUnder(master))
        
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
        
        
    def newFile(self, master):
        print("Hello")
        #Todo, aber erst StatusBar neu aufarbeite, sodass Filename etc. in statusbar zwischengelagert werden kann
        
        
    def saveFileUnder(self,master):
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
               
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim Speichern ist ein unvorhergesehender Fehler aufgetreten.')
            print(e)
            
    def saveFile(self,master):
        try: #try block für generelle fehler
            #speichert den pfad von eventuellen dateien zwischen aus der statusbar
            status = master.statusbar.status.cget("text").split("Saved: ").pop().replace('/','\\')
            try: #try block für das öffnen
                if os.path.exists(status): #checkt ob es die datei gibt
                    #überschreibt inhalt mit dem aus dem textfeld
                    text_file = open(status, mode ='w')
                    text_file.write(master.textfield.get(1.0,'end'))
                    text_file.close()
                else: raise OSError
            except Exception as e:
                print(e)
                #falls speichern nicht möglich ist, wird speichern unter aufgerufen um neue datei zu erstellen
                self.saveFileUnder(master)
            
        except Exception as e:
            tkinter.messagebox.showwarning('warning', 'Beim Speichern ist ein unvorhergesehender Fehler aufgetreten.')
            print(e)