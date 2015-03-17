import sys
import string

def substitute(text, original, new):
    new = "[1;31m" + new + "[m"
    result = []
    newBool = False;
    for i in list(text):
        if i == "":
            newBool = not newBool
        if not newBool and i == original:
            result.append(new)
        else:
            result.append(i)
    return "".join(result)

def clearScreen():
    print "\033\143"

def langStat(text):
    stats = {}
    listOChar = list(text.lower())
    alphabet = list(string.ascii_lowercase)
    charCount = 0
    for i in listOChar:
        charCount += 1
        if i not in alphabet:
            pass;
        elif i in stats:
            stats[i] += 1
        else:
            stats[i] = 1

    for i in stats:
        stats[i] = 100 * float(stats[i]) / float(charCount)
    return stats

def main():
    print "Welcome to frequency analysor!"
    path = raw_input("Please enter the location of encrypted file: ")
    text = open(path, "r").read().lower()
    print "File loaded! Use 'help' for help."
    statDict = langStat(text)
    prompt = raw_input(">> ")
    while (prompt != "EXIT"):
        if prompt.find("replace") != -1:
            try:
                statDict["[1;31m" + new + "[m"] = statDict[original]
                statDict.pop(original)
            except Exception:
                print "alread substituted!"
            original = prompt[prompt.find(" ") + 1:prompt.find(",")]
            new = prompt[prompt.find(",") + 1:]
            text = substitute(text, original, new)
        if prompt.find("display") != -1:
            print text
        if prompt.find("stats") != -1:
            result = ""
            for i in statDict:
                result += i + ": %.02f " % (statDict[i]) + "%\n"
            print result
        if prompt.find("write") != -1:
            path = prompt[prompt.find(" ") + 1:]
            text2 = text.replace("1;31m", "").replace("[m", "")
            fout = open(path, "w")
            fout.write(text2)
            fout.close()
        if prompt.find("help") != -1:
            print """Usage:
display: prints the passage as it looks now
stats: prints the current letter statistics
replace <original>,<new>: replace the original letter with the new letter
write <path> writes the final passage to path
EXIT: exit the program
"""
        prompt = raw_input(">> ")

main()
