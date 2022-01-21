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
        filemenu = file_menu.filemenu(self,master)
        self.add_cascade(label="Datei", menu=filemenu)
        
    def __create_editmenu(self, master):
        #create the edit menu
        editmenu = edit_menu.editmenu(self,master)
        self.add_cascade(label="Bearbeiten", menu=editmenu)
        
    def __create_searchmenu(self, master):
        #create the search menu
        searchmenu = search_menu.searchmenu(self,master)
        self.add_cascade(label="Suchen", menu=searchmenu)
       
        
    def __create_segmenu(self, master):
        #ceate the segmentation menu
        segmenu = seg_menu.segmenu(self,master)
        self.add_cascade(label="Segmentieren", menu=segmenu)
      
    
    
    def __create_transmenu(self, master):
        #creating the transcribtion menu
        transmenu = trans_menu.transmenu(self,master)
        self.add_cascade(label="Transkription", menu=transmenu)
        
       
        
    