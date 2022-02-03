import tkinter

#erstellt das Such Fenster, wir in search_menu aufgerufen
class searchWindow(tkinter.Toplevel):
    def __init__(self,menu,master):
        super().__init__()
        
        self.title("Suchen...")
        
        self.geometry("500x200")
        self.minsize(500,200)
        self.resizable(True, True)
        
        self.__inside(menu,master)
        
        self.liste = [] #liste um alle gefundenen übereinstimmungen zu speichern
        master.textfield.tag_configure("searchActive", background="yellow")
        master.textfield.tag_configure("search", background="lightgreen")
        
        self.protocol('WM_DELETE_WINDOW', lambda: self.__closeWindow(menu,master)) #überschreiben, des xButtons wenn das TopLvl Fenster verlassen wird
        
    
    #inside build all the widgets we need in the window
    def __inside(self,menu,master):
        #columnconfigure to build a better grid setup
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=2) 
        self.grid_columnconfigure(2, weight=1) 
        
        self.searchLabel = tkinter.Label(self, text="Suche nach:") #Label für den suche nach text
        self.searchField = tkinter.Entry(self) #Entry für das was gesucht werden soll
        #die drei button um das erste mal zu suchen, um weiter zu suchen und um zu zählen
        self.searchButton = tkinter.Button(self , text ="Suchen", command= lambda: self.startButton(master,True))
        self.nextButton = tkinter.Button(self , text ="Nächster", state=tkinter.DISABLED ,command= lambda: self.__next(master))
        self.countButton = tkinter.Button(self , text ="Zählen" ,command= lambda: self.__count(master))
        
        #variablen für die checkboxes
        self.wholeWord = tkinter.IntVar()
        self.upperLower = tkinter.IntVar()
        #checkbocen, ob Groß-/Kleinschreibung berücksichtigt werden soll und ob ganze Wörter gesucht werden sollen
        self.wholeWordCheckbox = tkinter.Checkbutton(self, text = "Nur ganze Wörter suchen", variable=self.wholeWord)
        self.upperLowerCheckbox = tkinter.Checkbutton(self, text = "Groß-/Kleinschreibung beachten", variable=self.upperLower)    
        
        #label für die Angabe des Count wertes
        self.countLabel = tkinter.Label(self, text="")
        
        #alles ins grid packen
        self.searchLabel.grid(row=0, column=0, sticky='e', padx=(0,2), pady=(20,1))
        self.searchField.grid(row=0, column=1, sticky='we', pady=(20,1))
        self.searchButton.grid(row=0, column=2, pady=(20,10))
        self.nextButton.grid(row=1,column=2, pady=(0,10))
        self.countButton.grid(row=2, column=2)
        self.wholeWordCheckbox.grid(row=2, column=1, sticky="w")
        self.upperLowerCheckbox.grid(row=3, column=1, sticky="w")
        self.countLabel.grid(row=4, column=0,columnspan=3, pady=(5,30),ipady=10, sticky="nwe")

    #funktion um das erste mal die suche zu starten, von hier aus gehen wir in die Rekursion über 
    def startButton(self,master,button=False):
        #bei neuer suche müssen alle vorherige tags entfernt werden
        master.textfield.tag_remove("searchActive",1.0,'end')
        master.textfield.tag_remove("search",1.0,'end')
        self.countLabel.config(text="")
        #liste wird ebenfalls geleert
        self.liste = []
        if self.searchField.get() != "":
            #erste mal suchen wird aufgerufen
            self.__search(master,1.0) 
            
            if self.liste != []:
                #im folgenden wird die Färbung der ergebnisse übernommen
                #erst alles in search colourn
                for f in self.liste:
                    start, ende = f
                    master.textfield.tag_add("search",start,ende)

                if button == True:
                    #erstes element wird in active gefärbt
                    start, ende = self.liste.pop(0)
                    self.liste.append((start,ende))
                    master.textfield.tag_remove("search",start,ende)
                    master.textfield.tag_add("searchActive",start,ende)
                    #setzen das erste gefundene in fokus
                    master.textfield.see(ende)
                    master.textfield.focus()
                    master.textfield.mark_unset("insert")
                    master.textfield.mark_set("insert", ende)
                
                #setzt den nextButton auf auswählbar
                self.nextButton.config(state=tkinter.NORMAL)
            else:
                self.countLabel.config(text=f"Es wurden {len(self.liste)} Übereinstimmungen gefunden.",font=("TkDefaultFont", 15))

        
        

    #die rekursive Funktion welche alles findet
    def __search(self, master, start):
        try: 
            #wenn das ganze wort gesucht wird, elif fall 
            if self.wholeWord.get() == 0:
                searchWord = self.searchField.get()
            elif self.wholeWord.get() == 1:
                searchWord = r"\y"+self.searchField.get()+"\y"   #fügen \y hinzu, um nur ganze wörter zu finden
            
            #großkleinschreibung wird ignoriert
            if self.upperLower.get() == 0:
                countVar = tkinter.IntVar() #länge des wortes
                pos = master.textfield.search(searchWord,start,'end', count=countVar, nocase=1,regexp=True) #startposition des gefundenen wortes
                try:    #wenn was gefunden wird müssen wir die länge auf den start punkt raufaddieren
                    row , col = pos.split('.')
                    ende = int(col) + countVar.get()
                    ende = row + '.' + str(ende)
                    self.liste.append((pos,ende)) #wird der liste hinzugefügt
                    
                    self.__search(master,ende) #rekusion
                except ValueError:
                    pass
                except Exception as e:
                    print("Error in search_window: "+str(e))
            #gleich wie if case nur nocase=0
            elif self.upperLower.get() == 1:
                countVar = tkinter.IntVar()
                pos = master.textfield.search(searchWord,start,'end', count=countVar,regexp=True)
                try:    
                    row , col = pos.split('.')
                    ende = int(col) + countVar.get()
                    ende = row + '.' + str(ende)
                    self.liste.append((pos,ende))
                    
                    self.__search(master,ende)
                except ValueError:
                    pass
                except Exception as e:
                    print("Error in search_window: "+str(e))
        except AttributeError:
            pass


    def __next(self,master):
        #remove from the old active the active Colour and add the search colour
        start, ende = self.liste.pop()
        self.liste.append((start,ende))
        master.textfield.tag_remove("searchActive",start,ende)
        master.textfield.tag_add("search",start,ende)
        
        #add to the next the active colour and remove the search colour
        start, ende = self.liste.pop(0)
        self.liste.append((start,ende))
        master.textfield.tag_remove("search",start,ende)
        master.textfield.tag_add("searchActive",start,ende)
        master.textfield.see(ende)
        master.textfield.focus()
        master.textfield.mark_unset("insert")
        master.textfield.mark_set("insert", ende)
        

    #wird nochmal gesucht, und dann die Länge der Liste ins countLabel geschrieben
    def __count(self,master):
        self.liste = []
        self.__search(master,1.0) 
       
       
        self.countLabel.config(text=f"Es wurden {len(self.liste)} Übereinstimmungen gefunden.",font=("TkDefaultFont", 15))
    
    
    #overwrite für das schliesen des fensters
    def __closeWindow(self,menu,master):
        self.destroy() #normal destroy
        master.menubar.searchmenu.searchwindow = None #damit ein neues searchwindow erstellt werden kann
        #alle tags werden gelöscht, damit keine markierung mehr da ist
        master.textfield.tag_delete("searchActive")
        master.textfield.tag_delete("search")