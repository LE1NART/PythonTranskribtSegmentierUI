import tkinter


import search_window


class searchmenu(tkinter.Menu):
    def __init__(self,menu,master):
        super().__init__(menu, tearoff=0)
        
        
        #adding commands to the searchmenu
        self.add_command(label="Suchen..." ,command=lambda: self.create_searchWindow(menu,master), accelerator="Crtl+F")
        
        #kontrollvariable, damit nicht mehrere fenster geöffnet werden
        self.searchwindow = None
        
       
        
    def create_searchWindow(self,menu,master):
        if self.searchwindow: #wenn ein fenster existiert
            self.searchwindow.lift() #wird es in den vordergrund gerufen
        else: #wenn nicht wir
            self.searchwindow = search_window.searchWindow(menu,master)
        
    
    