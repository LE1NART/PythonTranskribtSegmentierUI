import tkinter
import seg_window
import opt_window
import segmentieren


class segmenu(tkinter.Menu):
   def __init__(self,menu,master):
      super().__init__(menu, tearoff=0)
                
      #adding commands to the segmentation menu
      self.add_command(label="Einzeltext",command=lambda: self.__segment(menu,master))
      self.add_command(label="Multitext",command=lambda: self.create_segWindow(menu,master))

      self.add_command(label="Einstellungen", command=lambda: self.create_optWindow(menu,master))

      self.segwindow = None
      self.optwindow = None


   def create_segWindow(self,menu,master):
      if self.segwindow: #wenn ein fenster existiert
            self.segwindow.lift() #wird es in den vordergrund gerufen
      else: #wenn nicht wir
         self.segwindow = seg_window.segWindow(menu,master)

   def create_optWindow(self,menu,master):
      if self.optwindow:
         self.optwindow.lift()
      else:
         self.optwindow = opt_window.optWindow(menu,master)

   def __segment(self,menu,master):
      try: #try block für generelle fehler
         if tkinter.messagebox.askokcancel(title="Info", message="Der Text muss zwischen gespeichert werden. Wollen sie Fortfahren?"):
            if menu.filemenu.saveFile(master):
         
               status = master.statusbar.status.cget("text").split("Saved: ").pop().replace('/','\\')
               
               segmentieren.segment(master,status,1)
               
            else: raise Exception

   
      except Exception as e:
         tkinter.messagebox.showwarning('warning', 'Beim Segmentieren ist ein unvorhergesehender Fehler aufgetreten.')
         print("Error in segMenu segmentieren: "+str(e))
      