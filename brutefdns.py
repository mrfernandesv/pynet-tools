#!/usr/bin/python
import socket
import sys

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "----------------PYNET-TOOLS - brutefdns.py--------------"
    print "--------------------------------------------------------"
    print "-----usage: ./brutefdns.py -d domain.com.br wordlist----"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)

def brutefdns():
    
    file = open(sys.argv[3])

    for i in file:
        i = i.replace("\n","")
        name = i + "." + sys.argv[2]
        
        try:
            host = socket.gethostbyname(name)
            print "Host", name, "===>",host
        except:
            pass

def main():

    if not len(sys.argv[1:]):
        help()
    else:
        arg1 = sys.argv[1]

    if (arg1 == "-h" or arg1 == "--help"):
        help()
    elif (arg1 == "-d"):
        if not len(sys.argv[3:]):
            help()
        else:
            brutefdns()

main()


