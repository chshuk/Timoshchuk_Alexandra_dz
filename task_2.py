import os

with open('config.yaml', 'r', encoding='utf-8') as f1:
    dir_root = f1.readline().strip()
    for line in f1:
        objects = line.split('{')
        dir_path = os.path.join(dir_root, objects[0].strip())
        os.makedirs(dir_path)
        for obj in objects[1:]:
            for el in obj.split(','):
                if '.' in el:
                    f = open(os.path.join(dir_path, el.strip()), 'w')
                    f.close()
                else:
                    dir_path = os.path.join(dir_path, el)
                    os.makedirs(dir_path)
