#!/usr/bin/python3

print("content-type:text/html")
print()

import cgi
import subprocess as sp


form = cgi.FieldStorage()
cmd = form.getvalue("program")
if "date" in cmd or "day" in cmd  or "time" in cmd:
    a = sp.getstatusoutput("date")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif "month" in cmd or "calender" in cmd:
    a = sp.getstatusoutput("cal")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif "year" in cmd:
    a = sp.getstatusoutput("cal -y")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif "ip" in cmd or "address" in cmd:
    a = sp.getstatusoutput("ifconfig")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")

elif "working directory" in cmd or "dir" in cmd or  "workspace" in cmd:
    a = sp.getstatusoutput("pwd")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif "ram" in cmd or "memory " in cmd:
    a = sp.getstatusoutput("free -m")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif "stop  web server" in cmd or "terminate  server" in cmd:
    a = sp.getstatusoutput("sudo systemctl stop httpd")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("stopped....")
        print("</pre>")
        print(a[0])
    else:
        print("Unsupported input format")
elif "storage" in cmd or "capacity" in cmd: 
    a = sp.getstatusoutput("df -h")
    if a[0] == 0:
        print("<pre>")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported input format")
elif  "start web server" in cmd  or "launch server" in cmd:
    a = sp.getstatusoutput("sudo systemctl start httpd")
    if a[0] == 0:
        print("<pre>")
        print("lauchced ...")
        print(a[1])
        print("</pre>")
    else:
        print("Unsupported format")
else:
    print("Command not found")
