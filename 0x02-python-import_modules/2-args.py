#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNum = len(sys.argv) - 1

    if argNum == 0:
        print("{} arguments.".format(argNum))
    elif argNum == 1:
        print("{} argument:".format(argNum))
    else:
        print("{} arguments:".format(argNum))

    if argNum >= 1:
        argNum = 0
        for arg in sys.argv:
            if argNum != 0:
                print("{}: {}".format(i, arg))
            i += 1
