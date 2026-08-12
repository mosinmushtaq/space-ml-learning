import numpy as np 
import matplotlib.pyplot as plt

# For plotting the two lines, that is, two equations, and getting the intersection point as a solution, 
# we have to make a separate function. The function goes like this. 
matrixeq=np.array([[-1,2],
                  [3,2]])

matrixcont=np.array([7,1])
reshaped=matrixcont.reshape(2,1)


matrix=np.hstack((matrixeq, reshaped))

result=np.linalg.solve(matrixeq,matrixcont)

def plot_lines(matrixeq,matrix,result):
    a_coef_1=matrix[0,0]
    a_coef_2=matrix[1,0]

    b_coef_1=matrix[0,1]
    b_coef_2=matrix[1,1]

    const_1=matrix[0,2]
    const_2=matrix[1,2]

    a_range=np.linspace(-5,5,2)

    b_line1=(const_1-a_coef_1*a_range)/b_coef_1
    b_line2=(const_2-a_coef_2*a_range)/b_coef_2

    
    plt.plot(a_range,b_line1, color="blue",marker="^",label="Equation 1")
    plt.plot(a_range,b_line2,color="green",marker="s",label="Equation 2")

    plt.plot(result[0],result[1],color="red",marker="o",label=f"solution: ({result[0]:.2f}, {result[1]:.2f})")

    plt.grid()
    plt.legend()
    plt.xlabel("a")
    plt.ylabel("b")
    plt.title("System of linear equations")
    plt.savefig("05-Graphical-Representation.png")

plot_lines(matrixeq, matrix, result)
