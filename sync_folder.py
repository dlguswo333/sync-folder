import tkinter as tk
import os
import os.path
import tkinter.filedialog

target_ext=[".jpg", ".jpeg", ".webp", ".txt"]

class Terminal:
    def __init__(self, pathbox, listbox):
        self.path=""
        self.pathbox=pathbox
        self.listbox=listbox
    def set_path(self):
        self.path=tk.filedialog.askdirectory()
        self.pathbox.config(state="normal")
        self.pathbox.delete(0, tk.END)
        self.pathbox.insert(0, self.path)
        self.pathbox.config(state="disabled")
        self.get_filenames()
    def get_filenames(self):
        if not os.path.isdir(self.path):
            return False
        self.filenames=[name for name in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, name)) and os.path.splitext(name)[1] in target_ext]        
        self.listbox.delete(0, tk.END)
        for name in self.filenames:
            self.listbox.insert(tk.END, name)
if __name__=="__main__":
    mw=tk.Tk()
    mw.title="sync_folder"
    mw.geometry("800x600")
    frame=list()
    listbox=list()
    terminal=list()
    pathbox=list()
    pathbutton=list()
    loadbutton=list()
    for i in range(2):
        frame.append(tk.Frame(mw))
        frame[i].pack(side="left" if i==0 else "right", fill="both", expand=True)
        listbox.append(tk.Listbox(frame[i]))
        listbox[i].pack(side="top", fill="both", expand=True)
        pathbox.append(tk.Entry(frame[i], width=30, state="disabled", textvariable=str))
        terminal.append(Terminal(pathbox[i], listbox[i]))
        pathbox[i].pack(side="left", anchor="w", expand=True)
        pathbutton.append(tk.Button(frame[i], overrelief="solid", text="Set Path", command=terminal[i].set_path))
        pathbutton[i].pack(side="left", anchor="e")

    mw.mainloop()
    
    
