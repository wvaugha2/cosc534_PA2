import sys
import os
import re
from operator import itemgetter

###################################################################################
# Open the csv file of senders and receivers and return their corresponding lists #
###################################################################################
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

#######################################################################
# Check to make sure sender is only the 0th sender for its associated #
# letter --> (ex: a0, b0, c0, d0, etc..)                              #
#######################################################################
def senderCheck(user):
    if (user[1] == '0'):
        return True
    else:
        return False

#############################################################
# Return recipient location in users list for current round #
#############################################################
def find_offset(user):
    index_i = ord(user[0]) - 97
    index_j = int(user[1])
    offset = (index_i*10) + index_j
    return offset

###########################################################################
# Fill the dictionary with usrs being keys, value is a list of tuples     #
# correpsonding to current round, first element, and a list of recipients #
# for that round, second element.                                         #
###########################################################################
def fill_dict(senders, receivers, dict):
    for rnd in range(0, len(senders)):
        for sender in senders[rnd]:
            if (senderCheck(sender)):
                so = find_offset(sender)
                rnd_list = [(None, 0)]*260
                for receiver in receivers[rnd]:
                    num_messages = len(receivers[rnd])
                    ro = find_offset(receiver)
                    if (ro != so):
                        rnd_list[ro] = (receiver, (1/(num_messages*1.0))/100)
                if sender in dict.keys():
                    list = dict.get(sender)
                    for item in range(0, len(rnd_list)):
                        rec = rnd_list[item][0]
                        if (rec == None):
                            rec = list[item][0]
                        value = list[item][1]
                        ave_value = (value + rnd_list[item][1])
                        list[item] = (rec, ave_value)
                else:
                    dict[sender] = rnd_list
    return dict

########################
# Print out users, yo. #
########################
def print_dict(dict):
    for key, value in dict.items():
        friends = sorted(set(value), key=itemgetter(1))
        print "{0} --> {1}".format(key, friends[-2:])
        print ""


if __name__ == "__main__":
    users = {}
    # Get the senders and receivers... booyah!!!
    senders, receivers = openFile(sys.argv[1])
    users = fill_dict(senders, receivers, users)
    #users = arith_mean(users)
    print_dict(users)
    # Print out dem bad boys
    #for s, r in zip(senders, receivers):
        #print ("S: ", s)
        #print ("R: ", r)
