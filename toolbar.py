import tkinter

import os

class toolbar(tkinter.Frame):
    
    def __init__(self):
        super().__init__( bd=1, relief='groove')
        
        
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_columnconfigure(6,weight=1)
        self.grid_columnconfigure(7,weight=1000)
        
        self.__addButtons()
        self.__addSlider()
        
        
    def __addButtons(self):
        self.icon_tracklist=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\tracklist.png')
        self.icon_pause=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\pause.png')        
        self.icon_play=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\play.png')
        self.icon_trackback=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\trackback.png')
        self.icon_tracknext=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\tracknext.png')


        
        
        
        
        tracklist = tkinter.Button(self, image=self.icon_tracklist, activebackground="#a6eff7") #,command=TODO)
        tracklist.grid(row=0, column=0, sticky='w')

        trackback = tkinter.Button(self, image=self.icon_trackback, activebackground="#a6eff7") #,command=TODO)
        trackback.grid(row=0, column=1, sticky='w', padx=(5,0))
        
        pause_play = tkinter.Button(self, image=self.icon_play, activebackground="#a6eff7") #,command=TODO)
        pause_play.grid(row=0, column=2, sticky='w')
        
        tracknext = tkinter.Button(self, image=self.icon_tracknext, activebackground="#a6eff7") #,command=TODO)
        tracknext.grid(row=0, column=3, sticky='w', padx=(0,5))
        
        
    def __addSlider(self):
        self.volume = tkinter.Spinbox(self, from_=0, to=100,width=5)
        self.playTime = tkinter.Scale(self, from_=0, to=100, orient='horizontal', length=200)
        
        self.volume.grid(row=0, column=5, sticky='w', padx=5)
        self.playTime.grid(row=0, column=6, sticky='w', padx=5)