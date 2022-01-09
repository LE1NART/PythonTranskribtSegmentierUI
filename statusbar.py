import tkinter

class statusbar(tkinter.Frame):
    
    def __init__(self,master):
        super().__init__(master)
        #create the Label which represent the status in the status bar
        
        
        self.status = tkinter.Label(self, text='Ready   ', anchor='e')
        self.status.pack(side='right')