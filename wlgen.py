import random
import string
def banner():
    print "#################################################################################"
    print "##     __     __             __                                                ##"
    print "##    /  |   /  |           /  |                                               ##"
    print "##    $$ |   $$ | ______   _$$ |_     ______    ______   ______   _______      ##"
    print "##    $$ |   $$ |/      \ / $$   |   /      \  /      \ /      \ /       \     ##"
    print "##    $$  \ /$$//$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$$  |    ##"
    print "##     $$  /$$/ $$    $$ |  $$ | __ $$    $$ |$$ |  $$/ /    $$ |$$ |  $$ |    ##"
    print "##      $$ $$/  $$$$$$$$/   $$ |/  |$$$$$$$$/ $$ |     /$$$$$$$ |$$ |  $$ |    ##"
    print "##       $$$/   $$       |  $$  $$/ $$       |$$ |     $$    $$ |$$ |  $$ |    ##"
    print "##        $/     $$$$$$$/    $$$$/   $$$$$$$/ $$/       $$$$$$$/ $$/   $$/     ##"
    print "##                                                                             ##"
    print "##                      By : T3r@bYt3 | Python 2.x                             ##"
    print "#################################################################################"
def easyGen(a,b,c):
    file=open("WList.txt","w")
    chars=string.ascii_letters + string.digits
    wrd=''
    for counter in range(0,c):
        for x in random.sample(chars,random.randint(a,b)):
            wrd+=x
        file.write(wrd+"\n")
        wrd=''
    file.close()

def medGen(a,b,c):
    file = open("WList.txt", "w")
    chars = string.ascii_letters + string.digits + string.punctuation
    wrd = ''
    for counter in range(0, c):
        for x in random.sample(chars, random.randint(a, b)):
            wrd += x
        file.write(wrd + "\n")
        wrd = ''
    file.close()

def hardGen(a,b,c):
    file = open("WList.txt", "w")
    chars = string.ascii_letters + string.digits + string.punctuation + string.hexdigits + string.octdigits + string.whitespace
    wrd = ''
    for counter in range(0, c):
        for x in random.sample(chars, random.randint(a, b)):
            wrd += x
        file.write(wrd + "\n")
        wrd = ''
    file.close()

def creator():
    wmlen=int(raw_input("Minimum Length of Word : "))
    wMlen=int(raw_input("Maximum Length of Word : "))
    nW=int(raw_input("Number of words : "))
    lvl=int(raw_input("Select Level :\n1. Easy\t2. Medium\t3. Hard\n-> "))
    if lvl==1:
        easyGen(wmlen,wMlen,nW)
    elif lvl==2:
        medGen(wmlen,wMlen,nW)
    elif lvl==3:
        hardGen(wmlen,wMlen,nW)
    else:
        print "Invalid Input"
    print "[ INFO ] Wordlist generated successfully."
    print "[ INFO ] Output is stored in 'WList.txt'"
if __name__=="__main__":
    banner()
    creator()