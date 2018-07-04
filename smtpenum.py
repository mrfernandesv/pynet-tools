#!/usr/bin/python
import socket
import sys
import re

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "-----------------PYNET-TOOLS - smtpenum.py--------------"
    print "--------------------------------------------------------"
    print "------usage: ./smtpenum.py hostip hostport wordlist-----"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)

def smtpenum():
    
    file = open(sys.argv[3])

    for i in file.readlines():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[1], int(sys.argv[2])))
        resp = s.recv(1024)
        send = "VRFY " + i
        s.send(send)
        resp = s.recv(1024)
        if re.search("252",resp):
            print "Usuario encontrado: " + resp.strip("252 2.0.0 \r\n")

def main():
    if len(sys.argv)!=4:
        help()
    elif (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        help()
    else:
        smtpenum()

main()


