import matplotlib.pyplot as plt

fig, axes=plt.subplots(1,3)

Days=[1,2,3,4,5,6,7]
Temperature=[22, 24, 19, 25, 23, 26, 20]


NDVI=[0.3, 0.6, 0.8, 0.4, 0.9, 0.5, 0.7]
Cloud=[80, 60, 20, 75, 10, 65, 30]


Temperature=[22, 24, 19, 25, 23, 26, 20]


axes[0].plot(Days, Temperature)
axes[0].set_title("Temperature Trend")

axes[1].scatter(NDVI, Cloud)
axes[1].set_title("NDVI vs Cloud Cover")

axes[2].hist(Temperature, bins=3)
axes[2].set_title("Temperature Distribution")


plt.savefig("06_mixed_subplots.png")