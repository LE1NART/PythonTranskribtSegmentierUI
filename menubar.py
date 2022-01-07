import tkinter

class menubar(tkinter.Menu):

    def __init__(self):
        super().__init__()
        
        self.__create_filemenu()
        self.__create_editmenu()
        self.__create_searchmenu()
        self.__create_segmenu()
        self.__create_transmenu()
        
        


    def __create_filemenu(self):
        #create the first submenu for "Datei"
        filemenu = tkinter.Menu(self,tearoff=0)
        self.add_cascade(label="Datei", menu=filemenu)
        
        filemenu.add_command(label="Neu") #,command=TODO)
        filemenu.add_command(label="Öffnen")#, command=TODO)
        filemenu.add_command(label="Speichern")#, command=TODO)
        filemenu.add_command(label="Speichern unter...")#, command=TODO)
        
    def __create_editmenu(self):
        editmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Bearbeiten", menu=editmenu)
        
        editmenu.add_command(label="Rückgängig") #,command=TODO)
        editmenu.add_command(label="Wiederherstellen") #,command=TODO)
        editmenu.add_separator()
        editmenu.add_command(label="Ausschneiden")#,command=TODO)
        editmenu.add_command(label="Kopiere")#,command=TODO)
        editmenu.add_command(label="Einfügen")#,command=TODO)
        editmenu.add_command(label="Löschen")#,command=TODO)
        editmenu.add_command(label="Alles auswählen")#,command=TODO)
        
    def __create_searchmenu(self):
        searchmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Suchen", menu=searchmenu)
        
        searchmenu.add_command(label="Suchen...") #,command=TODO)
        
    def __create_segmenu(self):
        segmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Segmentieren", menu=segmenu)
        
        segmenu.add_command(label="Einzeltext")#,command=TODO)
        segmenu.add_command(label="Multitext")#,command=TODO)
    
    
    def __create_transmenu(self):
        transmenu = tkinter.Menu(self, tearoff=0)
        self.add_cascade(label="Transkription", menu=transmenu)
        
        transmenu.add_command(label="Einzeltranskription")#,command=TODO)
        transmenu.add_command(label="Multitranskription")#,command=TODO)
        transmenu.add_separator()
        transmenu.add_command(label="Einstellungen")#,command=TODO)
        transmenu.add_command(label="Hilfe")#,command=TODO)