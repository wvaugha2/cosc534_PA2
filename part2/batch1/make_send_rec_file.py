import sys
import os

if __name__ == "__main__":
    rounds = []
    firstFile = True

    for r in range(0, 120):
        rounds.append(({}, {}))

    for filename in os.listdir('.'):
        if(filename).endswith(".txt"):
            prev = ""
            round = 0
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

                        # Check if tag in dict
                        if items[2] in rounds[round][0].keys():
                            tuple = rounds[round][0][items[2]]
                            if(float(items[0]) < tuple[0]):
                                # Insert the tuple: (time, node ID)
                                rounds[round][0][items[2]] = (float(items[0]), id)
                        else:
                            if (firstFile == True):
                                rounds[round][0][items[2]] = (float(items[0]), id)
                        prev = "OFFER"
                    # Process all of the ACKs for current id
                    else:
                        # Check if tag in dict
                        if items[2] in rounds[round][1].keys():
                            tuple = rounds[round][1][items[2]]
                            if(float(items[0]) < tuple[0]):
                                #Insert the tuple: (time, node ID)
                                rounds[round][1][items[2]] = (float(items[0]), id)
                        else:
                            if (firstFile == True):
                                rounds[round][1][items[2]] = (float(items[0]), id)
                        prev = "ACK"
            firstFile = False

    for round in range(len(rounds)):
        #Print the receivers and senders for each round
        s = []
        x = 0
        for tuple in rounds[round][0].values():
            s.append(tuple[1])
        print "S: {0}".format(s)

        r = []
        for tuple in rounds[round][1].values():
            r.append(tuple[1])
        print "R: {0}".format(r)
