import matplotlib.pyplot as plt


def plot_RKvsE():

    ax = plt.subplot(111)

    for i in range(2):
        og_x = []
        string_x = []
        x = []
        og_y = []
        string_y = []
        y = []

        if i == 0:
            with open("x_data.txt", "r") as xdata, open("y_data.txt", "r") as ydata:
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

            ax.plot(x, y, label='Euler')

        else:
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

            ax.plot(x, y, label='Runge-Kutta')

    ax.legend()
    #plt.show()


def plot_range_versus_():

    fig, axs = plt.subplots(1, 2)

    for i in range(2):
        og_r = []
        string_r = []
        r = []
        og_var = []
        string_var = []
        var = []

        if i == 0:
            with open("masses.txt", "r") as xdata, open("ranges_m.txt", "r") as ydata:
                og_r = xdata.read()
                og_var = ydata.read()

                string_r = og_r.split(" ")
                string_var = og_var.split(" ")

                del string_r[-1]
                del string_var[-1]

                for i in string_r:
                    r.append(float(i))

                for j in string_var:
                    var.append(float(j))

            axs[0].plot(var, r)
            axs[0].set(xlabel="Cd", ylabel="range [m]")
            axs[0].set_title("range versus Cd")

        else:
            with open("cds.txt", "r") as xdata, open("ranges_cd.txt", "r") as ydata:

                og_r = xdata.read()
                og_var = ydata.read()

                string_r = og_r.split(" ")
                string_var = og_var.split(" ")

                del string_r[-1]
                del string_var[-1]

                for i in string_r:
                    r.append(float(i))

                for j in string_var:
                    var.append(float(j))

            axs[1].plot(var, r)
            axs[1].set(xlabel="mass [kg]", ylabel="range [m]")
            axs[1].set_title("range versus mass")
    
    plt.show()


plot_RKvsE()
plot_range_versus_()

# cudni skokovi postoje na zadnja 2 grafa, nije ni do dt-a ni do koraka u masama/Cd-ovima