with open("input.txt", "r") as inp:
    content = inp.readlines()
    for i in range(len(content)):
        content[i] = content[i].split()

with open("constraints.txt", "w") as file:
    # constraint 1
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                print(str(100 * x + 10 * y + z) + " ", end="", file=file)
            print(" 0", file=file)

    # constraint 2
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1, 9):
                for i in range(x + 1, 10):
                    print(str(-(100 * x + 10 * y + z)) + " " + str(-(100 * i + 10 * y + z)) + " 0", file=file)

    # constraint 3
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y + 1, 10):
                    print(str(-(100 * x + 10 * y + z)) + " " + str(-(100 * x + 10 * i + z)) + " 0", file=file)
    # constraint nr 4 part 1
    for z in range(1, 10):
        for i in range(3):
            for j in range(3):
                for x in range(1, 4):
                    for y in range(1, 4):
                        for k in range(y + 1, 4):
                            print(str(-((3 * i + x) * 100 + (3 * j + y) * 10 + z)) + " " + str(
                                -((3 * i + x) * 100 + (3 * j + k) * 10 + z)) + " 0", file=file)
    # constraint nr 4 part 2
    for z in range(1, 10):
        for i in range(3):
            for j in range(3):
                for x in range(1, 4):
                    for y in range(1, 4):
                        for k in range(x + 1, 4):
                            for l in range(1, 4):
                                print(str(-((3 * i + x) * 100 + (3 * j + y) * 10 + z)) + " " + str(
                                    -((3 * i + k) * 100 + (3 * j + l) * 10 + z)) + " 0", file=file)
    for i in range(len(content)):
        for j in range(len(content[i])):
            if int(content[i][j]) != 0:
                print(str((i + 1) * 100 + (j + 1) * 10 + int(content[i][j])), "0", file=file)