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
        
        
    def __cut(self,master):
        self.__copy(master)
        master.textfield.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
        
    def __copy(self,master):
        if master.textfield.selection_get():
            master.clipboard_clear()
            master.clipboard_append(master.textfield.selection_get())
            

    
    def __paste(self,master):
        master.textfield.insert(master.textfield.index(INSERT),master.clipboard_get())
        
    def __delete(self,master):
        master.textfield.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
       
    def __selectAll(self,master):
        master.textfield.tag_add('sel',1.0,'end')