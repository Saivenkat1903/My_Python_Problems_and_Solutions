''' Plotting 2 graphs on the same plot using matplotlib '''

from matplotlib import pyplot as plt


y2_values=[29,27,29,30,31,31,34,33,34,34,33,32,30,30,21,27,29]
y1_values=[28,29,29,30,31,32,33,33,34,34,33,32,31,30,29,29,29]
x_values=[]
thing=6

while len(x_values)!=len(y1_values):
    if thing!=24:
        x_values.append(str(thing)+":30")
        thing=thing+1
    else:
        x_values.append("00"+":30")
        thing=1

plt.plot(x_values,y1_values,x_values,y2_values,marker="o")
plt.legend(["Chennai Temp","Puducherry Temp"])
plt.title("Temperature Variation of Chennai")
plt.xlabel("24 hour Time")
plt.ylabel("Temperature in degrees Celcius")
plt.axis(ymin=0)
plt.axis(ymax=40)
plt.axis(xmax=len(x_values))
plt.tick_params(axis='x', which='major', labelsize=5.5)

plt.show()
