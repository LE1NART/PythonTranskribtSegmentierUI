import tkinter
from tkinter import filedialog
from tkinter import *

import file_menu 
import trans_menu
import seg_menu
import search_menu
import edit_menu

import os

class menubar(tkinter.Menu):

    def __init__(self, master):
        super().__init__(master)
        
        #create all menus+submenus in their own functions
        self.__create_filemenu(master)
        self.__create_editmenu(master)
        self.__create_searchmenu(master)
        self.__create_segmenu(master)
        self.__create_transmenu(master)
        
       
        


    def __create_filemenu(self, master):
        #create the first submenu for "Datei"
        self.filemenu = file_menu.filemenu(self,master)
        self.add_cascade(label="Datei", menu=self.filemenu)
        
    def __create_editmenu(self, master):
        #create the edit menu
        self.editmenu = edit_menu.editmenu(self,master)
        self.add_cascade(label="Bearbeiten", menu=self.editmenu)
        
    def __create_searchmenu(self, master):
        #create the search menu
        self.searchmenu = search_menu.searchmenu(self,master)
        self.add_cascade(label="Suchen", menu=self.searchmenu)
       
        
    def __create_segmenu(self, master):
        #ceate the segmentation menu
        self.segmenu = seg_menu.segmenu(self,master)
        self.add_cascade(label="Segmentieren", menu=self.segmenu)
      
    
    
    def __create_transmenu(self, master):
        #creating the transcribtion menu
        self.transmenu = trans_menu.transmenu(self,master)
        self.add_cascade(label="Transkription", menu=self.transmenu)
        
       
        
    