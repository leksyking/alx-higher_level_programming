#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    chk = len(sys.argv) - 1
    if chk == 0:
        print("0 arguments.")
    elif chk == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(chk))
    for i in range(chk):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
