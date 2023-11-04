from ..Backend.Playlist import playlist
from PyQt5 import QtWidgets, QtCore
import os

MEDIA_EXTENSIONS = ['.mp3', '.mp4', '.avi', '.mkv', '.mov', '.flv']

class menu_bar(QtWidgets.QMenuBar):
    
    # <--Signals-->
    open_file_signal = QtCore.pyqtSignal()
    
    
    def __init__(self, parent=None):
        #Create the menu bar
        super().__init__(parent)
        self.parent = parent
        self.setEnabled(True)
        self.setNativeMenuBar(False)
        self.setGeometry(0,0,700,30)
        self.playlist = playlist()
        
        # <-- Import icons over here -->
        
                
        #Create the various menu buttons
        file_menu = QtWidgets.QMenu("&File" ,self)
        edit_menu = QtWidgets.QMenu("&Edit" ,self)
        wp_menu = QtWidgets.QMenu("&WatchParty" ,self)
        help_menu = QtWidgets.QMenu("&Help" ,self)
        drive_menu = QtWidgets.QMenu("&Drive" ,self)
        
        #Adding the menu buttons
        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(wp_menu)
        self.addMenu(help_menu)
        self.addMenu(drive_menu)
        
        # Adding actions and submenus
        #File menu       
        add_action(file_menu, "&Open File", "Ctrl+O", "Open file", self.open_file)
        add_action(file_menu, "&Open Playlist", "Ctrl+Shift+O", "Open playlist", open_playlist)
        add_action(file_menu, "&Save", "Ctrl+S", "Save file with current name", save_file)
        add_action(file_menu, "Save As...", "Ctrl+Shift+S", "Save file as...", save_as)
        #Edit menu
        add_action(edit_menu, "Copy", "Ctrl+C", "Copy clip", copy_file)
        add_action(edit_menu, "Cut", "Ctrl+X", "Cut current clip", cut_file)
        add_action(edit_menu, "Paste", "Ctrl+V", "Paste clip from clipboard", paste_file)
        #WP menu
        add_action(wp_menu, "Join", "Ctrl+K", "Join an existing party", join_party)
        add_action(wp_menu, "Host", "Ctrl+L", "Host a new Watch-Party", host_party)
        #Drive menu
        # <-- Add functionality to display the current acount status -->
        add_action(drive_menu, "Import", "Ctrl-I", "Import directly from Google Drive", import_file)
        
    def open_file(self):
        global MEDIA_EXTENSIONS
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video")
        
        if filename is not None:
            #need to check if the file is of supported format
            playlist_t = playlist()
            playlist_t.add_file(filename)
        
        
      
def add_action(menu, name, shortcut, tip, func, icon=None):
    if icon is None:
        action = QtWidgets.QAction(name, menu)
    else:
        action = QtWidgets.QAction(icon, name, menu)
    action.setShortcut(shortcut)
    action.setStatusTip(tip)
    action.triggered.connect(func)
    menu.addAction(action)
    
#File menu functions

    
def open_playlist(self):
    pass
    # self.open_file_signal.emit("Hello darkness my old friend!")        

        
def save_file():
    pass 
        
def save_as():
    pass
   
#Editor functions     
def copy_file():
    pass

def cut_file():
    pass

def paste_file():
    pass        
        
#WP functions
def join_party():
    pass

def host_party():
    pass        
        
#Drive functions
def import_file():
    pass
        
        
        