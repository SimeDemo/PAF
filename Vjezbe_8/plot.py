import matplotlib.pyplot as plt

og_x = []
string_x = []
x = []
og_y = []
string_y = []
y = []

with open("x_dataRK.txt", "r") as xdata, open("y_dataRK.txt", "r") as ydata:
    og_x = xdata.read()
    og_y = ydata.read()

    string_x = og_x.split(" ")
    string_y = og_y.split(" ")

    del string_x[-1]
    del string_y[-1]

    for i in string_x:
        x.append(float(i))

    for j in string_y:
        y.append(float(j))

            
plt.plot(x, y)
plt.show()