''' From pdf Python4Everyone, tried to see Network Socketting '''

import socket
import re

webpage=input("Enter link to open:\n")
x=re.findall("//(.+?)/",webpage)
for y in x:
    z=str(y)
if len(x)==1:
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((z, 80))
        thing= 'GET '+webpage+" HTTP/1.0\r\n\r\n"
        cmd = thing.encode()
        mysock.send(cmd)
        while True:
            data = mysock.recv(512)
            if (len(data) < 1):
                break
            else:
                print(data.decode())
        mysock.close()
    except:
        print("Given URL does not work or is in wrong format.")
        print(thing)
else:
    print("Given URL does not work or is in wrong format.")
