

import sys
import os
import re

def senderCheck(name):
    if(name[0] >= 'a' and name[0] <= 'z' and name[1] == '0'):
        return True
    else:
        return False

def openFile(fname):

    senders = []
    receivers = []

    with open(fname) as fp:
        lines = fp.readlines()

        for line in lines:
            if line[0] == 'S':
                input = re.findall(r"(?<![@#])\b\w+(?:'\w+)?", line[1:])
                senders.append(input)
            else:
                input = re.findall(r"(?<![@#])\b\w+(?:'\w+)?", line[1:])
                receivers.append(input)
    return senders, receivers

def fill_dict(senders, receivers, dict):
    for rnd in range(0, len(senders)):
        for sender in senders[rnd]:
            key = sender
            rnd_list = [0]*260
            for receiver in receivers[rnd]:
                index_i = ord(receiver[0]) - 97
                index_j = int(receiver[1])
                offset = (index_i*10) + index_j
                rnd_list[offset] = 1/32.0
            if key in dict.keys():
                value = dict.get(key)
                value.append((rnd, rnd_list))
            else:
                dict[key] = [(rnd, rnd_list)]
    return dict

def print_dict(dict):
    for key, value in dict.items():
        print "{0} --> {1}".format(key,  value)


if __name__ == "__main__":
    users = {}
    # Get the senders and receivers... booyah!!!
    senders, receivers = openFile(sys.argv[1])
    users = fill_dict(senders, receivers, users)
    print_dict(users)
    # Print out dem bad boys
    #for s, r in zip(senders, receivers):
        #print ("S: ", s)
        #print ("R: ", r)
