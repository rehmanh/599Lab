import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from scipy.interpolate import make_interp_spline
from datetime import datetime as dt


def read_datafiles():
    # sensor in lab
    inside_df = pd.read_table('/Users/rehmanh/Desktop/599/Lab/day1dat', header=None)
    # sensor outside
    outside_df = pd.read_table('/Users/rehmanh/Desktop/599/Lab/out1dat', header=None)
    # logfile
    logs_df = pd.read_table('/Users/rehmanh/Desktop/599/Lab/fixed_logs', header=None)
    return (inside_df, outside_df, logs_df)

def print_statistics(dataframe, location):
    # (date, time, temperature, pressure, humidity)
    temperature = []
    pressure = []
    humidity = []
    
    for index, row in dataframe.iterrows():
        r = row[0].split()
        temperature.append(float(r[2]))
        pressure.append(float(r[3]))
        humidity.append(float(r[4]))
    
    mean_temp = statistics.mean(temperature)
    mean_pres = statistics.mean(pressure)
    mean_humd = statistics.mean(humidity)

    medi_temp = statistics.median(temperature)
    medi_pres = statistics.median(pressure)
    medi_humd = statistics.median(humidity)

    print('Printing statistics for sensor placed: {}'.format(location))
    
    print("Mean Temperature: {}\nMean Pressure: {}\nMean Humidity: {}\n".format(mean_temp, mean_pres, mean_humd))
    print("Median Temperature: {}\nMedian Pressure: {}\nMedian Humidity: {}\n".format(medi_temp, medi_pres, medi_humd))
    
    print("Temperature Min: {} | Temperature Max: {}".format(min(temperature), max(temperature)))
    print("Pressure Min: {} | Pressure Max: {}".format(min(pressure), max(pressure)))
    print("Humidity Min: {} | Humidity Max: {}".format(min(humidity), max(humidity)))
    
    print("\n")

def detect_storm(dataframe):
    readings = []
    pressure = []
    humidity = []

    for index, row in dataframe.iterrows():
        r = row[0].split()
        readings.append(index)
        pressure.append(float(r[3]))
        humidity.append(float(r[4]))
    
    x = np.array(readings)
    # y = np.array(pressure)
    y = np.array(pressure)

    x_y_spline = make_interp_spline(x, y)

    x_interval = np.linspace(x.min(), x.max())
    y_interval = x_y_spline(x_interval)

    plt.plot(x_interval, y_interval)
    plt.title("Pressure Outside the Lab: 9/11/22 - 10/11/22")
    plt.xlabel("Reading Count")
    plt.ylabel("Pressure (mbar)")
    plt.show()

def detect_front(dataframe):
    readings = []
    temperature = []
    pressure = []
    humidity = []

    for index, row in dataframe.iterrows():
        r = row[0].split()
        readings.append(index)
        temperature.append(float(r[2]))
        pressure.append(float(r[3]))
        humidity.append(float(r[4]))


    # temp
    x = np.array(readings)
    y = np.array(temperature)

    x_y_spline = make_interp_spline(x, y)

    x_interval = np.linspace(x.min(), x.max())
    y_interval = x_y_spline(x_interval)

    plt.plot(x_interval, y_interval)
    plt.title("Temperature Outside the Lab: 31/10/23 - 3/11/23")
    plt.xlabel("Reading Count")
    plt.ylabel("Temperature (F)")
    plt.show()

    # pressure
    y = np.array(pressure)

    x_y_spline = make_interp_spline(x, y)

    x_interval = np.linspace(x.min(), x.max())
    y_interval = x_y_spline(x_interval)

    plt.plot(x_interval, y_interval)
    plt.title("Pressure Outside the Lab: 31/10/23 - 3/11/23")
    plt.xlabel("Reading Count")
    plt.ylabel("Pressure (mbar)")
    plt.show()

    # humidity
    y = np.array(humidity)

    x_y_spline = make_interp_spline(x, y)

    x_interval = np.linspace(x.min(), x.max())
    y_interval = x_y_spline(x_interval)

    plt.plot(x_interval, y_interval)
    plt.title("Humidity Outside the Lab: 31/10/23 - 3/11/23")
    plt.xlabel("Reading Count")
    plt.ylabel("Humidity (%)")
    plt.show()

if __name__ == '__main__':
    try:
        (inside, outside, logs) = read_datafiles()
    except:
        raise Exception("Error occurred reading the datafiles")
    
    # print_statistics(inside, "Inside The Lab")
    # print_statistics(outside, "Outside")
    # print_statistics(logs, "Logfile")

    #detect_storm(outside)
    detect_front(logs)
