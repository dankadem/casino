import sys

def clear():
    sys.stdout.write("\033[2J\033[3J\033[H")
    sys.stdout.flush()