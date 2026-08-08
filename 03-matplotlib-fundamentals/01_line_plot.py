import matplotlib.pyplot as plt


x_axis=[1,2,3,5,6]
y_axis=[10,20,30,40,50]


plt.plot(x_axis,y_axis)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Just to see")
# plt.show()  There was some problem as vscode terminal cant show the graph , so imma use the savefig function instead
plt.savefig("01_line_plot.png")

##ONE IMPORTANT THING I LEANT  is that if i dont clear the canvas , the first graph will be wrapped by the first graph 
# the function to clear the canvas is 

plt.clf()

days = [1, 2, 3, 4, 5, 6, 7]
cloud_coverage = [45, 60, 30, 80, 25, 50, 35] 

plt.plot(days,cloud_coverage)

plt.xlabel("Days")
plt.ylabel("Cloud Coverage (%)")
plt.title("Cloud Coverage Over Time")
plt.savefig("01_line_plot(1).png")

