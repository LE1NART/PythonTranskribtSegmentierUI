import tkinter



class fenster(tkinter.Tk):
    
    #init function für fenster
    def __init__(self):
        
        #calling die tkinter.Tk init methode
        super().__init__()
        
        #values für das Fenster
        self.title("My App")
        self.geometry("500x300")
        self.minsize(500,300)
        self.resizable(True, True)
        
        self.grid_rowconfigure(0,weight=1000)
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.__Main_Frame()
        self.__create_Menu()
        self.__create_Scrollbar()
        self.__create_Textfield()
        self.__create_StatusBar()
       
    def __Main_Frame(self):
        self.mainFrame = tkinter.Frame(self)
        self.mainFrame.grid(row=0, sticky='news')
        
        

    #Private Methode, welche die menubar erzeugt
    def __create_Menu(self):
        self.menubar = tkinter.Menu(self)
        self.menubar.add_cascade(label="test")
        self.config(menu= self.menubar)
        
    def __create_StatusBar(self):
        self.status_bar = tkinter.Frame(self)
        self.status_bar.grid(row=2, sticky='news')
            
        self.status_bar.status = tkinter.Label(self.status_bar, text='Ready   ', anchor='e')
        self.status_bar.status.pack(side='right')
        
        
    def __create_Scrollbar(self):
        #packing Scrollbar
        self.scrollbar = tkinter.Scrollbar(self.mainFrame)
        self.scrollbar.pack(side="right",fill="y")
        
    def __create_Textfield(self):
        #creating the textfield and setting the scrollcommand in the textfield to the scrollbar
        self.textfield = tkinter.Text(self.mainFrame, yscrollcommand=self.scrollbar.set)
        self.textfield.pack(expand=True,fill="both")
        
        #setting the scrollbar to the textfield viewfield
        self.scrollbar.config(command=self.textfield.yview)