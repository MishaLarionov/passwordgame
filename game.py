import time, random, os, sys

def importantText(n):
    return("Enter terminal password now (" + str(n) + "/3 attempts left):")

def repetitiveOutput():
    output("Extracted possible passwords:\n" + wordchoicetext + "\n" + importantText(attempts))

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def ltos(l):
    s = ""
    for i in range(0, len(l)):
        s = (s + l[i] + " ")
    s = s.strip()
    return s

def repetitivelist(n, i):
    l = []
    for z in range(0, n):
        l.append(random.choice(i))
    return l

def output(string):
    for i in range(0, len(string)+1):
        cls()
        print(string[:i])
        time.sleep(0.01)

def readfile(n):
        l = []
        with open("dictionary.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) == n:
                    l.append(line)
        f.close()
        return l

input("Press ENTER to run. Do not run from IDLE.")

attempts = 3
wordlist = readfile(5)
passGuessed = False

wordchoice = repetitivelist(8, wordlist)
wordchoicetext = ltos(wordchoice).upper()
password = random.choice(wordchoice).strip()
repetitiveOutput()

while attempts > 0 and passGuessed == False:
    userinput = input()
    userinput = userinput.strip().upper()
    if userinput == password:
        passGuessed = True
    else:
        attempts = attempts - 1
        
print("ayy lmao")
input()
sys.exit()




