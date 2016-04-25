import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from atus_tools import *


def test_to_plot_category_vs_x():
    a = pd.DataFrame({'value':np.arange(30)})
    a['even'] = [x%2 == 0 for x in a.value]
    a['fours'] = [x//4 for x in a.value]
    b = to_plot_category_vs_x(a,'even','fours',"mean")["value"]
    tuples2=[(False,),(True,)]
    index2 = pd.MultiIndex.from_tuples(tuples2, names=['even'])
    idx2 = pd.Series(list(range(8))).rename("fours")
    df2 = pd.DataFrame([[2,1],[6,5],[10,9],[14,13],[18,17],[22,21],[26,25],[29,28]],index = idx2,columns=index2)
    assert b.equals(df2)
