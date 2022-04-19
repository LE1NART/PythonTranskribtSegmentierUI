import tkinter
import os
from tkinter import ttk
from tkinter import filedialog
import threading
import speech_recognition


class transWindow(tkinter.Toplevel): 
    
    def __init__(self,menu,master):
        super().__init__()

        self.title("Segmentieren...")
        
        self.geometry("500x200")
        self.minsize(500,250)
        self.resizable(False, False)
        
        self.__inside(menu,master)

        self.protocol('WM_DELETE_WINDOW', lambda: self.__closeWindow(menu,master)) #überschreiben, des xButtons wenn das TopLvl Fenster verlassen wird
        

    
    def __inside(self,menu,master):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=1)

        self.icon_file=tkinter.PhotoImage(file=os.path.dirname(os.path.abspath(__file__)) +r'\icons\folder.png')

        self.entryLabel = tkinter.Label(self, text="Eingabe Pfad:")
        self.entryField = tkinter.Entry(self)
        self.entryButton = tkinter.Button(self,image=self.icon_file, command=lambda: self.__openPath(self.entryField))

        self.outroLabel = tkinter.Label(self, text="Ausgabe Pfad:")
        self.outroField = tkinter.Entry(self)
        self.outroButton = tkinter.Button(self,image=self.icon_file, command=lambda: self.__openPath(self.outroField))

        self.ambient = tkinter.IntVar()
        self.ambientNoise = tkinter.Radiobutton(self, text="Ambient Noise Filtern",variable=self.ambient,value=1)

        self.startButton = tkinter.Button(self, text="Transkribieren", command=lambda: threading.Thread(target=self.__transkribieren, args=(self.entryField.get(),self.outroField.get())).start())

        self.progressBar = ttk.Progressbar(self, orient=tkinter.HORIZONTAL,length=200,mode='determinate')
        self.progressLabel = tkinter.Label(self, text="")


        self.entryLabel.grid(row=0, column=0, sticky='e', padx=(0,2), pady=(20,1))
        self.entryField.grid(row=0, column=1, sticky='we', pady=(20,1))
        self.entryButton.grid(row=0, column=2, pady=(20,1))

        self.outroLabel.grid(row=1, column=0, sticky='e', padx=(0,2), pady=(20,1))
        self.outroField.grid(row=1, column=1, sticky='we', pady=(20,1))
        self.outroButton.grid(row=1, column=2, pady=(20,1))

        self.startButton.grid(row=2,column=2,pady=(20,1))

        self.progressBar.grid(row=3,column=1,pady=(20,1))
        self.progressLabel.grid(row=4,column=1,pady=(20,1))
        self.progressBar.grid_remove()

    def __openPath(self, entry):
        op = filedialog.askdirectory()
        if op != '' :
            entry.delete(0,tkinter.END)
            op = op +"/"
            entry.insert(0,op)
        #TopLevel Window wieder in den Vordergrund heben, weil sonst das Main window vorne steht
        self.lift()


    def __transkribieren(self,folderpath,outputfilepath):
        #progress bar wieder auf 0 setzen
        self.progressBar['value'] = 0
        #startbutton disabeln, damit nicht erneut gestartet werden kann
        self.startButton.config(state=tkinter.DISABLED)
        self.ambientNoise.config(state=tkinter.DISABLED)
        try:
            if os.path.isdir(folderpath) and os.path.isdir(outputfilepath):

                self.progressLabel.config(text="In Arbeit")

                #for file in os.listdir(folderpath):
                 #   self.__to_wav(folderpath+file)

                count = 0
                for file in os.listdir(folderpath):
                    try:
                        if str(file.split('.')[1]) == 'wav': #nur wav dateien
                            count+=1
                    except Exception as e:
                        print(file)
                        print("trans_window hat nicht geklappt. [1]")
                        print(e)

                #setze die Progressbar
                self.progressBar.grid()
                
                recognizer = speech_recognition.Recognizer()
                for file in os.listdir(folderpath):
                    try:
                        if file.split('.')[1] == 'wav': #nur wav dateien
                            with speech_recognition.AudioFile(folderpath+file) as source:
                                if self.ambient == 1:
                                    recognizer.adjust_for_ambient_noise(source)
                                # listen for the data (load audio to memory)
                                audio_data = recognizer.record(source)
                                # recognize (convert from speech to text)
                                text = recognizer.recognize_google(audio_data, language='de-DE')
                                
                                datei = open(outputfilepath+file.split('.wav')[0]+'.txt', 'w',encoding="utf-8")
                                datei.write(text)
                                datei.close()


                            self.progressBar['value'] += (200/count)
                            self.update_idletasks()
                    except Exception as e:
                        print(file)
                        print("trans_window hat nicht geklappt. [2.2]")
                        print(e)
                self.progressLabel.config(text="Fertig!")

            else:
                self.progressLabel.config(text="Einer der angegebenen Pfade existiert nicht!")
        except Exception as e:
            print(file)
            print("trans_window hat nicht geklappt. [3]")
            print(e)
        #start button wieder auswählbar
        self.startButton.config(state=tkinter.NORMAL)
        self.ambientNoise.config(state=tkinter.NORMAL)


     #overwrite für das schliesen des fensters
    def __closeWindow(self,menu,master):
        self.destroy() #normal destroy
        master.menubar.transmenu.transwindow = None #damit ein neues searchwindow erstellt werden kann
        