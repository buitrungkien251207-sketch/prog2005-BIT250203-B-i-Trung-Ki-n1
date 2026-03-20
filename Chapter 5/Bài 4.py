import matplotlib.pyplot as plt

cities = ['LA','SD','SJ','SF','Fresno','Sac','LB','Oak','Bake','Ana']
areas = [1302,964,469,121,298,259,133,202,388,131]

plt.barh(cities, areas)
plt.show()