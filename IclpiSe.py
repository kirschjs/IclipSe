import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# global simulation parameters

Ti = 0.0
Tf = 10
dt = 0.1



time = np.linspace(Ti, Tf, int((Tf-Ti)/dt))  # Time array

''' define a class of a stelar object following a Keplerian path

potential: V(r) = -k/r  k = G(m+M) with G = 6.674e-11 Nm**2kg**-2
and \vec{r}=\vec{x}(M)-\vec{x}(m)

xM=xcm+M/mu r
xm=xcm-m/mu r



'''
class KeplerObject:
    
    def __init__(self, energy,angmom,mass):
        self.E = energy
        self.l = angmom
        self.m = mass

    def eccentricity(self,)

    def r(self,t):
        return self.m * t

sA = KeplerObject(1,1,0.31)

print(sA.m,sA.r(5.2))
exit()

def circularOverlap(r1, r2, d):
    if r1 + r2 > d:
        return


# Parameters for the circular motions
radius1 = 5
pos1 = [2, 4]
omega1 = 1  # Angular velocity

# Parameters for the circular motions
radius2 = 4
pos2 = [1, 5]
omega2 = 1  # Angular velocity


# Circular motion equations
x1 = pos1[0] + radius1 * np.cos(omega1 * time)
y1 = pos1[1] + radius1 * np.sin(omega1 * time)
z1 = 1  # For a helical motion, you can use z = time

# Circular motion equations
x2 = pos2[0] + radius2 * np.cos(omega2 * time)
y2 = pos2[1] + radius2 * np.sin(omega2 * time)
z2 = 1  # For a helical motion, you can use z = time

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, z1, label='Circular Motion1')
ax.plot(x2, y2, z2, label='Circular Motion2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Circular Motion')
ax.legend()

plt.show()