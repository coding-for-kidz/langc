"""
This file outputs a human-readable graph
"""
import matplotlib.pyplot as plt
import os
import time

def plot():
    """
    This will plot the data
    """
    stream = os.popen('%cd%/internalwindows/langc.exe')
    t1 = time.time()
    output = stream.read()
    t2 = time.time()
    print(t2 - t1)
    parse = output.split("\n\n")
    values = parse[0].split("\n")
    labels = parse[1].split("\n")
    labels.pop()
    fig1, ax1 = plt.subplots()

    ax1.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
