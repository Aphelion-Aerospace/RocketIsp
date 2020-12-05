#!/usr/bin/env python
# -*- coding: ascii -*-
from __future__ import print_function

# NOTICE... this file is generated by TkGridGUI.
# Any code or comments added by the user must be in designated areas ONLY.
# User additions will be lost if they are placed in code-generated areas.
# (i.e. Saving from TkGridGUI will over-write code-generated areas.)

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "imports"


from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

from tkinter.ttk import Combobox, Progressbar, Separator, Treeview, Notebook

from tkinter import *
from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, LabelFrame
from tkinter import Listbox, Message, Radiobutton, Spinbox, Text
from tkinter import OptionMenu
import tkinter.filedialog
from tkinter import _setit as set_command


# >>>>>>insert any user code below this comment for section "imports"
# Place any user import statements here
from rocketisp.gui.global_vars import fuelL, oxidizerL

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "top_of_init"

if sys.version_info < (3,):
    from tkSimpleDialog import Dialog
else:
    from tkinter.simpledialog import Dialog

class _Dialog(Dialog):
    # use dialogOptions dictionary to set any values in the dialog
    def __init__(self, parent, title = None, dialogOptions=None):
    
        self.dialogOptions = dialogOptions
        Dialog.__init__(self, parent, title)

class _propellants(_Dialog):

    def body(self, master):
        dialogframe = Frame(master, width=350, height=135)
        self.dialogframe = dialogframe
        dialogframe.pack()


        self.make_Combobox_1( self.dialogframe )       #    Combobox: Oxidizer : at Main(3,1)
        self.make_Combobox_2( self.dialogframe )       #    Combobox: Fuel : at Main(3,2)
        self.make_Label_1( self.dialogframe )          #       Label: Oxidizer : at Main(2,1)
        self.make_Label_2( self.dialogframe )          #       Label: Fuel : at Main(2,2)
        self.make_Label_3( self.dialogframe )          #       Label: Select Oxidizer and Fuel : at Main(1,1)
        self.make_Label_4( self.dialogframe )          #       Label:  at Main(0,1)
        self.make_Label_5( self.dialogframe )          #       Label:  at Main(2,0)
        self.make_Label_6( self.dialogframe )          #       Label:  at Main(2,3)


        # >>>>>>insert any user code below this comment for section "top_of_init"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Combobox_1"
    def make_Combobox_1(self, frame):
        """    Combobox: Oxidizer : at Main(3,1)"""
        self.Combobox_1 = Combobox( frame , values="Mine Yours Ours", text="Oxidizer")
        self.Combobox_1.grid(row=3, column=1)
        self.Combobox_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Combobox_1"
        
        self.Combobox_1.configure( values=' '.join(oxidizerL) )

        self.Combobox_1.configure(textvariable=self.Combobox_1_StringVar)
        self.Combobox_1_StringVar.set( self.dialogOptions['oxName'] )
        self.Combobox_1_StringVar_traceName = self.Combobox_1_StringVar.trace_variable("w", self.Combobox_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Combobox_2"
    def make_Combobox_2(self, frame):
        """    Combobox: Fuel : at Main(3,2)"""
        self.Combobox_2 = Combobox( frame , values="Mine Yours Ours", text="Fuel")
        self.Combobox_2.grid(row=3, column=2)
        self.Combobox_2_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Combobox_2"
        self.Combobox_2.configure( values=' '.join(fuelL) )

        self.Combobox_2.configure(textvariable=self.Combobox_2_StringVar)
        self.Combobox_2_StringVar.set( self.dialogOptions['fuelName'] )
        self.Combobox_2_StringVar_traceName = self.Combobox_2_StringVar.trace_variable("w", self.Combobox_2_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_1"
    def make_Label_1(self, frame):
        """       Label: Oxidizer : at Main(2,1)"""
        self.Label_1 = Label( frame , text="Oxidizer", width="15")
        self.Label_1.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Label_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_2"
    def make_Label_2(self, frame):
        """       Label: Fuel : at Main(2,2)"""
        self.Label_2 = Label( frame , text="Fuel", width="15")
        self.Label_2.grid(row=2, column=2)

        # >>>>>>insert any user code below this comment for section "make_Label_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_3"
    def make_Label_3(self, frame):
        """       Label: Select Oxidizer and Fuel : at Main(1,1)"""
        self.Label_3 = Label( frame , text="Select Oxidizer and Fuel", width="30")
        self.Label_3.grid(row=1, column=1, columnspan="2")

        # >>>>>>insert any user code below this comment for section "make_Label_3"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_4"
    def make_Label_4(self, frame):
        """       Label:  at Main(0,1)"""
        self.Label_4 = Label( frame , text="", width="15", height="2")
        self.Label_4.grid(row=0, column=1)

        # >>>>>>insert any user code below this comment for section "make_Label_4"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_5"
    def make_Label_5(self, frame):
        """       Label:  at Main(2,0)"""
        self.Label_5 = Label( frame , text="", width="8")
        self.Label_5.grid(row=2, column=0)

        # >>>>>>insert any user code below this comment for section "make_Label_5"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_6"
    def make_Label_6(self, frame):
        """       Label:  at Main(2,3)"""
        self.Label_6 = Label( frame , text="", width="8")
        self.Label_6.grid(row=2, column=3)

        # >>>>>>insert any user code below this comment for section "make_Label_6"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Combobox_1_StringVar_traceName"
    def Combobox_1_StringVar_Callback(self, varName, index, mode):
        """    Combobox: Oxidizer : at Main(3,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "Combobox_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Combobox_1_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Combobox_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Combobox_2_StringVar_traceName"
    def Combobox_2_StringVar_Callback(self, varName, index, mode):
        """    Combobox: Fuel : at Main(3,2)"""
        pass

        # >>>>>>insert any user code below this comment for section "Combobox_2_StringVar_traceName"
        # replace, delete, or comment-out the following
        print( "Combobox_2_StringVar_Callback varName, index, mode",varName, index, mode )
        print( "    new StringVar value =",self.Combobox_2_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "dialog_validate"
    def validate(self):
        self.result = {} # return a dictionary of results
    

        #self.result["Combobox_1"] = self.Combobox_1_StringVar.get()
        #self.result["Combobox_2"] = self.Combobox_2_StringVar.get()

        # >>>>>>insert any user code below this comment for section "dialog_validate"
        # set values in "self.result" dictionary for return
        # for example...
        # self.result["age"] = self.Entry_2_StringVar.get() 
        self.result["oxName"] = self.Combobox_1_StringVar.get()
        self.result["fuelName"] = self.Combobox_2_StringVar.get()

        """
    # for testing, reinstate this code below
        dialog = _propellants(self.master, "Propellants Dialog", 
                 dialogOptions={'oxName':'LOX', 'fuelName':'MMH'})

        """        

        #self.result["test"] = "test message" 
        return 1
# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"


    def apply(self):
        pass
        #print( 'apply called' )

class _Testdialog:
    def __init__(self, master):
        frame = Frame(master, width=300, height=300)
        frame.pack()
        self.master = master
        self.x, self.y, self.w, self.h = -1,-1,-1,-1
        
        self.Button_1 = Button(text="Test Dialog", relief="raised", width="15")
        self.Button_1.place(x=84, y=36)
        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    def Button_1_Click(self, event): #click method for component ID=1
        dialog = _propellants(self.master, "Propellants Dialog", 
                 dialogOptions={'oxName':'LOX', 'fuelName':'MMH'})
        print( '===============Result from Dialog====================' )
        print( dialog.result )
        print( '=====================================================' )

def main():
    root = Tk()
    app = _Testdialog(root)
    root.mainloop()

if __name__ == '__main__':
    main()
