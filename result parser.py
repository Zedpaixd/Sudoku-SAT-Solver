with open("SAToutput.txt","r") as file:
    line = file.readline()
    while line:
        for satConstraint in line.split(" "):
                if len(satConstraint) > 2 and satConstraint[0] not in ["v","-"]:
                    print("line:{} | column:{} | value:{}".format(satConstraint[0],satConstraint[1],satConstraint[2]))
        line = file.readline()

input("Press enter to exit.")