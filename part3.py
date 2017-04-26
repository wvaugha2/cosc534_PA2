import socket
import sys
import os
import re
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



    for key,value in priv_nodes.items():
        print(key, " -> ", value)










