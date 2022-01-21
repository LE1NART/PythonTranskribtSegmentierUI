import tkinter
from tkinter import filedialog
from tkinter import *


class searchmenu(tkinter.Menu):
   def __init__(self,menu,master):
        super().__init__(menu, tearoff=0)
        
        
        #adding commands to the searchmenu
        self.add_command(label="Suchen...") #,command=TODO)