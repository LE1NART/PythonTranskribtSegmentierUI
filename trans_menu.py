import tkinter
from tkinter import filedialog
from tkinter import *

import tkinter
import speech_recognition

import trans_window


class transmenu(tkinter.Menu):
   def __init__(self,menu,master):
         super().__init__(menu, tearoff=0)
         
         self.transwindow = None
         
         self.ambient = 0

         #adding commands to the transcribtion menu
         self.add_command(label="Einzeltranskription",command=lambda: self.__soloTrans(menu,master))
         self.add_command(label="Multitranskription",command=lambda: self.create_transWindow(menu,master))
         self.add_separator()
         self.add_command(label="Einstellungen")#,command=TODO)
         self.add_command(label="Hilfe")#,command=TODO)
         
   def create_transWindow(self,menu,master):
      if self.transwindow:
            self.transwindow.lift()
      else:
            self.transwindow = trans_window.transWindow(menu,master)

   def __soloTrans(self,menu,master):
      file = filedialog.askopenfilename()
      if file.split('.')[1] == 'wav': #nur wav dateien
         recognizer = speech_recognition.Recognizer()
         with speech_recognition.AudioFile(file) as source:
            if self.ambient == 1:
                  recognizer.adjust_for_ambient_noise(source)
            # listen for the data (load audio to memory)
            audio_data = recognizer.record(source)
            # recognize (convert from speech to text)
            text = recognizer.recognize_google(audio_data, language='de-DE')
            
            print(type(text))
            master.textfield.delete(1.0,tkinter.END)
            master.textfield.insert(1.0,text)
            #datei = open(file.split('.wav')[0]+'.txt', 'w')
            #datei.write(text)
            #datei.close()
      else:
         pass