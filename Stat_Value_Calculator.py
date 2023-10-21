''' Using the collections library to get median mode and mean '''

from collections import Counter

data=list()

file=input("Enter the file with the data:\n")
fhand=open(file)

for line in fhand:
    data.append(int(line))

mean=sum(data)/len(data)

thing=Counter(data)
print(thing[0])
mode=1

data.sort()
if len(data)%2==0:
    index=int((len(data)/2)-1)
    median=data[index]
else:
    index=int((len(data)+1)/2)
    median=data[index]

print("Mean is {0}, Mode is {1}, and Median is {2}".format(mean,mode,median))
