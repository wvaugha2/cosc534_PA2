import socket
import sys
import os
import re
import itertools
from operator import itemgetter

if __name__ == "__main__":

    # Holds the private nodes a public node connects to.
    pub_nodes_priv = {}
    
    # Holds the public node information to connect via socket.
    pub_nodes_info = {}
    
    # Holds all of private node ids.
    private = []
    
    # Holds the public nodes each private node connects to
    priv_nodes = {}
    
    # Obtain public nodes from nodes.txt file.
    with open("nodes.txt") as f:
        lines = f.readlines()
        for line in lines[1:121]:
            line = line.rstrip()
            
            # Keyed on node ID, value is a tuple - (ip, port)
            pub_nodes_info[line[0:64]] = (line[65:77],int(line[78:]))

        for line in lines[123:243]:
            line = line.rstrip()
            private.append(line[0:64])

    for key,values in pub_nodes_info.items():
        # Connect to the node
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        add = (values[0],values[1])
        
        peers = []

        try:
            socket1.connect (add)
            
            turns_same = 0
            oldctr = 0
            curctr = 0
        
            while(turns_same < 20):
                socket1.send(b'PEERS\n')
                for j in range(8):
                    data = socket1.recv(84).decode("utf-8").rstrip()
                    if(data[0] != '8'):
                        j -= 1
                    else:
                        #print(data)
                        oldctr = curctr
                        if(data[0:64] not in peers and data[0:64] in private):
                            curctr += 1
                            peers.append(data[0:64])
                    #print(j)
                
                if(oldctr == curctr):
                    turns_same += 1
                else:
                    turns_same = 0

                #print(key,"Number of peers found: ", len(peers))
        except:
            print("{} - could not connect".format(key))

        pub_nodes_priv[key] = peers


    for node in private:
        
        priv_nodes[node] = []
        
        for key,value in pub_nodes_priv.items():
            if node in value:
                priv_nodes[node].append(key)



    #for key,value in priv_nodes.items():
        #print(key, " -> ", value)


########################################################################################################

    public_rounds = []
    private_rounds = []
    ack_rounds = []
    firstFile = True
    
    # Keep track of how many ACKs per round (first 16 public, last 16 private)
    ack = 0
    
    for r in range(0, 120):
        public_rounds.append(({}, {}))
        private_rounds.append(({},{}))
        ack_rounds.append({})

    for filename in os.listdir('.'):
        if(filename).endswith(".txt") and filename != "nodes.txt":
            
            prev = ""
            round = 0
            ack = 0
            off = 0
            priv_indexes = []
            
            id = filename[:-4]
            #sys.stderr.write(str(id) + '\n')
            
            with open(filename) as f:
                lines = f.readlines()
                
                
                for line in range(0, len(lines)):
                    items = lines[line].rstrip().split(' ')
                    # Process all of the OFFERs from current id
                    if(items[1] == "OFFER"):
                        
                        if (prev == "ACK"):
                            round += 1
                            #if(round == 120):
                                #break
                            priv_index = []
                            ack = 0
                            off = 0
                        
                        # Public OFFER messages
                        if(items[2][0] == 'f'):
                            # Check if tag in dict
                            if items[2] in public_rounds[round][0].keys():
                                tuple = public_rounds[round][0][items[2]]
                                if(float(items[0]) < tuple[0]):
                                    # Insert the tuple: (time, node ID)
                                    public_rounds[round][0][items[2]] = (float(items[0]), id)
                            else:
                                if (firstFile == True):
                                    public_rounds[round][0][items[2]] = (float(items[0]), id)
                        
                        # Private OFFER messages
                        else:
                            priv_indexes.append(off)
                            if items[2] in private_rounds[round][0].keys():
                                list = private_rounds[round][0][items[2]]
                                
                                if(len(list) < 8):
                                    private_rounds[round][0][items[2]].append((float(items[0]), id))
                                else:
                                    list = sorted(list, key=itemgetter(0))
                                    list.reverse()
                                    
                                    if(float(items[0]) < list[0][0]):
                                        list[0] = (float(items[0]), id)
                                        private_rounds[round][0][items[2]] = list
                                
                                #if(float(items[0]) < tuple[0]):
                                    #private_rounds[round][0][items[2]] = (float(items[0]), id)
                        
                            else:
                                if (firstFile == True):
                                    private_rounds[round][0][items[2]] = []
                                    private_rounds[round][0][items[2]].append((float(items[0]), id))
                
                        prev = "OFFER"
                        off += 1
                    
                    
                    # Process all of the ACKs for current id
                    else:

                        if items[2] in ack_rounds[round].keys():
                            list = ack_rounds[round][items[2]]
                                
                            if(len(list) < 8):
                                ack_rounds[round][items[2]].append((float(items[0]), id))
                            else:
                                list = sorted(list, key=itemgetter(0))
                                list.reverse()
                                    
                                if(float(items[0]) < list[0][0]):
                                    list[0] = (float(items[0]), id)
                                    ack_rounds[round][items[2]] = list
                    
                    
                        #if(float(items[0]) < tuple[0]):
                        #private_rounds[round][1][items[2]] = (float(items[0]), id)
                        
                        else:
                            if (firstFile == True):
                                ack_rounds[round][items[2]] = []
                                ack_rounds[round][items[2]].append((float(items[0]), id))
                    
                    
                        ack += 1
                        prev = "ACK"
        
            firstFile = False



    # To be filled with ACK senders of each round
    pub_r = []
    for i in range(120):
        pub_r.append([])

    # Write out the private rounds file.
    with open("private_rounds.txt","w") as f:
        for round in range(len(private_rounds)):
            #print("Round: ",round, " --> ")
        
            if(len(private_rounds[round][0]) == 0):
                break;
        
            s = []
            
            for message in private_rounds[round][0]:
                #print("  Message: ",message)
                list = private_rounds[round][0][message]
                
                people = []
                for e in list:
                    people.append(e[1])

                #Search for a match with a private node.
                found = False
                for key,value in priv_nodes.items():
                    ret = set(value) & set(people)
                    #print(len(ret))
                    if(len(ret) == 8):
                        s.append(key)
                        found = True
                        break

                '''if(found == True):
                    print("OFFER", message, " --> ", s[-1])
                else:
                    print("OFFER", message, " No match found")'''

            priv_r = []
            for message in ack_rounds[round]:
                list = ack_rounds[round][message]

                people = []
                for e in list:
                    people.append(e[1])

                found = False
                for key,value in priv_nodes.items():
                    ret = set(value) & set(people)
                    if(len(ret) == 8):
                        priv_r.append(key)
                        found = True
                        break
                
                if(found == False):
                    ack_rounds[round][message] = sorted(ack_rounds[round][message], key=itemgetter(0))
                    pub_r[round].append(ack_rounds[round][message][0][1])

            #print("Round {} --> len(priv_r): {}     len(pub_r[{}]): {}\n\n".format(round,len(priv_r),round,len(pub_r[round])))
        
            f.write("S: {0}\n".format(s))
            f.write("R: {0}\n".format(priv_r))

    # Write out the public rounds file.
    with open("public_rounds.txt","w") as f:
        for round in range(len(public_rounds)):
            
            if(len(private_rounds[round][0]) == 0):
                break;
            
            # Print the senders for the round
            s = []
            for tuple in public_rounds[round][0].values():
                s.append(tuple[1])
            f.write("S: {0}\n".format(s))
            
            # Print the receivers for the round
            f.write("R: {0}\n".format(pub_r[round]))










