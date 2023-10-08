#!/usr/bin/python3

import os
import re
import sys

def main():
    for line in sys.stdin:

        match = re.match('^\\s*#', line)
        fields = line.strip().split(':')  # Strip whitespace and split into an array

        if match or len(fields) != 5: # if the line starts with # or does not have five fields it will skip 
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        groups = fields[4].split(',')  # This line of code is spliting the fifth field using commas

        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print cmd
        os.system(cmd)

        print("==> Setting the password for %s..." % (username)) 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #print cmd
        os.system(cmd)

        for group in groups: # this for loop is iterating through the list and assiging users to a group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print cmd
                os.system(cmd)  # this line of code takes the command and passes it to the operating system

if __name__ == '__main__':
    main()
