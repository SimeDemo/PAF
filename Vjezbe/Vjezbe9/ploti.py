import matplotlib.pyplot as plt

def plot_motion():

    fig, axs = plt.subplots(1, 2)

    for i in range(2):
        og_r = []
        string_r = []
        r = []
        og_var = []
        string_var = []
        var = []

        if i == 0:
            with open("h_data.txt", "r") as xdata, open("t_data.txt", "r") as ydata:
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
            axs[0].set(xlabel="t [s]", ylabel="h [m]")
            axs[0].set_title("h-t graph")

        elif i == 1:
            with open("h_dataAR.txt", "r") as xdata, open("t_dataAR.txt", "r") as ydata:

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
            axs[1].set(xlabel="t [s]", ylabel="h [m]")
            axs[1].set_title("h-t graph with air resistance")

    plt.show()


def plot_energy():

    axsE = plt.subplot(111)

    for i in range(4):
        og_r = []
        string_r = []
        r = []
        og_var = []
        string_var = []
        var = []

        if i == 0: # energy no AR 
            with open("ekinetic.txt", "r") as xdata, open("t_data.txt", "r") as ydata:

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

            axsE.plot(var, r, label="kinetic energy")
            axsE.set(xlabel="t [s]", ylabel="E [J]")
            axsE.set_title("Energy conservation")

        elif i == 1:
            with open("epotential.txt", "r") as xdata, open("t_data.txt", "r") as ydata:

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

            axsE.plot(var, r, label="potential energy")
        
        elif i == 2:
            with open("eelastic.txt", "r") as xdata, open("t_data.txt", "r") as ydata:

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

            axsE.plot(var, r, label="elastic energy")

        elif i == 3:
            with open("etotal.txt", "r") as xdata, open("t_data.txt", "r") as ydata:

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

            axsE.plot(var, r, label="total energy")
    
    plt.legend()
    plt.show()
    

def plot_energyAR():

    axsE = plt.subplot(111)

    for i in range(4):
        og_r = []
        string_r = []
        r = []
        og_var = []
        string_var = []
        var = []

        if i == 0: # energy no AR 
            with open("ekineticAR.txt", "r") as xdata, open("t_dataAR.txt", "r") as ydata:

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

            axsE.plot(var, r, label="kinetic energy")
            axsE.set(xlabel="t [s]", ylabel="E [J]")
            axsE.set_title("Energy conservation with air resistance")

        elif i == 1:
            with open("epotentialAR.txt", "r") as xdata, open("t_dataAR.txt", "r") as ydata:

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

            axsE.plot(var, r, label="potential energy")
        
        elif i == 2:
            with open("eelasticAR.txt", "r") as xdata, open("t_dataAR.txt", "r") as ydata:

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

            axsE.plot(var, r, label="elastic energy")

        elif i == 3:
            with open("etotalAR.txt", "r") as xdata, open("t_dataAR.txt", "r") as ydata:

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

            axsE.plot(var, r, label="total energy")
    
    plt.legend()
    plt.show()


plot_motion()
plot_energy()
plot_energyAR()