import tkinter
from tkinter import filedialog

class songBox(tkinter.Toplevel):
    def __init__(self,toolbar,master):
        super().__init__()

        self.title("Audio Liste")

        self.geometry("500x250")
        self.minsize(500,250)
        self.resizable(False,False)

        self.__inside(toolbar,master)

        self.config(menu=self.menu)

        self.protocol('WM_DELETE_WINDOW', lambda: self.__closeWindow(toolbar)) #überschreiben, des xButtons wenn das TopLvl Fenster verlassen wird


    def __inside(self,toolbar,master):
        self.boxList = tkinter.Listbox(self,selectmode="single")
        self.boxList.pack(expand=True,fill="both")

        self.menu = tkinter.Menu(self)
        self.addMenu = tkinter.Menu(self.menu, tearoff=0)
        self.deleteMenu = tkinter.Menu(self.menu, tearoff=0)

        self.addMenu.add_command(label="Eine Datei hinzufügen", command=lambda: self.addFile(toolbar))
        self.addMenu.add_command(label="Mehrere Dateien hinzufügen", command=lambda: self.addMultipleFiles(toolbar))

        self.deleteMenu.add_command(label="Datei löschen", command=lambda: self.deleteFile(toolbar))
        self.deleteMenu.add_command(label="Alle Dateien löschen", command=lambda: self.deleteAllFiles(toolbar))

        self.menu.add_cascade(label="Add", menu=self.addMenu)
        self.menu.add_cascade(label="Delete", menu=self.deleteMenu)

    #die function öffnet die datei und ruft die beiden addSong funktionen auf, die eigene und die von der Toolbar
    def addFile(self,toolbar):
        #open the file with tkinter filedialog
        audio_file = filedialog.askopenfilename(filetypes=[("Audio File", "*.MP3 *.mp3"),("Audio File","*.wav")])
        #calling the own addSong function
        self.addSong(toolbar,audio_file)
        #and the toolbarAddsong Function
        toolbar.addSong(audio_file)

    #sie addFile nur für mehere
    def addMultipleFiles(self,toolbar):
        audio_files = filedialog.askopenfilenames(filetypes=[("Audio File", "*.MP3 *.mp3"),("Audio File","*.wav")])
        for audio_file in audio_files:
            self.addSong(toolbar,audio_file)
            toolbar.addSong(audio_file)
        self.lift()
    
    #der Grund das wir diese Funktion aussondern ist reduktion von rekursion
    def addSong(self,toolbar,audio_file):
        audio_name = audio_file.split("/").pop()
        self.boxList.insert(tkinter.END ,audio_name)
        self.boxList.selection_set(0)

    #löscht die ausgewählte datei
    def deleteFile(self,toolbar):
        ind = self.boxList.curselection()[0]
        toolbar.deleteSong(ind)
        self.boxList.delete(ind)

    #löscht alle Dateien in der Boxlist
    def deleteAllFiles(self,toolbar):
        for ind  in reversed(range(self.boxList.size())):
            toolbar.deleteSong(ind)
            self.boxList.delete(ind)

    #wird von der Toolbar genutzt, damit wenn der nextSong Button genutzt wird auch die selection weitergeht
    def nextSong(self):
        newInd = self.boxList.curselection()[0] + 1
        if newInd < self.boxList.size():
            self.boxList.selection_clear(newInd-1)
            self.boxList.activate(newInd)
            self.boxList.select_set(newInd)
        else:
            pass
    #siehe nextSong nur andere richtung
    def prevSong(self):
        newInd = self.boxList.curselection()[0] - 1
        if newInd >= 0:
            self.boxList.selection_clear(newInd+1)
            self.boxList.activate(newInd)
            self.boxList.select_set(newInd)
        else:
            pass

    #overrite für wenn das Window geschlossen wird
    def __closeWindow(self, toolbar):
        self.withdraw()
        toolbar.trackBoxVis = False