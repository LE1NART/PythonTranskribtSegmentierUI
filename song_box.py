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

    def __inside(self,toolbar,master):
        self.boxList = tkinter.Listbox(self)
        self.boxList.pack(expand=True,fill="both")

        self.menu = tkinter.Menu(self)
        self.addMenu = tkinter.Menu(self.menu, tearoff=0)
        self.deleteMenu = tkinter.Menu(self.menu, tearoff=0)

        self.addMenu.add_command(label="Eine Datei hinzufügen", command=lambda: self.addFile(toolbar))
        self.addMenu.add_command(label="Mehrere Dateien hinzufügen", command=lambda: self.addMultipleFile(toolbar))

        self.deleteMenu.add_command(label="Datei löschen", command=lambda: self.deleteFile(toolbar))
        self.deleteMenu.add_command(label="Alle Dateien löschen", command=lambda: self.deleteAllFile(toolbar))

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
    def addMultipleFile(self,toolbar):
        audio_files = filedialog.askopenfilename(filetypes=[("Audio File", "*.MP3 *.mp3"),("Audio File","*.wav")])
        for audio_file in audio_files:
            self.addSong(toolbar,audio_file)
            toolbar.addSong(audio_file)

    def deleteFile(self,toolbar):
        pass

    def deleteAllFile(self,toolbar):
        pass
    
    #der Grund das wir diese Funktion aussondern ist reduktion von rekursion
    def addSong(self,toolbar,audio_file):
        pass