import matplotlib.pyplot as plt 

ndvi_readings = [0.3, 0.6, 0.8, 0.4, 0.9, 0.5, 0.7, 0.65, 0.75, 0.55]

plt.hist(ndvi_readings, bins=5)

plt.xlabel("Readings")
plt.ylabel("Frequency")

plt.title("Ndvi Frequency histogram")
plt.grid(axis="y",alpha=0.3) # Used to mark the axis at points to read values better - alpha means opacity
plt.savefig("04_histogram.png")