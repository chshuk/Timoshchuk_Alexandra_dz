import os
from shutil import copy2

folder_name = 'templates'
root_name = 'my_project'
dir_name = os.path.join(root_name, folder_name)
os.makedirs(dir_name)
for root, dirs, files in os.walk(root_name):
    for file in files:
        ext = file.split('.')[-1].lower()
        if ext == 'html':
            file_path = os.path.relpath(root, file)
            new_dir = os.path.join(dir_name,file_path.split('\\')[-1])
            if not root == new_dir:
                if not os.path.isdir(new_dir):
                    os.mkdir(new_dir)
                copy2(os.path.join(root,file), new_dir)


