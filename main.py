import os
import sys

target_ext=["webp", "jpg", "png", "txt"]
def get_filenames(dir):
    #This function returns a list of file name without ext, except for the currently executing python file.
    filenames=[filename for filename in os.listdir(dir) if os.path.splitext(filename)[1][1:] in target_ext and filename!=os.path.basename(sys.argv[0])]
    for i in range(len(filenames)):
        filenames[i]=os.path.splitext(filenames[i])[0]
    return filenames

#main
target_dir="C:\\Users\\LHJ\\Documents\\VSCodeWorkspace\\sync_folder"
filenames=get_filenames(target_dir)
output_file=open(target_dir+"/filenames.txt", 'w')
for filename in filenames:
    output_file.write(filename+'\n')
output_file.close()