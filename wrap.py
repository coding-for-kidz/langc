"""
This file outputs a human-readable graph
"""
import os
import platform

import matplotlib.pyplot as plt


def plot():
    """
    This will plot the data
    """
    stream = ""
    if platform.system() == "Windows":
        stream = os.popen("%cd%/internalwindows/langc.exe")
    elif platform.system() == "Linux":
        stream = os.popen("./internallinux/langc")
    elif platform.system() == "Darwin":
        pass
    output = stream.read()
    parse = output.split("\n\n")
    values = parse[0].split("\n")
    labels = parse[1].split("\n")
    labels.pop()
    fig1, ax1 = plt.subplots()

    ax1.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
