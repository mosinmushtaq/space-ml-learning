import matplotlib.pyplot as plt


x_axis=[1,2,3,5,6]
y_axis=[10,20,30,40,50]


plt.plot(x_axis,y_axis)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Just to see")
# plt.show()  There was some problem as vscode terminal cant show the graph , so imma use the savefig function instead
plt.savefig("01_line_plot.png")

