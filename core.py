import os
from shutil import copy2

# Return list of file names in the path.
def get_filenames(path) -> list:
    filenames=os.listdir(path)
    return filenames

# Copy folder recursively.
# This copying function works based on file names.
# If a files with the same name exists, it will not be copied.
def copy_folder(src_path, dst_path):
    src_path=os.path.abspath(src_path)
    dst_path=os.path.abspath(dst_path)
    
    src_filenames=get_filenames(src_path)

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
                    print('Error: Could not copy folder', src)
            # Recursively call copy function.
            copy_folder(src, dst)
        elif not os.path.exists(dst):
            # Copy file if not exists.
            try:
                copy2(src, dst)
                print(src, 'copied to', dst)
            except:
                print('Error: Could not copy file', src)
        else:
            # Do not copy the file exists.
            pass
    
# Synchronize folder.
def sync_folder(a_path, b_path):
    copy_folder(a_path, b_path)
    copy_folder(b_path, a_path)

if __name__=='__main__':
    a_path=input()
    b_path=input()
    sync_folder(a_path, b_path)