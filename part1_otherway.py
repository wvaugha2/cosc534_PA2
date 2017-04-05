

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


def senderCheck(name):
    if(name[0] >= 'a' and name[0] <= 'z' and name[1] == '0'):
        return True
    else:
        return False


if __name__ == "__main__":

    # Get the senders and receivers... booyah!!!
    senders, receivers = openFile(sys.argv[1])

    # Print out dem bad boys
    #for s, r in zip(senders, receivers):
        #print ("S: ", s)
        #print ("R: ", r)

#   for rnd in range(0, len(senders)):
#        for sender in range(0, len(senders[rnd])):
#            index_i = ord(senders[rnd][sender][0]) - 97
#            index_j = int(senders[rnd][sender][1])
#            offset = index_i
#            print(index_i, index_j)
#            break;
#        break;

    o_list = [[]]*26
    for i in range(len(o_list)):
        o_list[i] = [0]*len(receivers)
    
    print(len(o_list), len(o_list[0]))
    round = 0

    # Go through each round
    for senders_rnd, receivers_rnd in zip(senders, receivers):

        o_i = [0]*260

        # Obtain the receiver list o_i
        for receiver in range(0, len(receivers_rnd)):
            index_i = ord(receivers_rnd[receiver][0]) - 97
            index_j = int(receivers_rnd[receiver][1])
            offset = index_i*10 + index_j
            o_i[offset] = 1/len(receivers_rnd)


        # Update o_i for each appropriate sender on round i
        for sender in range(len(senders_rnd)):
            if(senderCheck(senders_rnd[sender]) == True):
                index_i = ord(senders_rnd[sender][0]) - 97
                index_j = int(senders_rnd[sender][1])
                offset = index_i*10 + index_j

                tmp = o_i[offset]
                o_i[offset] = 0
                o_list[index_i][round] = o_i*1
                o_i[offset] = tmp

        round += 1

    print(o_list[0][0])



