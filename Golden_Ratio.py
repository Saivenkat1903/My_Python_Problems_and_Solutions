''' Plots the golden ratio in graphical form '''

from matplotlib import pyplot as plt

index=[1]
fibo=[1,1]

ratios=[1]

for i in range(0,100):
    if i>1:
        next_number=fibo[i-1]+fibo[i-2]
        next_ratio=next_number/fibo[i-1]
        fibo.append(next_number)
        ratios.append(next_ratio)
        index.append(i)

plt.plot(index,ratios)
plt.title("Golden Ratio")
plt.xlabel("Term in series")
plt.ylabel("Ratio value")
plt.axis(ymin=1)
plt.show()
