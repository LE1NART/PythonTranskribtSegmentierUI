from statistics import mode
from time import sleep
import tkinter
from tkinter import ttk
from tkinter import filedialog
import os
import re
import threading

class segWindow(tkinter.Toplevel):
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

        self.startButton = tkinter.Button(self, text="Segmentieren", command=lambda: threading.Thread(target=self.__segmentieren, args=(self.entryField.get(),self.outroField.get())).start())

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

    #wird im neuen Thread gestartet, siehe command beim Button
    def __segmentieren (self,folderpath, outputfilepath):
        #progress bar wieder auf 0 setzen
        self.progressBar['value'] = 0
        #startbutton disabeln, damit nicht erneut gestartet werden kann
        self.startButton.config(state=tkinter.DISABLED)

        #checkn ob die paths die gegeben sind wirklich valide paths sind
        if os.path.isdir(folderpath) and os.path.isdir(outputfilepath):

            self.progressLabel.config(text="In Arbeit")

            liste = ["a." , "a." , "a.A." , "a.a.O." , "a.a.S." , "a.D." , "a.d." , "A.d.Hrsg." , "A.d.Ü." , "a.G." , "a.gl.O." , "a.n.g." , "a.S." , "Abb." , "Abf." , "Abg." , "abg." , "Abh." , "Abk." , "abk." , "Abs." , "Abw." , "Abz." , "Adir." , "Adj." , "adj." , "Adr." , "Adv." , "adv." , "Afr." , "Ag." , "agg." , "Aggr." , "Ahg." ",Anh." , "Akad." , "akad." , "Akk." , "Alg." , "allg." , "alph." , "altgr." , "Am." , "Amp." , "amtl." , "Amtsbl." , "An." , "anat." , "anerk." , "Anf." , "Anfr." , "Ang." , "angekl." , "Angel." , "Angest." , "angew." , "Ank." , "Anl." , "anl." , "Anm." , "Ann." , "ann." , "anon." , "Anord." , "Anp." , "ANr." , "Ans." , "Ansch.-K." , "Ansch." , "anschl." , "Anschr." , "Anspr." , "Antiq." , "Antr." , "Antw." , "Anw.-L." , "Anz." , "Apart." , "apl." , "App." , "Apr." , "apr." , "Aq." , "Arbf." , "Arbg." , "Arbn.","ArbN" , "Arch." , "arr." , "Art.","Artt." , "Art.-Nr." , "Asp." , "Ass." , "Assist." , "ASt." , "Astrol." , "astron." , "asym." , "asymp." , "At." , "Atl." , "Atm." , "Attr." , "Aufb.","Aufbew." , "Aufg." , "Aufkl." , "Aufl." , "Ausg." , "ausschl." , "Az." , "Änd." , "Äq." , "ärztl." , "ästh." , "äth." , "b." , "b.w." , "Ba." , "Bd.","Bde." , "beil." , "bes." , "Best.-Nr." , "Betr." , "bez." , "Bez." , "Bhf." , "Bil." , "Bl." , "brosch." , "Bsp." , "Bspw." ,"bspw." , "bzgl." , "bzw." , "Bzw.", "c.t." , "ca." , "d.Ä." , "d.Gr." , "d.h." , "d.i." , "d.J." , "d.M." , "d.O." , "d.R." , "d.U." , "d.Vf." , "DDr." , "desgl." , "dgl." , "Dipl." , "Dr." , "Dr.-Ing." , "Dr.jur." , "Dr.med." , "Dr.med.dent." , "Dr.med.vet." , "Dr.phil." , "Dr.rer.nat." , "Dr.rer.pol." , "Dr.theol." , "Dres." , "Ph.D." , "dt.","dtsch." , "dto." , "Dtz.","Dtzd." , "e.h." , "e.V." , "ebd." , "Ed." , "ehem." , "eig.", "eigtl." , "einschl." , "entspr." , "erg." , "etal." , "etc." , "etc.pp." , "ev." , "evtl." , "exkl." , "Expl." , "Exz.", "f." , "f.d.R." , "Fa." , "Fam." , "ff." , "Forts." , "Fr." , "frdl." , "Frhr." , "Frl." , "frz." , "Gbf." , "geb." , "Gebr." , "gegr." , "geh." , "gek." , "Ges." , "ges.gesch." , "gesch." , "Geschw." , "gest." , "Gew." , "gez." , "ggf." , "Hbf." , "hg." , "hL." , "hl." , "Hr(n)." , "Hrsg." , "Hs." , "i.a.","i.allg." , "i.A.","i.Allg." , "i.A." , "i.d.R." , "i. e." , "i.e.S." , "i. H. v." , "i.J." , "i.R." , "i.S." , "i.V." , "i.W." , "i.w.S." , "i.Z.m." , "id." , "Ing." , "Inh." , "inkl." , "Jb." , "Jg." , "Jh." , "Jkr." , "jr.","jun." , "Kap." , "kart." , "kath." , "Kfm." , "kfm." , "kgl." , "Kl." , "Komp." , "Kr." , "Kto." , "led." , "lfd." , "lfd.m." , "lfd.Nr." , "Lfg.","Lfrg." , "lt." , "Ltn." , "luth." , "m.A.n." , "m.a.W." , "m.E." , "m.W." , "math." , "m.d.B." , "Min." , "Mio.","Mill." , "möbl." , "Mrd.","Md.","Mia." , "Ms.","Mskr." , "mtl." , "MwSt." , "Mz." , "Nachf.","Nchf." , "n.Chr." , "n.J." , "n.M." , "N.N." , "nachm." , "Nds." , "Nr.","No." , "Nrn.","Nos." , "o." , "o.Ä." , "o.B." , "o.B.d.A.","oBdA" , "o.J." , "o.P." , "Obb." , "op." , "p.A." , "Pf." , "Pfd." , "pp.","ppa." , "Pfr." , "Pkt." , "Prof." , "Prov." , "ps." , "q.e.d." , "r.-k.","rk." , "rd." , "Reg.-Bez." , "Rel." , "resp." , "Rhh." , "Rhld." , "S." , "s.a." , "s.d." , "s.o." , "s.t." , "s.u." , "s.Z." , "Sa." , "sen." , "spez." , "Spk." , "sog." , "spec." , "St.","Skt." , "St.","Std." , "Str." , "stud." , "svw.","s.v.w." , "Tel." , "Tsd." , "u.A.w.g." , "u." , "u.a." , "u.a.m." , "u.Ä." , "u.d.M." , "u.dgl.(m.)" , "u.E." , "u.U." , "u.ü.V." , "u.v.a." , "u.v.m." , "u.W." , "ü.d.M." , "Univ.-Prof." , "urspr." , "usf.","u.s.f." , "usw.","u.s.w." , "v." , "V." , "v.a." , "v.Chr." , "v.g.u." , "v.H." , "v.J." ,"vl.", "vll.", "vlt.", "vllt.", "v.M." , "v.T." , "Verf.","Vf." , "verh." , "Verl." , "Vers." , "vers." , "verw." , "vgl." , "vorm." , "Vors." , "w.o." , "Wwe." , "Wwr." , "Wz." , "z.B." ,"zB.", "z.d.A." , "z.H.","z.Hd." , "z.K.","z.Kts." , "z.S." , "z.T." , "zz.","zzt." , "zz." , "z.Z.","z.Zt." , "Ztg." , "Ztr." , "Ztschr." , "zus." , "zw." , "zzgl."]
        

            #count die Anzahl der zu segmentierenden Files, damit wir eine Progressbar erzeugen können
            count = 0
            for file in os.listdir(folderpath):
                try:
                    if str(file.split('.')[1]) == 'txt': #nur txt dateien
                        count+=1
                except Exception as e:
                    print(file)
                    print("seg_window hat nicht geklappt. [1]")
                    print(e)
                    
            #setze die Progressbar
            self.progressBar.grid()

            for file in os.listdir(folderpath):
                try:
                    if file.split('.')[1] == 'txt': #nur txt dateien
                        datei = open(folderpath+'/'+file, 'r',encoding="utf-8")
                        text = datei.read()
                        datei.seek(0)
                        datei.close()
                        
                        text = text.replace("\r\n", " ")
                        text = text.replace("\n", " ")
                        text = text.replace("\r", " ")
                        
                        
                        text = text.replace(". ", ". \r")
                        text = text.replace(", " or ",", ", \r")
                        text = text.replace("? " or "?", "? \r")
                        text = text.replace("! " or "!", "! \r")
                        text = text.replace(": " or ":", ": \r")
                        
                        
                        # Für die Folgenden Ersätze nutzen wir re.sub, da wir damit raw Strings einlesen können.
                        # Dadurch können wir den Vorsatz \b dazu nehmen um sicher zu stellen, dass wir keine Teilwörter Teilen wie z.B. Bund -> B\n und
                        
                        text = re.sub(r"\bund ", "\rund ", text)
                        text = re.sub(r"\boder ","\roder ", text)
                        
                        for l in liste:
                            l1 = re.sub(r"\." ,"\."  , l) #wir ersetzen die "." durch "\." damit die im folgenden bei r"" nicht als alles gelesen werden sondern wirklich als punkte
                            #in der vorderen bedingungen muss \. sein, weil sonst wieder alles gelten kann und hinten schreiben wir es nicht in raw also steht da wirklich "\."
                            #wir hatten sonst das Problem das zb die Abkürzung b.w. die abkürzung bzw. ersetzt hat, weil in der liste der "." als jedes zeichen im Raw code gelten konnte
                            c1 = r"\b"+l1+" \r"
                            c2 = l+" "
                            text = re.sub(c1 , c2 , text) #r"{}".format(c1) da nicht einfach r c1 oder ähnliches

                        datei = open(outputfilepath+'/'+file, 'w',encoding="utf-8")
                        datei.write(text)
                        datei.close()
                        
                        self.progressBar['value'] += (200/count)
                        self.update_idletasks()
                except Exception as e:
                    print(file)
                    print("seg_window hat nicht geklappt. [2]")
                    print(e)
            self.progressLabel.config(text="Fertig!")
        #wenn einer der pfade nicht existiert
        else:
            self.progressLabel.config(text="Einer der angegebenen Pfade existiert nicht!")
        #start button wieder auswählbar
        self.startButton.config(state=tkinter.NORMAL)


    #overwrite für das schliesen des fensters
    def __closeWindow(self,menu,master):
        self.destroy() #normal destroy
        master.menubar.segmenu.segwindow = None #damit ein neues searchwindow erstellt werden kann
        