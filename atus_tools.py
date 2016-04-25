import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def to_plot_category_vs_x(data,category_name,x_name,reduce_type,**kwargs):
    grouped = data.groupby([x_name,category_name])
    if reduce_type.lower() == "mean":
        reduced = grouped.mean()
    to_plot = reduced.unstack()
    return to_plot
