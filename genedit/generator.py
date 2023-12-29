import random
import re
import os
import data
import importlib.util
module_path = os.path.join(os.getenv('appdata'), 'RandomizeMe/lists.py')
spec = importlib.util.spec_from_file_location('lists', module_path)
lists = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lists)

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

def returnstr(pre=None):
    sval = ''
    if pre is not None:
        try:
            int(pre)
            if int(pre) < 0:
                pre = str(int(pre) * -1)
            if 2 < len(pre) < 10:
                pre = str(pre) * 5
                pre = pre[:10]
            if len(pre) < 2:
                pre = str(pre) * 10
            if len(pre) > 10:
                pre = pre[:10]
            sval = pre  # sanitized & validated sval
            # print('nogen sval ' + sval)
        except:
            sval = rnum()
    else:
        sval = str(rnum())  # generate number
        # print('gen sval ' + sval)

    # print("rnum call getstr: " + str(pre))
    textout = "Your "
    with open(data.getsval(), 'a') as f:
        f.write(sval + '\n')
        f.close()
    slsize = os.path.getsize(data.getsval())
    if slsize > 10000:
        with open(data.getsval(), 'w') as f:
            f.write(sval + '\nnote: file exceeded 10kb and was overwritten\n')
            f.close()

    # print(sval)

    # pass 1
    match = re.match(r'^\d{2}', sval)
    if match:
        textout += lists.ListA[int(match.group()) % len(lists.ListA)] + " "

    # pass 2
    match = re.match(r'^\d{2}(\d{2})', sval)
    if match:
        textout += lists.ListB[int(match.group(1)) % len(lists.ListB)] + " "

    # pass 3
    match = re.match(r'^\d{4}(\d{2})', sval)
    if match:
        textout += lists.ListC[int(match.group(1)) % len(lists.ListC)] + ", "

    # pass 4
    match = re.match(r'^\d{6}(\d{2})', sval)
    if match:
        textout += lists.ListD[int(match.group(1)) % len(lists.ListD)] + "! "

    # pass 5
    match = re.match(r'^\d{8}(\d{2})', sval)
    if match:
        textout += lists.ListE[int(match.group(1)) % len(lists.ListE)]

    return textout


# print("Random seed: " + rnum())
# print(returnstr())
