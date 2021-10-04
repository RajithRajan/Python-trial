from tkinter import Tk
from tkinter.filedialog import askdirectory
import os

# Renames the LRF extenstion files into MP4 files in the selected folder

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)

files = os.listdir(path)

for file in files:
    file_split = os.path.splitext(file)
    if file_split[1] == '.LRF' :
        print(file)
        os.rename(os.path.join(path,file),os.path.join(path,''.join([file_split[0],'.MP4'])))