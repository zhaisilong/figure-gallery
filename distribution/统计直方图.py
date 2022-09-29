from pathlib import Path
import pandas as pd
from pandas import CategoricalDtype
from plotnine import *

DATA_DIR = Path('../data/distribution')
DATA = DATA_DIR / 'Distribution_Data.csv'

df = pd.read_csv(DATA)
df['class'] = df['class'].astype(CategoricalDtype(categories=["n", "s", "k", "mm"], ordered=True))

histogram_plot = (ggplot(df, aes(x="value", fill="class"))
                  + geom_histogram(alpha=1, colour="black", bins=30, size=0.2)
                  + facet_grid('class~.')
                  + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
                  + theme_light()
                  + theme(aspect_ratio=0.25,
                          dpi=100,
                          figure_size=(3, 4)))
print(histogram_plot)
