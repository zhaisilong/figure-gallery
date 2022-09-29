from pathlib import Path
import pandas as pd
from pandas import CategoricalDtype
from plotnine import *

DATA_DIR = Path('../data/distribution')
DATA = DATA_DIR / 'Distribution_Data.csv'

df = pd.read_csv(DATA)
df['class'] = df['class'].astype(CategoricalDtype(categories=["n", "s", "k", "mm"], ordered=True))

# 多图
density_plot = (ggplot(df, aes(x="value", fill="class"))
                + geom_density(alpha=1)
                + facet_grid('class~.')
                + scale_fill_brewer(palette=6, type="qualitative")
                + scale_fill_hue(s=0.90, l=0.65, h=0.0417, color_space='husl')
                + theme_light()
                + theme(aspect_ratio=0.25,
                        dpi=100,
                        figure_size=(3, 4)))
print(density_plot)

# 单图
single_density_plot = (ggplot(df, aes(x="value"))
                + geom_density(alpha=1))
print(single_density_plot)
