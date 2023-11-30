#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArgs = (len(sys.argv) - 1)
    if (numArgs == 0):
        print("{} arguments.".format(numArgs))
    elif (numArgs == 1):
        print("{} argument:".format(numArgs))
    else:
        print("{} arguments:".format(numArgs))

    if (numArgs > 1):
        numArgs = 0
        for arg in sys.argv:
            if numArgs != 0:
                print("{}: {}".format(numArgs, arg))
            numArgs += 1
