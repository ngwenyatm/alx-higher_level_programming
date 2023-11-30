#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArg = len(sys.argv)-1
    if numArg == 1:
        print("{} arguments.".format(numArg))
    elif numArg == 2:
        print("{} argument:".format(numArg))
    else:
        print("{} arguments:".format(numArg))
    for i in range(1, numArg):
        print("{}: {}".format(i, sys.argv[i]))
