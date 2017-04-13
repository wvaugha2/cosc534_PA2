import socket
import threading
import time
import sys
import os
import re
from operator import itemgetter

def thread_function(node,stime):
    id = node[0:64]
    ip = node[65:77]
    port = int(node[78:])

    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    add = (ip,port)
    socket1.connect(add)

    fname = id + ".txt"
    f = open(fname, "a")

    while True:
        data = socket1.recv(1024).decode("utf-8").rstrip()
        f.write(data + '\n')
        f.flush()


if __name__ == "__main__":
    
    nodes = []

    # Obtain public nodes from nodes.txt file.
    with open("nodes.txt") as f:
        lines = f.readlines()
        for line in lines[1:121]:
            nodes.append(line.rstrip())

    curTime = time.time()

    print("Hey")

    for node in nodes:
        print("fork thread")
        t = threading.Thread(target=thread_function,args=(node,curTime))
        t.daemon = True
        t.start()

    while time.time() - curTime < 36000:
        curTime = curTime

