import time
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def output(str):
    for i in range(0, len(str)-1):
        print(str[:i])
        time.sleep(0.01)
        cls()

def readfile(n):
        l = []
        with open("dictionary.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) == n:
                    l.append(line)
        print(l)
        f.close()

input("Press ENTER to run. Do not run from IDLE.")

readfile(5)
