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
        self.add_command(label="Ausschneiden")#,command=TODO)
        self.add_command(label="Kopiere")#,command=TODO)
        self.add_command(label="Einfügen")#,command=TODO)
        self.add_command(label="Löschen")#,command=TODO)
        self.add_command(label="Alles auswählen")#,command=TODO)