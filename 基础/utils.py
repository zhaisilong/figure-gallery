from typing import List

import numpy as np
import pandas as pd


def hist_point(x: List[float], bin_width: float = 0.3) -> pd.DataFrame:
    division = np.arange(x.min(), x.max(), bin_width)
    hist, bin_edges = np.histogram(x, bins=division, density=False)

    Hist_x = []
    Hist_y = []

    for i in range(0, len(bin_edges) - 1):
        for j in range(1, hist[i] + 1):
            Hist_x.append((bin_edges[i] + bin_edges[i + 1]) / 2)
            Hist_y.append(j)

    return pd.DataFrame(dict(x=Hist_x, count=Hist_y))
