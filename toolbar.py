import tkinter
import os
import pygame

import song_box

class toolbar(tkinter.Frame):
    
    def __init__(self, master):
        super().__init__( master, bd=1, relief='groove')
        
        #row- and column configuration for the toolbar
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_columnconfigure(6,weight=1)
        self.grid_columnconfigure(7,weight=1000)
        
        #calling functions to create the Buttons and the Slider
        self.__addButtons(master)
        self.__addSlider()
        
        self.trackBox = None
        self.trackBoxVis = False
        self.trackList = [] #diese Liste dient dazu, dass wir hier und in der SongBox gleichermaßen zugriff auf die Songs haben
        self.play = False

        pygame.mixer.init()

    def __addButtons(self,master):
        #adding the Buttons for the MP3 Controll
        
        #saving the Icons to show them the whole time
        self.icon_tracklist=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\tracklist.png')
        self.icon_pause=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\pause.png')        
        self.icon_play=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\play.png')
        self.icon_trackback=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\trackback.png')
        self.icon_tracknext=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\tracknext.png')

        
        #creating the tracklist button
        self.tracklist = tkinter.Button(self, image=self.icon_tracklist, activebackground="#a6eff7" ,command=lambda: self.createTrackBox(master))
        self.tracklist.grid(row=0, column=0, sticky='w')

        #creating the button to going to the track before
        self.trackback = tkinter.Button(self, image=self.icon_trackback, activebackground="#a6eff7",command=lambda: self.prevSong())
        self.trackback.grid(row=0, column=1, sticky='w', padx=(5,0))
        
        #creating the play/pause button
        self.pause_play = tkinter.Button(self, image=self.icon_play, activebackground="#a6eff7" ,command=lambda: self.playSong())
        self.pause_play.grid(row=0, column=2, sticky='w')
        
        #creating the next track button
        self.tracknext = tkinter.Button(self, image=self.icon_tracknext, activebackground="#a6eff7",command= lambda: self.nextSong())
        self.tracknext.grid(row=0, column=3, sticky='w', padx=(0,5))
        
        
    def __addSlider(self):
        #adding the slider and volume controll to the toolbar
        self.volume = tkinter.Spinbox(self, from_=0, to=100,width=5)
        self.playTime = tkinter.Scale(self, from_=0, to=100, orient='horizontal', length=200)
        
        self.volume.grid(row=0, column=5, sticky='w', padx=5)
        self.playTime.grid(row=0, column=6, sticky='w', padx=5)

        


    def createTrackBox(self,master):
        if self.trackBox: #check ob das Fenster schon existiert,
            if self.trackBoxVis == False:
                self.trackBox.deiconify() #wird sichtbar gemacht
                self.trackBoxVis = True
                self.trackBox.lift()#wenn ja, kommt es in den Vordergrund
            else:
                self.trackBox.lift()
        else:
            self.trackBox = song_box.songBox(self,master) #wenn nicht erzeugt
            self.trackBoxVis = True
            for track in self.trackList:
                self.trackBox.addSong(self,track)

    #Hier wird der Dateipfad der audio datei der Liste hinzugefügt
    def addSong(self, audio_file):
        self.trackList.append(audio_file)

    #der Song an der stelle des Indexes wird aus der Liste gelöscht
    def deleteSong(self,index):
        self.trackList.pop(index)

    def playSong(self):
        if self.play == False and pygame.mixer.music.get_pos() > 0:
            self.play = True
            self.pause_play.config(image=self.icon_pause)
            pygame.mixer.music.unpause()

        elif self.play == False:
            self.play = True
            self.pause_play.config(image=self.icon_pause)
            try:
                self.startSong()
            except Exception as e:
                print(e)


        elif self.play == True:
            self.play = False
            self.pause_play.config(image=self.icon_play)
            
            pygame.mixer.music.pause()
            print(pygame.mixer.music.get_pos())

    def startSong(self):
        path = self.trackList[self.trackBox.boxList.curselection()[0]]
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(loops=0)

    def nextSong(self):
        self.trackBox.nextSong()
        self.startSong()

    def prevSong(self):
        self.trackBox.prevSong()
        self.startSong()

    def skipBack(self):
        pos = pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos(pos-10)
    
    def skipForward(self):
        pos = pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos(pos+10)