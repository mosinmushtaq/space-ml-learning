import matplotlib.pyplot as plt


count=[29,45,78,32,90]
satelite=["Landsat","Sentinel","ESA","NASA","ISRO"]


plt.bar(satelite, count)

plt.xlabel("Satellite")
plt.ylabel("Count")
plt.title("Satellite Count in 2022")

plt.savefig("03_bar_chart.png")
