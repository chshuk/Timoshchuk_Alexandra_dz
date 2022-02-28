import os

root_name = 'my_project'
dir_names = {'settings', 'mainapp', 'adminapp', 'authapp'}
for name in dir_names:
    dir_path = os.path.join(root_name, name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)