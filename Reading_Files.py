''' First time seeing how to read text files and then manipulate them '''

file=input("Please enter a file name?\n")
count=0
total=0

try:
    fhand=open(file)
except:
    print("Please enter a valid file name or file does not exist")
    quit()

for line in fhand:
    if not line.find("X-DSPAM-Confidence:")==-1:
        y=line.find("X-DSPAM-Confidence:")
        x=line.find(":",y,len(line))
        z=line[x+1:]
        count=count+1
        total=total+float(z.strip())
    else:
        continue
average=total/count
print("Average spam confidence:",average)

# mbox-short.txt
