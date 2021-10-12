"""
This file outputs a human-readable graph
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
    for item in p:
        values.append(p[item])
        labels.append(item)
    fig1, ax1 = plt.subplots()

    ax1.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


plot()
