import tkinter
import menubar
import toolbar
import statusbar

class fenster(tkinter.Tk):
    
    #init function für fenster
    def __init__(self):
        
        #calling die tkinter.Tk init methode
        super().__init__()
        
        #values für das Fenster
        self.title("Transkriptionseditor")
        self.geometry("500x300")
        self.minsize(700,500)
        self.resizable(True, True)
        
        #row- and columnconfiguration for the layout
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1000)
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure(0,weight=1)
    
        #create all objectives in "private" functions
        self.__Main_Frame()
        self.__create_StatusBar()
        self.__create_Menu()
        self.__create_Toolbar()
        self.__create_Scrollbar()
        self.__create_Textfield()
        
        #calling function to set all bindings
        self.__set_Bindings()
        
        #setting focus so the Bindings work from the beginning
        self.textfield.focus_set()

        #variable für modifieSearch
        self.mod = 0
        
        
        
       
    def __Main_Frame(self):
        #create the mainframe, in the mainframe is the textfield and the scrollbar for the textfield
        self.mainFrame = tkinter.Frame(self)
        self.mainFrame.grid(row=1, sticky='news')
        
        

    #Private Methode, welche die menubar erzeugt
    def __create_Menu(self):
        #create the menubar
        self.menubar = menubar.menubar(self)
        self.config(menu= self.menubar)
        
    def __create_Toolbar(self):
        #create the toolbar, from his own class
        self.toolbar = toolbar.toolbar(self)
        self.toolbar.grid(row=0, sticky='news')

        
    def __create_StatusBar(self):
        #create the status bar as a Frame
        self.statusbar = statusbar.statusbar(self)
        self.statusbar.grid(row=2, sticky='news')
        
        
        
        
    def __create_Scrollbar(self):
        #packing Scrollbar
        self.scrollbar = tkinter.Scrollbar(self.mainFrame)
        self.scrollbar.pack(side="right",fill="y")
        
    def __create_Textfield(self):
        #creating the textfield and setting the scrollcommand in the textfield to the scrollbar
        self.textfield = tkinter.Text(self.mainFrame, undo=True,yscrollcommand=self.scrollbar.set)
        self.textfield.pack(expand=True,fill="both")
        
        #setting the scrollbar to the textfield viewfield
        self.scrollbar.config(command=self.textfield.yview)
        
        #wenn das textfeld bearbeitet wird, dann wir dieses event getriggert
        self.textfield.bind('<<Modified>>', lambda event: self.modifieSearch())
        
    
    def modifieSearch(self): #wenn das Textfield modifiziert wird, wird diese funktion aufgerufen
        if self.mod == 0: #die variable benutzen wir, damit es nicht zweimal ausgeführt wird, passiert sonst
            self.mod = 1
            if self.menubar.searchmenu.searchwindow: #muss nur gemacht werden, wenn auch das such menü auf ist
                self.menubar.searchmenu.searchwindow.startButton(self) #es wird erneut gesucht, damit wenn weiter gedrückt wird etc nicht die markierungen für die suche ungenau wird
            self.textfield.edit_modified(False) #die Modifie flag vom textfield wird auf false gesetzt, weil sonst weitere modifizierungen nicht erkannt werden
        else:
            self.mod = 0
        
    def __set_Bindings(self):
        #creating all the bindings for the programm
        #adding bindings for filemenu
        self.bind('<Control -n>', lambda event : self.menubar.filemenu.newFile(self))
        self.bind('<Control -o>', lambda event : self.menubar.filemenu.openFile(self))
        self.bind('<Control -s>', lambda event : self.menubar.filemenu.saveFile(self))
        self.bind('<Control - Alt - s>', lambda event : self.menubar.filemenu.saveFileUnder(self))
        
        #adding binding for searchmenu
        self.bind('<Control -f>', lambda event : self.menubar.searchmenu.create_searchWindow(self.menubar,self))
