
''' From Amit Shah Doing math with python, plots projectile motion curves '''

from matplotlib import pyplot as plt
import math

g=9.8
velocities=list()
angles=list()

number=input("How many total trajectories?\n")

try:
    bang=int(number)
except:
    print("feck off")
    exit()

for i in range(1,int(number)+1):
    u=input("Enter your initial velocity for trajectory "+str(i)+".\n")
    theta=input("Enter your angle of projection for trajectory "+str(i)+".\n")
    velocities.append(u)
    angles.append(theta)

try:
    for j in range(len(velocities)):
        temp_velo=float(velocities[j])  #u
        temp_theta=float(angles[j])*(math.pi/180)     #angle
        time_of_flight=2*temp_velo*math.sin(temp_theta)/g
        t_values=list()
        x_values=list()
        y_values=list()
        t=0
        while t<time_of_flight:
            t_values.append(t)
            t=t+0.001
        for k in t_values:
            corresponding_x_value=temp_velo*math.cos(temp_theta)*k
            corresponding_y_value=(temp_velo*math.sin(temp_theta)*k)-(g/2*(k**2))
            x_values.append(corresponding_x_value)
            y_values.append(corresponding_y_value)
        plt.plot(x_values,y_values)

except:
    print("Don't be a bitch")
    exit()

random_crap_I_Need=list()

for i in range(1,int(number)+1):
    thing="Trajectory "+str(i)
    random_crap_I_Need.append(thing)

plt.legend(random_crap_I_Need)
plt.title("Projectile Motion Comparision")
plt.xlabel("Horizontal distance")
plt.ylabel("Vertical distance")

plt.show()
