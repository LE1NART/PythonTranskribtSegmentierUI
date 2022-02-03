import tkinter
from tkinter import filedialog
from tkinter import *


class editmenu(tkinter.Menu):
    def __init__(self,menu,master):
        super().__init__(menu, tearoff=0)
      
        
        #adding commands to the edit menu
        self.add_command(label="Rückgängig" ,command=lambda: master.textfield.edit_undo() , accelerator="Crtl+Z")
        self.add_command(label="Wiederherstellen",command=lambda: master.textfield.edit_redo(), accelerator="Crtl+Y")
        self.add_separator()
        self.add_command(label="Ausschneiden",command=lambda: self.__cut(master), accelerator="Crtl+X")
        self.add_command(label="Kopiere",command=lambda: self.__copy(master), accelerator="Crtl+C")
        self.add_command(label="Einfügen",command=lambda: self.__paste(master), accelerator="Crtl+V")
        self.add_command(label="Löschen",command=lambda: self.__delete(master), accelerator="ENTF")
        self.add_command(label="Alles auswählen",command=lambda: self.__selectAll(master), accelerator="Crtl+A")
        
    #Ausschneiden    
    def __cut(self,master):
        self.__copy(master) #kopiert
        self.__delete(master) #löschen
    
    #Kopieren
    def __copy(self,master):
        if master.textfield.selection_get(): #wenn was ausgewählt ist
            master.clipboard_clear() #clipboard wird gecleart
            master.clipboard_append(master.textfield.selection_get()) #auswahl wird in das Clipboard gespeichert
            

    #Einfügen
    def __paste(self,master):
        master.textfield.insert(master.textfield.index(INSERT),master.clipboard_get()) #aus Clipboard in textfeld
    
    #Löschen
    def __delete(self,master):
        master.textfield.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST) #auswahl wird gelöscht
    
    #alles Auswählen
    def __selectAll(self,master):
        master.textfield.tag_add('sel',1.0,'end') #alles wird ausgewählt