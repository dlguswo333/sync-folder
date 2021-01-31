import os
from shutil import copy2
import tkinter.messagebox

# Print error message according to usage of tkinter.
def print_error(message, use_tk):
    if use_tk:
        tkinter.messagebox.showerror(title="Error", message=message)
    else:
        print(message)


# Return list of file names in the path.
def get_filenames(path) -> list:
    filenames=os.listdir(path)
    return filenames

# Copy folder recursively.
# This copying function works based on file names.
# If a files with the same name exists, it will not be copied.
def copy_folder(src_path, dst_path, use_tk=None, result=None):
    src_path=os.path.abspath(src_path)
    dst_path=os.path.abspath(dst_path)
    
    if not os.path.exists(src_path):
        print_error('Error: Folder '+src_path+' is not valid.', use_tk)
        return False

    if not os.path.exists(dst_path):
        print_error('Error: Folder'+dst_path+' is not valid.', use_tk)
        return False
        
    try:
        src_filenames=get_filenames(src_path)
    except:
        print_error('Error: Could not files from '+src_path, use_tk)
        return False

    for filename in src_filenames:
        src=os.path.join(src_path, filename)
        dst=os.path.join(dst_path, filename)

        if os.path.isdir(src):
            # Recursively copy inner folder.
            if not os.path.exists(dst):
                # Create inner folder.
                try:
                    os.mkdir(dst)
                except:
                    print('Error: Could not copy folder '+src, use_tk)
            # Recursively call copy function.
            copy_folder(src, dst)
        elif not os.path.exists(dst):
            # Copy file if not exists.
            try:
                copy2(src, dst)
                print(src, 'copied to', dst)
                try:
                    if use_tk:
                        result['num_files']+=1
                        result['labeltext'].set(str(result['num_files'])+' files copied')
                    else:
                        result['labeltext'].set(str(result['num_files'])+' files copied. '+str(result['num_failed']+' failed.'))
                except:
                    # What can I do here? Nothing.
                    pass
            except:
                print('Error: Could not copy file '+src, use_tk)
                try:
                    result['num_failed']+=1
                    result['labeltext'].set(str(result['num_files'])+' files copied. '+str(result['num_failed']+' failed.'))
                except:
                    # What can I do here? Nothing.
                    pass
        else:
            # Do not copy the file exists.
            pass
    return True
    
# Synchronize folder.
def sync_folder(a_path, b_path, use_tk=None, result=None):
    if a_path==b_path:
        return
    if not copy_folder(a_path, b_path, use_tk, result):
        return
    copy_folder(b_path, a_path, use_tk, result)
    if use_tk:
        try:
            result['labeltext'].set('Success! '+result['labeltext'].get())
        except:
            # What can I do here? Nothing.
            pass

if __name__=='__main__':
    a_path=input()
    b_path=input()
    sync_folder(a_path, b_path)