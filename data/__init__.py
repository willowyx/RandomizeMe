import os
import platform
import importlib.util


def getsysname():
    return platform.system()


def getModulePath(fname):
    if fname == 'lists':
        if getsysname() == 'Windows':
            return os.path.join(os.getenv('appdata'), 'RandomizeMe/lists.py')
        elif getsysname() == 'Darwin':
            return os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/lists.py')
    elif fname == 'sval':
        if getsysname() == 'Windows':
            return os.path.join(os.getenv('appdata'), 'RandomizeMe/sval.txt')
        elif getsysname() == 'Darwin':
            return os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/sval.txt')
    elif fname == 'prefs':
        if getsysname() == 'Windows':
            return os.path.join(os.getenv('appdata'), 'RandomizeMe/prefs.uwu')
        elif getsysname() == 'Darwin':
            return os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/prefs.uwu')


module_path = getModulePath('lists')
spec = importlib.util.spec_from_file_location('lists', module_path)
lists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lists)
