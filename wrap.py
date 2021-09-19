"""
This file outputs a human readable graph
"""
import matplotlib.pyplot as plt
from core import *


def plot():
    """
    This will plot the data
    """
    get_all()
    p = get_percents(find_langs())
    print(p)
    values = []
    labels = []
    colors = []
    color = {"python": "blue", "html": "red", "css": "cyan", "js": "orange"}
    for item in p:
        values.append(p[item])
        labels.append(item)
        colors.append(color[item])
    fig1, ax1 = plt.subplots()

    ax1.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
        colors=colors,
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


plot()
