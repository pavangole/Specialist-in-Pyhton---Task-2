#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess

form = cgi.FieldStorage()

osname = form.getvalue("x")
osimage = form.getvalue("i")


cmd = "sudo docker run  -d  -i  -t  --name{0}  {1}".format(osname, osimage)

output = subprocess.getstatusoutput(cmd)

status = output[0]
out = output[1]

if status == 0:
    print("os launched name {} ...".format(osname))
else:
    print("some error : {}", format(out))