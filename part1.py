

import sys
import os
import re

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


if __name__ == "__main__":

    # Get the senders and receivers... booyah!!!
    senders, receivers = openFile(sys.argv[1])

    # Print out dem bad boys
    for s, r in zip(senders, receivers):
        #print ("S: ", s)
        #print ("R: ", r)

        

