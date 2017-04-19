import socket
import sys
import os
import re
from operator import itemgetter

if __name__ == "__main__":

    pub = ["80514f8a06541066bdfccd9a97b5cfb92d5f9eefc8f3a6cd474deb33d7c90d91@160.36.57.98:15012",
             "8061e9097c2b1a39428c0e374f31f2da5477c579d556e1608ea0e0b3e176e391@160.36.57.98:15055",
             "80405bcea95b4c637f4a825e3737ef4cf1e900a74075170b47b08da95227675c@160.36.57.98:15046"]
    priv = []
    
    while(len(pub) != 120 and len(priv) != 120):
        for node in pub:
            # Set up the socket to connect to the node.
            id = node[0:64]
            ip = node[65:77]
            port = int(node[78:])
            
            socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            add = (ip,port)
            
            # If the node is private, add it to the private list.
            try:
                socket1.connect(add)
                # Call PEERS to obtain peer nodes.
                for i in range(5):
                    socket1.send(b'PEERS\n')
                    for j in range(8):
                        data = socket1.recv(84).decode("utf-8").rstrip()
                        if(data[0] != '8'):
                            j -= 1
                        else:
                            if(data not in pub and data not in priv):
                                pub.append(data)
            except:
                pub.pop(pub.index(node))
                priv.append(node)


    for i in range(len(pub)):
        if pub[i] in priv:
            pub.pop(i)
    for i in range(len(priv)):
        if priv[i] in pub:
            priv.pop(i)

    print("Public: ",len(pub))
    for i in range(120):
        print(pub[i])
    print("\nPrivate: ",len(priv))
    for i in range(120):
        print(priv[i])
