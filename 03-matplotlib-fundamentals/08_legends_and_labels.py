import matplotlib.pyplot as plt


days = [1, 2, 3, 4, 5, 6, 7]
sentinel = [45, 60, 30, 80, 25, 50, 35]
landsat = [48, 58, 32, 78, 28, 52, 38]


plt.plot(days, sentinel, label="Sentinel", color="red", linestyle='solid', marker="*")
plt.plot(days, landsat, label="Landsat", color="blue", linestyle='dashed', marker="^")

plt.xlabel("Days")
plt.ylabel("Cloud Coverage")
plt.title("Two Satellites")

plt.legend()

plt.savefig("08_legends_and_labels.png")