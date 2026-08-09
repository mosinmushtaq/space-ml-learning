import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sentinel = [45, 60, 30, 80, 25, 50, 35]
landsat = [48, 58, 32, 78, 28, 52, 38]
goes = [40, 65, 28, 82, 20, 55, 32]
temperature = [22, 24, 19, 25, 23, 26, 20]

# combined=[45, 60, 30, 80, 25, 50, 35,48, 58, 32, 78, 28, 52, 38,40, 65, 28, 82, 20, 55, 32]
combined=sentinel+landsat+goes
fig, axes=plt.subplots(1,3)

axes[0].plot(days,sentinel,color="red",linestyle="-",marker="o",label="Sentinel-2:")
axes[0].plot(days,landsat,color="blue",linestyle="--",marker="s",label="Landsat-8")
axes[0].plot(days,goes,color="green",linestyle=":",marker="^",label="GOES-16")

axes[0].set_xlabel("Days")
axes[0].set_ylabel("Cloud Coverage (%)")
axes[0].set_title("Cloud Coverage Comparison")

axes[0].legend()

axes[1].scatter(sentinel, temperature, color="orange", marker="*", label="Sentinel-2")
axes[1].set_title("Sentinel-2 vs Temperature")
axes[1].set_xlabel("Cloud Coverage (%)")
axes[1].set_ylabel("Temperature (°C)")



axes[2].hist(combined, bins=5, color="purple")
axes[2].set_title("Cloud Coverage Distribution")
axes[2].set_xlabel("Cloud Coverage (%)")
axes[2].set_ylabel("Frequency")


plt.savefig("09_styled_subplots.png")




