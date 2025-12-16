import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,1,0,-1,-2,-1,0])
y = np.array([0,2,0,3,0,3,0,2,0])

plt.plot(x, y, marker='*', markerfacecolor='red', 
         markeredgecolor='green', color='goldenrod', 
         linestyle='dashed', markersize=15)
plt.title("Last CHRISTMAS")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(color='green', linestyle='--', linewidth=1)
plt.gca().set_facecolor("lightyellow")
plt.show()
