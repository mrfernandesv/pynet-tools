#!/usr/bin/python
import socket
import sys

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "------------------PYNET-TOOLS - whois.py----------------"
    print "--------------------------------------------------------"
    print "------------usage: ./whois.py -d domain.com.br----------"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)

def whois():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("200.160.2.3",43))
    s.send(sys.argv[2]+'\r\n')
    resp = s.recv(1024)
    print resp

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
            whois()

main()


