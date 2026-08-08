import matplotlib.pyplot as plt

ndvi = [0.3, 0.6, 0.8, 0.4, 0.9, 0.5, 0.7]
cloud = [80, 60, 20, 75, 10, 65, 30]


plt.scatter(ndvi,cloud)

plt.xlabel("NDVI")
plt.ylabel("Cloud")

plt.title("NDVI vs Cloud Coverage ")

plt.savefig("02_scatter_plot.png")