import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
X = np.arange(40, 125, 5)

Y = np.array([872, 879, 878, 890, 961, 930, 943, 930, 961, 955, 968, 992, 1011, 1012, 1036, 1027, 1040])
Y2 = np.array([679, 683, 1041, 1880, 2572, 2853, 3161, 3914, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000, 4000])

plt.plot(X, Y, 'purple', label="cluster")
plt.plot(X, Y2, 'darkcyan', label="sppl")


plt.xlabel("the number of sheep")
plt.ylabel("steps")
plt.xticks(np.arange(0, 100, 10))
plt.legend()
plt.xlim(40, 125)
plt.ylim(0, 4200)
plt.grid()
plt.show()