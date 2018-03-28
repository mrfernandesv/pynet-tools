#!/usr/bin/python
import sys
import httplib

def help():
    
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    print "-------------PYNET-TOOLS - finddirectories.py-----------"
    print "--------------------------------------------------------"
    print "--------usage: ./finddirectories.py -s site.com.br------"
    print "--------------------------------------------------------"
    print "--------------------------------------------------------"
    sys.exit(1)


def finddirectories():
    
    file = open(sys.argv[3])

    for i in file:
        i = i.replace("\n","")
        connection = httplib.HTTPConnection(sys.argv[2])
        connection.request("GET", "/" + i)
        response = connection.getresponse().status
        if (str(response) != "404"):
             print "Found directory: " + sys.argv[2] + "/" + i
    
    file.close()


def main():

    if not len(sys.argv[1:]):
        help()
    else:
        arg1 = sys.argv[1]

    if (arg1 == "-h" or arg1 == "--help"):
        help()
    elif (arg1 == "-s"):
        if not len(sys.argv[3:]):
            help()
        else:
            finddirectories()


main()


