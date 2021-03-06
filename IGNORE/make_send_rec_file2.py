# Program Description

# This file should be placed within a directory that only contains node
# files generated by gatherData.py.  This file will create two files
# name public_rounds.txt and private_rounds.txt that will hold the
# round info to be used as input to part2.py and part3.py.

import sys
import os

if __name__ == "__main__":
    public_rounds = []
    private_rounds = []
    firstFile = True

    # Keep track of how many ACKs per round (first 16 public, last 16 private)
    ack = 0

    for r in range(0, 120):
        public_rounds.append(({}, {}))
        private_rounds.append(({},{}))

    for filename in os.listdir('.'):
        if(filename).endswith(".txt"):
            
            prev = ""
            round = 0
            ack = 0
            
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
                            ack = 0

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
                            if items[2] in private_rounds[round][0].keys():
                                tuple = private_rounds[round][0][items[2]]
                                if(float(items[0]) < tuple[0]):
                                    private_rounds[round][0][items[2]] = (float(items[0]), id)
                            else:
                                if (firstFile == True):
                                    private_rounds[round][0][items[2]] = (float(items[0]), id)
                                        
                        prev = "OFFER"
                            
                            
                    # Process all of the ACKs for current id
                    else:
                        #Public ACK messages
                        if(ack < 16):
                            # Check if tag in dict
                            if items[2] in public_rounds[round][1].keys():
                                tuple = public_rounds[round][1][items[2]]
                                if(float(items[0]) < tuple[0]):
                                    #Insert the tuple: (time, node ID)
                                    public_rounds[round][1][items[2]] = (float(items[0]), id)
                            else:
                                if (firstFile == True):
                                    public_rounds[round][1][items[2]] = (float(items[0]), id)
                    
                        ack += 1
                        prev = "ACK"
        
        
            firstFile = False

    # Write out the public rounds file.
    with open("public_rounds.txt","w") as f:
        for round in range(len(public_rounds)):
            #Print the receivers and senders for each round
            s = []
            x = 0
            for tuple in public_rounds[round][0].values():
                s.append(tuple[1])
            f.write("S: {0}\n".format(s))

            r = []
            for tuple in public_rounds[round][1].values():
                r.append(tuple[1])
            f.write("R: {0}\n".format(r))



