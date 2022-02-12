import tkinter
import seg_window

import os
import re

class segmenu(tkinter.Menu):
   def __init__(self,menu,master):
      super().__init__(menu, tearoff=0)
        
      self.liste = ["a." , "a." , "a.A." , "a.a.O." , "a.a.S." , "a.D." , "a.d." , "A.d.Hrsg." , "A.d.Ü." , "a.G." , "a.gl.O." , "a.n.g." , "a.S." , "Abb." , "Abf." , "Abg." , "abg." , "Abh." , "Abk." , "abk." , "Abs." , "Abw." , "Abz." , "Adir." , "Adj." , "adj." , "Adr." , "Adv." , "adv." , "Afr." , "Ag." , "agg." , "Aggr." , "Ahg." ",Anh." , "Akad." , "akad." , "Akk." , "Alg." , "allg." , "alph." , "altgr." , "Am." , "Amp." , "amtl." , "Amtsbl." , "An." , "anat." , "anerk." , "Anf." , "Anfr." , "Ang." , "angekl." , "Angel." , "Angest." , "angew." , "Ank." , "Anl." , "anl." , "Anm." , "Ann." , "ann." , "anon." , "Anord." , "Anp." , "ANr." , "Ans." , "Ansch.-K." , "Ansch." , "anschl." , "Anschr." , "Anspr." , "Antiq." , "Antr." , "Antw." , "Anw.-L." , "Anz." , "Apart." , "apl." , "App." , "Apr." , "apr." , "Aq." , "Arbf." , "Arbg." , "Arbn.","ArbN" , "Arch." , "arr." , "Art.","Artt." , "Art.-Nr." , "Asp." , "Ass." , "Assist." , "ASt." , "Astrol." , "astron." , "asym." , "asymp." , "At." , "Atl." , "Atm." , "Attr." , "Aufb.","Aufbew." , "Aufg." , "Aufkl." , "Aufl." , "Ausg." , "ausschl." , "Az." , "Änd." , "Äq." , "ärztl." , "ästh." , "äth." , "b." , "b.w." , "Ba." , "Bd.","Bde." , "beil." , "bes." , "Best.-Nr." , "Betr." , "bez." , "Bez." , "Bhf." , "Bil." , "Bl." , "brosch." , "Bsp." , "Bspw." ,"bspw." , "bzgl." , "bzw." , "Bzw.", "c.t." , "ca." , "d.Ä." , "d.Gr." , "d.h." , "d.i." , "d.J." , "d.M." , "d.O." , "d.R." , "d.U." , "d.Vf." , "DDr." , "desgl." , "dgl." , "Dipl." , "Dr." , "Dr.-Ing." , "Dr.jur." , "Dr.med." , "Dr.med.dent." , "Dr.med.vet." , "Dr.phil." , "Dr.rer.nat." , "Dr.rer.pol." , "Dr.theol." , "Dres." , "Ph.D." , "dt.","dtsch." , "dto." , "Dtz.","Dtzd." , "e.h." , "e.V." , "ebd." , "Ed." , "ehem." , "eig.", "eigtl." , "einschl." , "entspr." , "erg." , "etal." , "etc." , "etc.pp." , "ev." , "evtl." , "exkl." , "Expl." , "Exz.", "f." , "f.d.R." , "Fa." , "Fam." , "ff." , "Forts." , "Fr." , "frdl." , "Frhr." , "Frl." , "frz." , "Gbf." , "geb." , "Gebr." , "gegr." , "geh." , "gek." , "Ges." , "ges.gesch." , "gesch." , "Geschw." , "gest." , "Gew." , "gez." , "ggf." , "Hbf." , "hg." , "hL." , "hl." , "Hr(n)." , "Hrsg." , "Hs." , "i.a.","i.allg." , "i.A.","i.Allg." , "i.A." , "i.d.R." , "i. e." , "i.e.S." , "i. H. v." , "i.J." , "i.R." , "i.S." , "i.V." , "i.W." , "i.w.S." , "i.Z.m." , "id." , "Ing." , "Inh." , "inkl." , "Jb." , "Jg." , "Jh." , "Jkr." , "jr.","jun." , "Kap." , "kart." , "kath." , "Kfm." , "kfm." , "kgl." , "Kl." , "Komp." , "Kr." , "Kto." , "led." , "lfd." , "lfd.m." , "lfd.Nr." , "Lfg.","Lfrg." , "lt." , "Ltn." , "luth." , "m.A.n." , "m.a.W." , "m.E." , "m.W." , "math." , "m.d.B." , "Min." , "Mio.","Mill." , "möbl." , "Mrd.","Md.","Mia." , "Ms.","Mskr." , "mtl." , "MwSt." , "Mz." , "Nachf.","Nchf." , "n.Chr." , "n.J." , "n.M." , "N.N." , "nachm." , "Nds." , "Nr.","No." , "Nrn.","Nos." , "o." , "o.Ä." , "o.B." , "o.B.d.A.","oBdA" , "o.J." , "o.P." , "Obb." , "op." , "p.A." , "Pf." , "Pfd." , "pp.","ppa." , "Pfr." , "Pkt." , "Prof." , "Prov." , "ps." , "q.e.d." , "r.-k.","rk." , "rd." , "Reg.-Bez." , "Rel." , "resp." , "Rhh." , "Rhld." , "S." , "s.a." , "s.d." , "s.o." , "s.t." , "s.u." , "s.Z." , "Sa." , "sen." , "spez." , "Spk." , "sog." , "spec." , "St.","Skt." , "St.","Std." , "Str." , "stud." , "svw.","s.v.w." , "Tel." , "Tsd." , "u.A.w.g." , "u." , "u.a." , "u.a.m." , "u.Ä." , "u.d.M." , "u.dgl.(m.)" , "u.E." , "u.U." , "u.ü.V." , "u.v.a." , "u.v.m." , "u.W." , "ü.d.M." , "Univ.-Prof." , "urspr." , "usf.","u.s.f." , "usw.","u.s.w." , "v." , "V." , "v.a." , "v.Chr." , "v.g.u." , "v.H." , "v.J." ,"vl.", "vll.", "vlt.", "vllt.", "v.M." , "v.T." , "Verf.","Vf." , "verh." , "Verl." , "Vers." , "vers." , "verw." , "vgl." , "vorm." , "Vors." , "w.o." , "Wwe." , "Wwr." , "Wz." , "z.B." ,"zB.", "z.d.A." , "z.H.","z.Hd." , "z.K.","z.Kts." , "z.S." , "z.T." , "zz.","zzt." , "zz." , "z.Z.","z.Zt." , "Ztg." , "Ztr." , "Ztschr." , "zus." , "zw." , "zzgl."]
        
      #adding commands to the segmentation menu
      self.add_command(label="Einzeltext",command=lambda: self.__segment(menu,master))
      self.add_command(label="Multitext",command=lambda: self.create_segWindow(menu,master))

      self.segwindow = None


   def create_segWindow(self,menu,master):
      if self.segwindow: #wenn ein fenster existiert
            self.segwindow.lift() #wird es in den vordergrund gerufen
      else: #wenn nicht wir
            self.segwindow = seg_window.segWindow(menu,master)

   def __segment(self,menu,master):
      try: #try block für generelle fehler
         if tkinter.messagebox.askokcancel(title="Info", message="Der Text muss zwischen gespeichert werden. Wollen sie Fortfahren?"):
            if menu.filemenu.saveFile(master):
         
               status = master.statusbar.status.cget("text").split("Saved: ").pop().replace('/','\\')

               datei = open(status, 'r',encoding="utf-8")
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
               
               liste = ["a." , "a." , "a.A." , "a.a.O." , "a.a.S." , "a.D." , "a.d." , "A.d.Hrsg." , "A.d.Ü." , "a.G." , "a.gl.O." , "a.n.g." , "a.S." , "Abb." , "Abf." , "Abg." , "abg." , "Abh." , "Abk." , "abk." , "Abs." , "Abw." , "Abz." , "Adir." , "Adj." , "adj." , "Adr." , "Adv." , "adv." , "Afr." , "Ag." , "agg." , "Aggr." , "Ahg." ",Anh." , "Akad." , "akad." , "Akk." , "Alg." , "allg." , "alph." , "altgr." , "Am." , "Amp." , "amtl." , "Amtsbl." , "An." , "anat." , "anerk." , "Anf." , "Anfr." , "Ang." , "angekl." , "Angel." , "Angest." , "angew." , "Ank." , "Anl." , "anl." , "Anm." , "Ann." , "ann." , "anon." , "Anord." , "Anp." , "ANr." , "Ans." , "Ansch.-K." , "Ansch." , "anschl." , "Anschr." , "Anspr." , "Antiq." , "Antr." , "Antw." , "Anw.-L." , "Anz." , "Apart." , "apl." , "App." , "Apr." , "apr." , "Aq." , "Arbf." , "Arbg." , "Arbn.","ArbN" , "Arch." , "arr." , "Art.","Artt." , "Art.-Nr." , "Asp." , "Ass." , "Assist." , "ASt." , "Astrol." , "astron." , "asym." , "asymp." , "At." , "Atl." , "Atm." , "Attr." , "Aufb.","Aufbew." , "Aufg." , "Aufkl." , "Aufl." , "Ausg." , "ausschl." , "Az." , "Änd." , "Äq." , "ärztl." , "ästh." , "äth." , "b." , "b.w." , "Ba." , "Bd.","Bde." , "beil." , "bes." , "Best.-Nr." , "Betr." , "bez." , "Bez." , "Bhf." , "Bil." , "Bl." , "brosch." , "Bsp." , "Bspw." ,"bspw." , "bzgl." , "bzw." , "Bzw.", "c.t." , "ca." , "d.Ä." , "d.Gr." , "d.h." , "d.i." , "d.J." , "d.M." , "d.O." , "d.R." , "d.U." , "d.Vf." , "DDr." , "desgl." , "dgl." , "Dipl." , "Dr." , "Dr.-Ing." , "Dr.jur." , "Dr.med." , "Dr.med.dent." , "Dr.med.vet." , "Dr.phil." , "Dr.rer.nat." , "Dr.rer.pol." , "Dr.theol." , "Dres." , "Ph.D." , "dt.","dtsch." , "dto." , "Dtz.","Dtzd." , "e.h." , "e.V." , "ebd." , "Ed." , "ehem." , "eig.", "eigtl." , "einschl." , "entspr." , "erg." , "etal." , "etc." , "etc.pp." , "ev." , "evtl." , "exkl." , "Expl." , "Exz.", "f." , "f.d.R." , "Fa." , "Fam." , "ff." , "Forts." , "Fr." , "frdl." , "Frhr." , "Frl." , "frz." , "Gbf." , "geb." , "Gebr." , "gegr." , "geh." , "gek." , "Ges." , "ges.gesch." , "gesch." , "Geschw." , "gest." , "Gew." , "gez." , "ggf." , "Hbf." , "hg." , "hL." , "hl." , "Hr(n)." , "Hrsg." , "Hs." , "i.a.","i.allg." , "i.A.","i.Allg." , "i.A." , "i.d.R." , "i. e." , "i.e.S." , "i. H. v." , "i.J." , "i.R." , "i.S." , "i.V." , "i.W." , "i.w.S." , "i.Z.m." , "id." , "Ing." , "Inh." , "inkl." , "Jb." , "Jg." , "Jh." , "Jkr." , "jr.","jun." , "Kap." , "kart." , "kath." , "Kfm." , "kfm." , "kgl." , "Kl." , "Komp." , "Kr." , "Kto." , "led." , "lfd." , "lfd.m." , "lfd.Nr." , "Lfg.","Lfrg." , "lt." , "Ltn." , "luth." , "m.A.n." , "m.a.W." , "m.E." , "m.W." , "math." , "m.d.B." , "Min." , "Mio.","Mill." , "möbl." , "Mrd.","Md.","Mia." , "Ms.","Mskr." , "mtl." , "MwSt." , "Mz." , "Nachf.","Nchf." , "n.Chr." , "n.J." , "n.M." , "N.N." , "nachm." , "Nds." , "Nr.","No." , "Nrn.","Nos." , "o." , "o.Ä." , "o.B." , "o.B.d.A.","oBdA" , "o.J." , "o.P." , "Obb." , "op." , "p.A." , "Pf." , "Pfd." , "pp.","ppa." , "Pfr." , "Pkt." , "Prof." , "Prov." , "ps." , "q.e.d." , "r.-k.","rk." , "rd." , "Reg.-Bez." , "Rel." , "resp." , "Rhh." , "Rhld." , "S." , "s.a." , "s.d." , "s.o." , "s.t." , "s.u." , "s.Z." , "Sa." , "sen." , "spez." , "Spk." , "sog." , "spec." , "St.","Skt." , "St.","Std." , "Str." , "stud." , "svw.","s.v.w." , "Tel." , "Tsd." , "u.A.w.g." , "u." , "u.a." , "u.a.m." , "u.Ä." , "u.d.M." , "u.dgl.(m.)" , "u.E." , "u.U." , "u.ü.V." , "u.v.a." , "u.v.m." , "u.W." , "ü.d.M." , "Univ.-Prof." , "urspr." , "usf.","u.s.f." , "usw.","u.s.w." , "v." , "V." , "v.a." , "v.Chr." , "v.g.u." , "v.H." , "v.J." ,"vl.", "vll.", "vlt.", "vllt.", "v.M." , "v.T." , "Verf.","Vf." , "verh." , "Verl." , "Vers." , "vers." , "verw." , "vgl." , "vorm." , "Vors." , "w.o." , "Wwe." , "Wwr." , "Wz." , "z.B." ,"zB.", "z.d.A." , "z.H.","z.Hd." , "z.K.","z.Kts." , "z.S." , "z.T." , "zz.","zzt." , "zz." , "z.Z.","z.Zt." , "Ztg." , "Ztr." , "Ztschr." , "zus." , "zw." , "zzgl."]

               for l in liste:
                     l1 = re.sub(r"\." ,"\."  , l) #wir ersetzen die "." durch "\." damit die im folgenden bei r"" nicht als alles gelesen werden sondern wirklich als punkte
                     #in der vorderen bedingungen muss \. sein, weil sonst wieder alles gelten kann und hinten schreiben wir es nicht in raw also steht da wirklich "\."
                     #wir hatten sonst das Problem das zb die Abkürzung b.w. die abkürzung bzw. ersetzt hat, weil in der liste der "." als jedes zeichen im Raw code gelten konnte
                     c1 = r"\b"+l1+" \r"
                     c2 = l+" "
                     text = re.sub(c1 , c2 , text) #r"{}".format(c1) da nicht einfach r c1 oder ähnliches
               #segmentierter text wieder in die datei schreiben
               datei = open(status, 'w',encoding="utf-8")
               datei.write(text)
               datei.close()


               #clear the textfield
               master.textfield.delete(1.0, tkinter.END)

               #anpassen des Titels und der Statusbar
               name = status.split("/").pop()
               master.title(f'{name} - Transkriptionseditor')
               master.statusbar.status.config(text=f'Saved: {status}')
               #kopieren des textes aus der datei wieder in das textfeld
               text_file = open(status, "r",encoding="utf-8")
               master.textfield.insert(1.0,text_file.read())
               text_file.close()           
            else: raise Exception

   
      except Exception as e:
         tkinter.messagebox.showwarning('warning', 'Beim Segmentieren ist ein unvorhergesehender Fehler aufgetreten.')
         print("Error in segMenu segmentieren: "+str(e))
      