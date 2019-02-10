import serial
import time
import matplotlib
matplotlib.use("tkAgg")
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM11', 9600, timeout=5) #timeout of 5 to give python proper time to read bits
ser.flushInput()
#plot window of 60 seconds
plot_window = 60
y_var = np.array(np.zeros([plot_window]))

plt.ion()
fig, ax = plt.subplots()
plt.xlabel('Time (in seconds)',fontsize = 18)
plt.ylabel('Temperature (in degrees Celsius)', fontsize=18)
line, = ax.plot(y_var)

while True:
    try:
        #read bits from serial
        ser_bytes = ser.readline()
        try:
            #transform bytes into ascii code
            decoded_bytes = float(ser_bytes.decode("ascii"))
            print(ser_bytes.decode("ascii"))
        except:
            continue
        #graph data from MPU6050
        y_var = np.append(y_var,decoded_bytes)
        y_var = y_var[1:plot_window+1]
        line.set_ydata(y_var)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()
    except:
        print("Keyboard Interrupt")
        break