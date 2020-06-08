import tkinter as tk
import os
import os.path
import tkinter.filedialog

target_ext=[".jpg", ".jpeg", ".webp", ".txt"]

class Terminal:
    def __init__(self, pathbox):
        self.path=""
        self.pathbox=pathbox
    def set_path(self):
        self.path=tk.filedialog.askdirectory()
        self.pathbox.config(state="normal")
        self.pathbox.delete(0, tk.END)
        self.pathbox.insert(0, self.path)
        self.pathbox.config(state="disabled")
    def get_filenames(self):
        if not os.path.isdir(self.path):
            return False
        self.filenames=[name for name in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, name)) and os.path.splitext(name)[1] not in target_ext]        

if __name__=="__main__":
    mw=tk.Tk()
    mw.title="sync_folder"
    terminal=list()
    pathbox=list()
    pathbutton=list()
    for i in range(2):
        pathbox.append(tk.Entry(mw, width=30, state="disabled", textvariable=str))
        terminal.append(Terminal(pathbox[i]))
        pathbox[i].pack(side="left" if i==0 else "right")
        pathbutton.append(tk.Button(mw, overrelief="solid", text="Set Path", command=terminal[i].set_path))
        pathbutton[i].pack(side="left" if i==0 else "right")

    mw.mainloop()
    
    
