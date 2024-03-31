import random
import re
import os
import data
import importlib.util

module_path = ''
if data.getsysname() == 'Windows':
    module_path = os.path.join(os.getenv('appdata'), 'RandomizeMe/lists.py')
elif data.getsysname() == 'Darwin':
    module_path = os.path.join(os.path.expanduser('~/Library/Application Support'), 'RandomizeMe/lists.py')

spec = importlib.util.spec_from_file_location('lists', module_path)
lists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lists)


def rnum():
    svgen = ''
    lengths = (
    len(lists.ListF), len(lists.ListA), len(lists.ListB), len(lists.ListC), len(lists.ListD), len(lists.ListE))
    # print(lengths)
    for i in range(6):
        dig = random.randint(1, lengths[i] - 1)
        # print(dig)
        if len(str(dig)) < 2:
            dig = str(0) + str(dig)
        svgen += str(dig)
    return svgen


# all seeds are mod the list length (all normal integer seeds are valid)
# invalid seed values will always default to a new random seed

def returnstr(pre=None):
    sval = ''
    if pre is not None:
        try:
            int(pre)
            if " " in pre:
                pre = pre.replace(" ", "")
            if int(pre) < 0:
                pre = str(int(pre) * -1)
            if 3 < len(pre) < 12:
                pre = str(pre) * 5
                pre = pre[:10]
            if len(pre) <= 2:
                pre = str(pre) * 12
            if len(pre) > 12:
                pre = pre[:12]
            sval = pre  # sanitized & validated sval
            print('nogen sval result: ' + sval)
        except:
            sval = rnum()
            print('fallback to random generation')
    else:
        sval = str(rnum())  # generate number
        print('gen sval result: ' + sval)

    # print("rnum call getstr: " + str(pre))
    textout = ""
    with open(data.getModulePath('sval'), 'a') as f:
        f.write(sval + '\n')
        f.close()
    slsize = os.path.getsize(data.getModulePath('sval'))
    if slsize > 10000:
        with open(data.getModulePath('sval'), 'w') as f:
            f.write(sval + '\nnote: file exceeded 10kb and was overwritten\n')
            f.close()

    # print(sval)

    # pass 1
    match = re.match(r'^\d{2}', sval)
    if match:
        textout += lists.ListF[int(match.group(0)) % len(lists.ListF)] + " "

    # pass 2
    match = re.match(r'^\d{2}(\d{2})', sval)
    if match:
        textout += lists.ListA[int(match.group(1)) % len(lists.ListA)] + " "

    # pass 3
    match = re.match(r'^\d{4}(\d{2})', sval)
    if match:
        textout += lists.ListB[int(match.group(1)) % len(lists.ListB)] + " "

    # pass 4
    match = re.match(r'^\d{6}(\d{2})', sval)
    if match:
        textout += lists.ListC[int(match.group(1)) % len(lists.ListC)] + ", "

    # pass 5
    match = re.match(r'^\d{8}(\d{2})', sval)
    if match:
        textout += lists.ListD[int(match.group(1)) % len(lists.ListD)] + "! "

    # pass 6
    match = re.match(r'^\d{10}(\d{2})', sval)
    if match:
        textout += lists.ListE[int(match.group(1)) % len(lists.ListE)]

    return textout
