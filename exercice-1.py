import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100) # ---> Je trace pour 100 abscisses comprises entre 0 et 1
y = x**(5)

plt.plot(x, y)
plt.show()

