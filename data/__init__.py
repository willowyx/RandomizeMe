import os
import importlib.util
module_path = os.path.join(os.getenv('appdata'), 'RandomizeMe/lists.py')
spec = importlib.util.spec_from_file_location('lists', module_path)
lists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lists)

def getsval():
    appdata_path = os.getenv('appdata')
    folder_path = os.path.join(appdata_path, 'RandomizeMe')
    file_path = os.path.join(folder_path, 'sval.txt')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.path.isfile(file_path):
        open(file_path, 'a').close()

    return file_path

def getlists():
    appdata_path = os.getenv('appdata')
    folder_path = os.path.join(appdata_path, 'RandomizeMe')
    file_path = os.path.join(folder_path, 'lists.py')

    if not os.path.isfile(file_path):
        open(file_path, 'a').close()

    return file_path
