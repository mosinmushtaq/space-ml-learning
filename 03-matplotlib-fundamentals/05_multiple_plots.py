import matplotlib.pyplot as plt


fig, axes=plt.subplots(1,3) # subplots is important - donot use subplot
                               # axes is just a name 
x1=[1,2,3,5,6]
y1=[10,20,30,40,50]

x2 = [0.3, 0.6, 0.8, 0.4, 0.9, 0.5, 0.7]
y2 = [80, 60, 20, 75, 10, 65, 30]

y3=[29,45,78,32,90]
x3=["Landsat","Sentinel","ESA","NASA","ISRO"]


axes[0].plot(x1, y1)
axes[0].set_title("Plot 1")
axes[1].scatter(x2, y2)
axes[1].set_title("Plot 2")
axes[2].bar(x3, y3)
axes[2].set_title("Plot 3")

plt.savefig("05_multiple_plots.png")