import time, random, os, sys

def importantText(n):
    return("Enter terminal password now (" + str(n) + "/3 attempts left):")

def repetitiveOutput():
    output("Extracted possible passwords:\n" + wordchoicetext + "\n" + importantText(attempts))

def repetitiveOutput2(ui, pwd):
    cls()
    print("Extracted possible passwords:\n" + wordchoicetext + "\n" + importantText(attempts))
    for i in range(0, len(ui)):
        print(ui[i])
        print("Authentication failed. " + checksimilar(ui[i], pwd) + "/" + str(diff) + " correct.")

def checksimilar(ui, pwd):
    sim = 0
    for i in range(0, len(ui)):
        if ui[i] == pwd[i]:
            sim += 1
    return str(sim)

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
        time.sleep(0.005)

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

attemptsleft = 4
attempts = 0
diff = random.randint(3, 11) 
wordlist = readfile(diff)
passGuessed = False

wordchoice = repetitivelist(8, wordlist)
wordchoicetext = ltos(wordchoice).upper()
password = random.choice(wordchoice).strip()
repetitiveOutput()

userinput = []

while attemptsleft > 0 and passGuessed == False:
    userinput.append(input().strip().upper())
    userinputText = userinput[attempts].strip().upper()
    if userinputText == password:
        print("Correct")
        passGuessed = True
    else:
        print(userinputText + " " + password)
        attemptsleft = attemptsleft - 1
        repetitiveOutput2(userinput, password)
    attempts += 1

if passGuessed == False:    
    input("Put fancy lockout animation here")
else:
    input("Put fancy access granted animation here")
sys.exit()




