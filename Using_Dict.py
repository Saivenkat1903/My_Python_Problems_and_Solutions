''' Using a dictionary to manipulate strings from a file '''

import string

thing=dict()

file=input("Enter file name.\n")

try:
    fhand=open(file)
except:
    print("yo man I can't open this file, either it doesn't exist or you are pulling ebic prank on me.")
    quit()

for line in fhand:
    line=line.strip()
    dhang=line.split()
    if len(dhang)>=2 and dhang[0] in ["From","from"]:
        new=str(dhang[1])
        y=new.find("@")
        thing[new[y+1:]]=thing.get(new[y+1:],0)+1
    else:
        continue
print(thing)
