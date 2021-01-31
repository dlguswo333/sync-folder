import tkinter as tk
import tkinter.font
import os
import os.path
from tkinter.filedialog import askdirectory
from threading import Thread
import base64
from core import sync_folder

class Terminal(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.path=""
        self.label=tk.Label(self, text="Path : ")
        self.label.pack(side="left")
        self.pathbox=tk.Entry(self, width=50, state="normal", textvariable=str, font="Calibri 11")
        self.pathbox.pack(side="left", padx=5, ipady=5, expand=True)
        self.pathbutton=tk.Button(self, text="Set Path", command=self.set_path)
        self.pathbutton.pack(side="left", padx=10, anchor="n")


    def set_path(self):
        self.path=tk.filedialog.askdirectory()
        self.pathbox.config(state="normal")
        self.pathbox.delete(0, tk.END)
        self.pathbox.insert(0, self.path)
    
    def get_path(self):
        return self.pathbox.get()

class Top(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        if os.path.exists('sync_folder.ico'):
            self.iconbitmap('sync_folder.ico')
        self.title('Sync Folder')
        self.a_terminal=Terminal(self)
        self.b_terminal=Terminal(self)
        self.resizable(False, False)
        self.labeltext=tk.StringVar()
        self.labeltext.set('Hello!')


        # Change default font config.
        font=tk.font.nametofont("TkDefaultFont")
        font.configure(family="Calibri", size=11)

        self.a_terminal.pack(side="top", pady=5, anchor="n", expand=True)
        self.b_terminal.pack(side="top", pady=5, anchor="n", expand=True)

        self.frame=tk.Frame(self)
        self.frame.pack(side="bottom", fill="both", pady=5, expand=True)

        self.label=tk.Label(self.frame, textvariable=self.labeltext)
        self.label.pack(side="left", anchor="w", expand=True)

        self.syncbutton=tk.Button(self.frame, text="Synchronize", command=lambda :self.sync())
        self.syncbutton.pack(side="right", anchor="e", padx=10, expand=True)

        self.mainloop()

    def sync(self):
        if not self.a_terminal.get_path() or not self.b_terminal.get_path():
            # Do not synchronize if any of paths is empty.
            self.labeltext.set('Set path First!')
            return
        self.syncbutton["state"]="disabled"
        t=Thread(target=self.inner_sync)
        t.start()

    def inner_sync(self):
        # This innter method will make it easy with multithreading...
        self.labeltext.set('0 files copied')
        result={"labeltext":self.labeltext, "num_files":0, "num_failed":0}
        sync_folder(self.a_terminal.get_path(), self.b_terminal.get_path(), True, result)
        self.syncbutton["state"]="normal"

if __name__=="__main__":
    Top()
