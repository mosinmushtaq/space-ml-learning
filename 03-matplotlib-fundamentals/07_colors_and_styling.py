import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
sentinel = [45, 60, 30, 80, 25, 50, 35]
landsat = [56, 58, 63, 72, 81, 93, 99]

plt.plot(days, sentinel, color="red", linestyle='solid', marker="*")
plt.plot(days, landsat, color="black", linestyle='dashed', marker="o")


# 'solid' or '-' = normal line
# 'dashed' or '--' = dashed
# 'dotted' or ':' = dotted
# 'dashdot' or '-.' = dash-dot

plt.xlabel("Days")
plt.ylabel("Cloud Coverage")
plt.title("Two Satellites")

plt.savefig("07_colors_and_styling.png")