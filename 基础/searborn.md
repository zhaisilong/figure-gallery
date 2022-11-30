# Seaborn

- seaborn 函数中多余的关键词参数会传给 matlibplot 层

## 数据

```python
dots = sns.load_dataset("dots")
```

tips, iris, fmri

## 设置

```python
seaborn.set(context='notebook', style='darkgrid', 
palette='deep', font='sans-serif', font_scale=1, 
color_codes=True, rc=None)

sns.set(rc={'figure.figsize':(6,6)})
```

- context: paper, notebook, talk, poster
- style: darkgrid , whitegrid, dark , white ,和 ticks

```python
sns.axes_style()

{'axes.axisbelow': True,  #轴在图形的下面
'axes.edgecolor': 'white',    #边框的颜色
'axes.facecolor': '#EAEAF2',    #背景颜色
'axes.grid': True,    #是否显示网格
'axes.labelcolor': '.15',
'axes.linewidth': 0.0,
'figure.facecolor': 'white',
'font.family': ['sans-serif'],
'font.sans-serif': ['Arial',
'Liberation Sans',
'Bitstream Vera Sans',
'sans-serif'],
'grid.color': 'white',
'grid.linestyle': '-',
'image.cmap': 'Greys',
'legend.frameon': False,
'legend.numpoints': 1,
'legend.scatterpoints': 1,
'lines.solid_capstyle': 'round',
'text.color': '.15',
'xtick.color': '.15',
'xtick.direction': 'out',
'xtick.major.size': 0.0,
'xtick.minor.size': 0.0,
'ytick.color': '.15',
'ytick.direction': 'out',
'ytick.major.size': 0.0,
'ytick.minor.size': 0.0}
```



## 函数

- lmplot: 线性回归
- 估计与误差
  - replot
    - kind 参数设置成 line,有 95% 误差区间
- 分类
  - catplot(散点图)
    - kind
      - swarm
      - violin
      - bar

## 多图

### col 参数: 一列两图,按时间

```python
sns.lmplot(x="total_bill", y="tip", col="time", hue="smoker",
           data=tips);
```

### 轴操作

axes-level 函数返回一个 matplotlib axes，figure-level 函数返回一个 FacetGrid

```python
f, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.boxplot(x="day", y="tip", data=tips, ax=axes[0])
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips, ax=axes[1]);

sns.relplot(x="time", y="firing_rate", col="align",
            hue="choice", size="coherence", style="choice",
            height=4.5, aspect=2 / 3,
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=dots);
```

```python
sns.despine()  # 去掉图像上面和右面的刻度和轴线
sns.despine(offset=10)  # 画的图离轴线的距离
sns.set_context(fontscale=1.5, rc={'lines.linewidth':1.5)  # 曲线的宽度
sns.set_context(fontscale=1.5)  # 分度值的字体大小

```

### 数据集结构可视化: 多变量

```python
iris = sns.load_dataset("iris")
sns.jointplot(x="sepal_length", y="petal_length", data=iris);
```

```python
sns.pairplot(data=iris, hue="species");
```

## 色板

色彩推荐

分类：hls husl Paired Set1~Set3（色调不同）
连续：Blues[蓝s，颜色+s] BuGn[蓝绿] cubehelix（同色系渐变）
离散：BrBG[棕绿] RdBu[红蓝] coolwarm[冷暖]（双色对称）

### 定性调色

```python
current_palette = sns.color_palette()
sns.palplot(current_palette)
```

默认主题有六种变体

![](http://img.zhaisilong.com/202211292314279.png)

#### hls 颜色空间,定性,简单的 RGB 值变体

```python
sns.palplot(sns.color_palette("hls", 8))
sns.palplot(sns.hls_palette(8, l=.3, s=.8))
sns.palplot(sns.color_palette("husl", 8))  # 更好看的,与上面的等价
```

#### color brewer 调色板

```python
sns.palplot(sns.color_palette("Paired"))
sns.palplot(sns.color_palette("Set2"))
# 自定义
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.palplot(sns.color_palette(flatui))
```

### 顺序调色

```python
sns.palplot(sns.color_palette("Blues"))
sns.palplot(sns.color_palette("BuGn_r"))  # 逆序
sns.palplot(sns.color_palette("GnBu_d"))  # 缩小范围到较深区间

# cubehelix 生成
sns.palplot(sns.cubehelix_palette())

```

### 发散调色板

```python
seaborn.set_palette(palette, n_colors=None, desat=None, color_codes=False)
m=sns.color_palette(palette='bright',n_colors=4 )
```