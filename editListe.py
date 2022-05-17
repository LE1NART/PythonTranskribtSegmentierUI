import tkinter

class EditableListbox(tkinter.Listbox):
    """A listbox where you can directly edit an item via double-click"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs,selectmode=tkinter.SINGLE)
        self.edit_item = None
        self.bind("<Double-1>", self._start_edit)

    def _start_edit(self, event):
        index = self.index(f"@{event.x},{event.y}")
        self.start_edit(index)
        return "break"

    def start_edit(self, index):
        self.edit_item = index
        text = self.get(index)
        y0 = self.bbox(index)[1]
        entry = tkinter.Entry(self, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", self.accept_edit)
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0, y=y0, relwidth=1, width=-1)
        entry.focus_set()
        entry.grab_set()

    def cancel_edit(self, event):
        event.widget.destroy()

    def accept_edit(self, event):
        new_data = event.widget.get()
        self.delete(self.edit_item)
        self.insert(self.edit_item, new_data)
        event.widget.destroy()

class topListe(tkinter.Toplevel):
    def __init__(self,parent, **kwargs):
        super().__init__(parent,**kwargs)

        self.protocol('WM_DELETE_WINDOW', lambda: self.__closeWindow(parent))

        self.lb = EditableListbox(self)
        sb = tkinter.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=sb.set)

        sb.pack(side='right', fill='y')
        self.lb.pack(side='left',fill='both',expand=True)

        with open("seg.txt") as f:
            lines = f.read().splitlines() 
        
        for line in lines:
            self.lb.insert("end",line)

        self.menu = tkinter.Menu(self)
        self.menucas = tkinter.Menu(self.menu,tearoff=0)
        self.menucas.add_command(label="Hinzufügen", command=lambda: self.__add(self.lb.curselection()))
        self.menucas.add_command(label="Löschen", command=lambda: self.__delete(self.lb.curselection()))
        self.menucas.add_command(label="Standard wiederherstellen", command=lambda:self.__default())

        self.menu.add_cascade(label="Bearbeiten", menu=self.menucas)

        self.config(menu=self.menu)
    
    def __add(self,select):
        if select:
            self.lb.insert(select[0]+1,"NEW")
        else:
            self.lb.insert(tkinter.END,"NEW")

    def __delete(self,select):
        if select:
            self.lb.delete(select[0])
        else:
            pass

    def __default(self):
        with open("segDefault.txt") as f:
            lines = f.read().splitlines() 

        with open('seg.txt','w') as f:
            for lin in lines:
                f.write(lin+"\n")
                
        self.lb.delete(0,tkinter.END)

        for line in lines:
            self.lb.insert("end",line)

    def __closeWindow(self,parent):
        with open('seg.txt','w') as f:
            for lin in self.lb.get(0,'end'):
                f.write(lin+"\n")

        parent.liste = None

        self.destroy() #normal destroy