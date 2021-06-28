import numpy as np
from matplotlib import pyplot as plt

class Newton:

    def __init__(self, f, x, i, fig, ax, h=1.0E-6):
        self.f = f      #function
        self.x = x      #start estimate
        self.i = i      #iteration limit
        self.h = h      
        self.fig = fig
        self.ax = ax

    def calculate(self):
        counter = 0  #keeping track of iteration count

        #calculating the derivative
        der = lambda: (self.f(self.x + self.h) - self.f(self.x - self.h)) / (2 * self.h)

        while True:
            self.ax.plot(self.x, 0, "bo") #original estimate
            plt.pause(0.3)
            self.ax.plot(self.x, self.f(self.x), "o", c="black") 
            print(f"x{counter}: {self.x}")
            plt.pause(0.3)

            self.ax.plot([self.x, self.x], [0, self.f(self.x)], "k--d")
            plt.pause(0.3)

            old = self.x  
            self.x = self.x - (self.f(self.x) / der()) #new estimate

            self.ax.plot([old, self.x], [self.f(old), 0], "k--")

            counter += 1 
            if counter == self.i:  #maximum iteration limit
                return self.x, counter
            
            if abs(self.f(self.x)) < 1.0E-6:    #estimate is accurate to 1.0x10^6 
                self.ax.plot(self.x, 0, "o", c="pink")
                plt.pause(0.3)
                return self.x, counter

def main():

    print("Welcome!")
    print("\nPlease choose a function below")
    print("a) x^2")
    print("b) 2x^2 - x - 2")
    print("c) 1 - x^2 + 2^x")
    print("d) 3x^3 - 9x^2 +5x + 2")
    print("e) sin(x)")


   
    input_func = input("Choose a function to simulate: ")
    
    if(input_func == "a"):
        f = eval("lambda x:" + "x**2")
        
    elif(input_func == "b"):
        f = eval("lambda x:" + "2*x**2-x-2")
        
    elif(input_func == "c"):
        f = eval("lambda x: 1-x**2+2**x")
        
    elif(input_func == "d"):
        f = eval("lambda x: 3*x**3-9*x**2+5*x+2")
    elif(input_func == "e"):
        f = eval("lambda x: np.sin(x)")
        
    else:
        print("Invalid option")
        

    x = np.linspace(-10, 10, 1000)

    #plotting
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, f(x), color="orange")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.title("Simulation")
    plt.grid()



    while True:
        input_x = float(input("\nEnter the starting point: "))
        input_i = float(input("\nEnter max iterations: "))
        newton = Newton(f, input_x, input_i, fig, ax)
        root, iterations = newton.calculate()
        return root, iterations




if True:
    root, iterations = main()
    print(f"Root: {root}, Iterations: {iterations}")
    plt.show()
    
    
    
