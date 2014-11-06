#!/usr/bin/python

import os
import sys

n = 0
urls = []
names = []

def radio():
    global n, urls, names
    fhand = open("stations.txt")
    n = 0
    for line in fhand:
        n += 1
        print str(n)+":", line[:line.find(",")]
        url = line[line.find(",") + 1:]
        urls.append(url)
        name = line[:line.find(",")]
        names.append(name)
    
def interract():
    print ""
    station = raw_input("Select Station or type q to exit: ")
    try:
        st = int(station) 
        if st > len(names) or st < 0:
            interract()
    except:
        if station == "q":
            print "\nGoodbye...\n"
            sys.exit()
        else:
            print "\nWrong Input, try again\n"
            interract()
    print "\nNow playing", names[st-1]
    print "If you want to stop press q\n"
    os.system('mplayer -really-quiet '+ urls[st-1])
    make_change()

def make_change():
    global n, names, urls
    change = raw_input("\nType c to change station\nType q to exit\n% ")
    if change == "c":
        radio()
        interract()
    elif change == "q":
        print "\nGoodbye..."
        sys.exit()
    else:
        print "Wrong Input, try again"
        make_change()


radio()
interract()
