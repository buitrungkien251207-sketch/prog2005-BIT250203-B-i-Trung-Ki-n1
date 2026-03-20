import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 6)

plt.plot(x, x**2, label='y=x^2')
plt.plot(x, x, label='y=x')

plt.legend()
plt.show()