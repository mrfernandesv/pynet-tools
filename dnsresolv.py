#!/usr/bin/python
import socket
import sys

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "----------------PYNET-TOOLS - dnsresolv.py--------------"
    print "--------------------------------------------------------"
    print "----------usage: ./dnsresolv.py -d domain.com.br--------"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)

def dnsresolv():
    
    print sys.argv[2], "====>", socket.gethostbyname(sys.argv[2])

def main():

    if not len(sys.argv[1:]):
        help()
    else:
        arg1 = sys.argv[1]

    if (arg1 == "-h" or arg1 == "--help"):
        help()
    elif (arg1 == "-d"):
        if not len(sys.argv[2:]):
            help()
        else:
            dnsresolv()

main()


