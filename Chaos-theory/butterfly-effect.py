# https://medium.com/@alexroz/how-to-plot-chaos-butterfly-effect-in-python-862c0cb621a4

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.font_manager import FontProperties
import numpy as np

class Attractor():
  def __init__(self, X=1, Y=1, Z=1):
    self.x = X
    self.y = Y
    self.z = Z
    self.sigma = 10
    self.beta = 8 / 3
    self.rho = 28

  def step(self, dt=0.005):
    dx = self.sigma * (self.y - self.x)
    dy = self.x * (self.rho - self.z) - self.y
    dz = self.x * self.y - self.beta * self.z

    self.x += dx * dt
    self.y += dy * dt
    self.z += dz * dt
    
butterfly = Attractor(2,1,1)
N = 15000
x,y,z = [],[],[]
for i in range(N):
  x.append(butterfly.x)
  y.append(butterfly.y)
  z.append(butterfly.z)
  butterfly.step()
  
x,y,z = np.array(x), np.array(y), np.array(z)


points = np.array([x, z]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

lc = LineCollection(segments, cmap='cool')
lc.set_array(y) 
lc.set_linewidth(2)

fig, ax = plt.subplots(figsize=(16,9))
ax.add_collection(lc)
ax.autoscale_view()
ax.spines[['right', 'top', 'bottom', 'left']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('black')
#ax.text(-21,2,'Lorenz Attractor', fontproperties=font_prop,fontsize=25)
plt.tight_layout()
plt.savefig('Lorenz.png')
plt.show()