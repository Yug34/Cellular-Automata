import numpy as np
import matplotlib.pyplot as plt
import random as rd

s = 50
xp = 25
yp = 25

position = np.zeros((s, s))
position[yp][xp] = 1

for i in range(100):
    n = rd.randint(1, 4)
    if n == 1:
        # up
        xp += 0
        yp += 1
        position[yp][xp] = 1
        position[yp-1][xp] = 0
    elif n == 2:
        # down
        xp += 0
        yp -= 1
        position[yp][xp] = 1
        position[yp+1][xp] = 0
        
    elif n == 3:
        # right
        xp += 1
        yp += 0
        position[yp][xp] = 1
        position[yp][xp-1] = 0
    else:
        # left
        xp -= 1
        yp += 0
        position[yp][xp] = 1
        position[yp][xp+1] = 0
    plt.pause(0.05)
    plt.imshow(position)