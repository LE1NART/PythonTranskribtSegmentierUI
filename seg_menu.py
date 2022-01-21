import tkinter
from tkinter import filedialog
from tkinter import *


class segmenu(tkinter.Menu):
   def __init__(self,menu,master):
        super().__init__(menu, tearoff=0)
        
       
        
        #adding commands to the segmentation menu
        self.add_command(label="Einzeltext")#,command=TODO)
        self.add_command(label="Multitext")#,command=TODO)