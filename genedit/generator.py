import importlib.util
import random
import itertools
import re
import os

def import_module(mname, rpath):
    # Get the absolute path of the directory
    dir_path = os.path.join(os.path.dirname(__file__), rpath)

    # Get the absolute path of the module file
    module_file = os.path.join(dir_path, f'{mname}.py')

    # Create a module spec from the path
    spec = importlib.util.spec_from_file_location(mname, module_file)

    # Create a module from the spec
    module = importlib.util.module_from_spec(spec)

    # Execute the module
    spec.loader.exec_module(module)

    return module

# Current dir located in genedit/
lists = import_module('lists', '../data')


def rnum():
    svgen = ''
    lengths = (len(lists.ListA), len(lists.ListB), len(lists.ListC), len(lists.ListD), len(lists.ListE))
    # print(lengths)
    for i in range(5):
        dig = random.randint(1, lengths[i] - 1)
        # print(dig)
        if len(str(dig)) < 2:
            dig = str(0) + str(dig)
        svgen += str(dig)
    return svgen


# all seeds are mod the list length (all normal integer seeds are valid)
# invalid seed values will always default to a new random seed

def getabspath(rpath, rname):
    dirname = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(dirname, os.pardir))
    textout = os.path.join(parent_dir, rpath, rname)
    return textout

def returnstr(pre=None):
    sval = ''
    if pre is not None:
        try:
            int(pre)
            if 2 < len(pre) < 10:
                pre = str(pre) * 5
                pre = pre[:10]
            elif len(pre) < 2:
                pre = str(pre) * 10
            elif len(pre) > 10:
                pre = pre[:10]
            elif int(pre) < 0:
                pre = str(int(pre) * -1)
            sval = pre  # sanitized & validated sval
            # print('nogen sval ' + sval)
        except:
            sval = rnum()
    else:
        sval = str(rnum())  # generate number
        # print('gen sval ' + sval)

    # print("rnum call getstr: " + str(pre))
    textout = "Your "
    with open(getabspath('data', 'sval.txt'), 'a') as f:
        f.write(sval + '\n')
        f.close()
    slsize = os.path.getsize('../data/sval.txt')
    if slsize > 10000:
        with open('../data/sval.txt', 'w') as f:
            f.write(sval + '\nnote: file exceeded 10kb and was overwritten\n')
            f.close()

    # print(sval)

    # pass 1
    match = re.match(r'^\d{2}', sval)
    if match:
        # print(match.group())
        textout += lists.ListA[int(match.group()) % len(lists.ListA)] + " "

    # pass 2
    match = re.match(r'^\d{2}(\d{2})', sval)
    if match:
        # print(match.group(1))
        textout += lists.ListB[int(match.group(1)) % len(lists.ListB)] + " "

    # pass 3
    match = re.match(r'^\d{4}(\d{2})', sval)
    if match:
        # print(match.group(1))
        textout += lists.ListC[int(match.group(1)) % len(lists.ListC)] + ", "

    # pass 4
    match = re.match(r'^\d{6}(\d{2})', sval)
    if match:
        # print(match.group(1))
        textout += lists.ListD[int(match.group(1)) % len(lists.ListD)] + "! "

    # pass 5
    match = re.match(r'^\d{8}(\d{2})', sval)
    if match:
        # print(match.group(1))
        textout += lists.ListE[int(match.group(1)) % len(lists.ListE)]

    return textout


# print("Random seed: " + rnum())

# print(returnstr())
