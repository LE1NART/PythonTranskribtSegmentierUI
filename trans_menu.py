import tkinter
from tkinter import filedialog
from tkinter import *


class transmenu(tkinter.Menu):
   def __init__(self,menu,master):
        super().__init__(menu, tearoff=0)
        
      
        
        #adding commands to the transcribtion menu
        self.add_command(label="Einzeltranskription")#,command=TODO)
        self.add_command(label="Multitranskription")#,command=TODO)
        self.add_separator()
        self.add_command(label="Einstellungen")#,command=TODO)
        self.add_command(label="Hilfe")#,command=TODO)
        