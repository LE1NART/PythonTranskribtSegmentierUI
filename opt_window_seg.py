import tkinter
import editListe
import json

class optWindow(tkinter.Toplevel):
    def __init__(self,menu,master):
        super().__init__()
        
        self.title("Einstellungen")
        
        self.geometry("500x200")
        self.minsize(500,250)
        self.resizable(False, False)
        
        self.__inside(menu,master)

        self.liste = None

        self.__readOptions()

        self.protocol('WM_DELETE_WINDOW', lambda: self.__closeWindow(menu,master)) #überschreiben, des xButtons wenn das TopLvl Fenster verlassen wird

    def __inside(self,menu,master):
        #row and column configure
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.grid_rowconfigure(8,weight=1)

        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1) 

        label = tkinter.Label(self,text="Dieses Fenster muss geschlossen werden, damit die Einstellungen übernommen werden.")
        label.grid(row=8,column=0,columnspan=3,sticky=tkinter.W+tkinter.E)

        self.punktVal = tkinter.IntVar()
        self.kommaVal = tkinter.IntVar()
        self.undVal = tkinter.IntVar()
        self.oderVal = tkinter.IntVar()
        self.klammerVal = tkinter.IntVar()
        self.abkVal = tkinter.IntVar()
        self.doppelPunktVal = tkinter.IntVar()

        self.punktButton = tkinter.Checkbutton(self,text="Punkte (+?,!)",variable = self.punktVal)
        self.kommaButton = tkinter.Checkbutton(self,text="Komma",variable = self.kommaVal)
        self.undButton = tkinter.Checkbutton(self,text="Und",variable = self.undVal)
        self.oderButton = tkinter.Checkbutton(self,text="Oder",variable = self.oderVal)
        self.klammerButton = tkinter.Checkbutton(self,text="Klammer",variable = self.klammerVal)
        self.abkButton = tkinter.Checkbutton(self,text="Abkürzungen",variable = self.abkVal)
        self.doppelPunktButton = tkinter.Checkbutton(self,text="Doppelpunkt",variable=self.doppelPunktVal)

        self.abkListeButton = tkinter.Button(self,text="Liste der Abkürzungen",command=lambda:self.__openListe())


        self.punktButton.grid(row=0,column=1)
        self.kommaButton.grid(row=1,column=1)
        self.undButton.grid(row=2,column=1)
        self.oderButton.grid(row=3,column=1)
        self.klammerButton.grid(row=4,column=1)
        self.abkButton.grid(row=5,column=1)
        self.abkListeButton.grid(row=7,column=1)
        self.doppelPunktButton.grid(row=6, column=1)


    def __openListe(self):
        if self.liste:
            self.liste.lift()
        else:
            self.liste = editListe.topListe(self)


    def __readOptions(self):
        with open('options.json') as f:
            data = json.load(f)
        

        for d in data['segmentOptions'].values():
            exec(f"self.{d['id']}.set({d['value']})") 
            """wir setzen hier für die jeweils passende variable den wert den wir aus 
            der json datei lesen, damit wir ein haufen if statements verhindern, nutzen 
            wir die exec methode, welche einfach ausführt, was da als string steht
            """

    def __writeOptions(self):
        with open('options.json', 'r') as f:
            data = json.load(f)

        
        for d in data['segmentOptions'].values():
                exec(f"d['value'] = self.{d['id']}.get()")
        
        with open('options.json', 'w') as f:
            json.dump(data,f, indent=2)
             
        


        

    #overwrite für das schliesen des fensters
    def __closeWindow(self,menu,master):
        self.__writeOptions()
        self.destroy() #normal destroy
        master.menubar.segmenu.optwindow = None #damit ein neues optwindow erstellt werden kann