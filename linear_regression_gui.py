from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
from tkinter  import * 
from math import sqrt
from celluloid import Camera
#This fucntion is called after the commit button is clicked it stores the filename in the variable
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    global filename
    filename=inputValue
def retrieve_lr():
    inputValue=textBox2.get("1.0","end-1c")
    global learningRate
    learningRate=inputValue
# def predict_Y(m,c):
#     res=0
#     for i in range(0,len(height)):
#         res+=m*height[i]+c
#     global loss
#     loss=0
#     for i in range(0,len(height)):
#         loss+=weight[i]-res
#     return res
# def derivative_m(yp):
#     res=0
#     for i in range(0,len(height)):
#         res+=height[i] * (weight[i]-yp)
#     return res
# def derivative_c(yp):
#     res=0
#     for i in range(0,len(weight)):
#         res+=weight[i]-yp
#     return res

#start_calc() - This function starts the calculation
def start_calc():
    uio=0
    ypreds=[]
    w=0
    b=0
    lr=float(learningRate) #learning rate
    #epoch=1000
    losses=[]
    epochs=[]
    e=0
    loss1 = 10000
    prevloss = 0
    lossdiff = 1
    while(lossdiff>0.00001):
        print('epoch number- ',e,' loss sqrt = ',loss1) #printing epoch numbers and square roots of losses
        sumw = 0
        sumb = 0
        loss = 0
        for k in range(0,len(x)):
            ypred = x[k]*w + b
            sumw = sumw + x[k]*(y[k]-ypred)   # partial derivative of the cost function with respect to slope
            sumb = sumb + (y[k]-ypred)        # partial derivative of the cost function with respect to intercept
            loss = loss + (ypred - y[k])*(ypred - y[k])  
        dw = -2*(sumw)/len(x)
        bw = -2*(sumb)/len(x)
        loss = loss/len(x)
        prevloss = loss1
        loss1 = sqrt(loss)
        lossdiff = prevloss-loss1
        epochs.append(e+1)
        e = e+1
        losses.append(loss1)
        w = w - lr*dw
        b = b - lr*bw
        yp=[]
        for v in range(0,len(x)):
            yp.append(x[v]*w+b)
        if(e==1):
            plt.plot(x,y)
        plt.plot(x,yp)
        camera.snap()
    animation = camera.animate(interval = 50, repeat = True,repeat_delay = 50)
    print('w= ',w,' b= ',b)
    for k in range(0,len(x)):
        ypreds.append(x[k]*w + b)
    #plotting 
    plt.figure(2)
    plt.plot(x, ypreds,'red')
    plt.scatter(x,y,c='blue')
    plt.xlabel(header[1])
    plt.ylabel(header[2])
    plt.title((header[1]," vs ",header[2]))
    plt.grid(True)
    plt.show()
#Creating the root window
root=Tk()
root.geometry("1000x1000")
root.title("Linear Regressor")
#Creating the commit button
buttonCommit=Button(root, height=1, width=10, text="Commit", command=lambda: retrieve_input())
buttonCommit.pack()
#Creating the text box
l = Label(text = "Enter complete path of the csv file")
textBox=Text(root, height=2, width=100)
textBox.pack()
l.pack()
mainloop()
#End of tkinter mainloop
#Reading the file
file = open(filename)
csvreader = csv.reader(file)
header = []
#Reading the labels
header = next(csvreader)
x=[]
y=[]
#Storing the height and the weight
for i in csvreader:
    temp=next(csvreader)
    x.append(int(float(temp[1])))
    y.append(int(float(temp[2])))
fig=plt.figure()
camera=Camera(fig)
#plotting the values
plt.scatter(x,y,c="blue")
plt.xlabel(header[1])
plt.ylabel(header[2])
plt.title((header[1]," vs ",header[2]))
#C:\Users\Lenovo\Downloads\archive\weight-height.csv
root=Tk()
root.geometry("1000x1000")
root.title("Linear Regressor")
plot_button = Button(root,height = 2, width = 20, text = ("Plot ",header[1]," vs ",header[2]), command=lambda:plt.show())
l2 = Label(text = "Enter learning rate")
textBox2=Text(root, height=2, width=100)
enter_lr_button=Button(root,height = 2, width = 20, text = "Enter Learning Rate", command=lambda:retrieve_lr())
start_optimising=Button(root,height = 2, width = 20, text = "Start Optimising", command=lambda:start_calc())
start_optimising.pack()
enter_lr_button.pack()
textBox2.pack()
plot_button.pack()
mainloop()
