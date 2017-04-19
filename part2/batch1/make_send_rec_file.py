
import sys
import os














if __name__ == "__main__":

    rounds = []
    prev = ""
    firstFile = True

    rounds.append(({},{}))
    
    
    for filename in os.listdir('.'):
        if(filename).endswith(".txt"):
            round = 0
            id = filename[:-4]

            with open(filename) as f:
                lines = f.readlines()
                

                for line in lines:
                    items = line.rstrip().split(' ')

                    if(items[1] == "OFFER"):
                        if prev == "ACK":
                            round += 1
                            if(firstFile == True or round == len(rounds)):
                                rounds.append(({},{}))
                    
                    
                        
                        # Check if tag in dict
                        if items[2] in rounds[round][0].keys():
                            tuple = rounds[round][0][items[2]]
                            if(float(items[0]) < tuple[0]):
                                #Insert the tuple: (time, node ID)
                                #print(float(items[0]),id)
                                rounds[round][0][items[2]] = float(items[0]),id
                                #print(rounds[round][0][items[2]], '\n')
                        else:
                            #print(float(items[0]),id)
                            rounds[round][0][items[2]] = float(items[0]),id
                            #print(rounds[round][0][items[2]], '\n')
                        prev = "OFFER"

                    else:
                        # Check if tag in dict
                        if items[2] in rounds[round][1].keys():
                            tuple = rounds[round][1][items[2]]
                            if(float(items[0]) < tuple[0]):
                                #Insert the tuple: (time, node ID)
                                #print(float(items[0]),id)
                                rounds[round][1][items[2]] = float(items[0]),id
                                #print(rounds[round][1][items[2]], '\n')
                        else:
                            #print(float(items[0]),id)
                            rounds[round][1][items[2]] = float(items[0]),id
                            #print(rounds[round][1][items[2]], '\n')
                        prev = "ACK"
                firstFile = False

    for round in range(len(rounds)):
        #Print the receivers and senders for each round
        s = []
        for tuple in rounds[round][0].values():
            s.append(tuple[1])
        print("S:",s)
        
        r = []
        for tuple in rounds[round][1].values():
            r.append(tuple[1])
        print("R:",r)






