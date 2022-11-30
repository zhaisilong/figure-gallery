import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

figure(num=None, figsize=(2.8, 1.7), dpi=300)
# figsize的2.8和1.7指的是英寸，dpi指定图片分辨率。那么图片就是（2.8*300）*（1.7*300）像素大小

plt.plot(test_mean_1000S_n, 'royalblue', label='without threshold')
plt.plot(test_mean_1000S, 'darkorange', label='with threshold')

# 画图，并指定颜色
plt.xticks(fontproperties='Times New Roman', fontsize=8)
plt.yticks(np.arange(0, 1.1, 0.2),
           fontproperties='Times New Roman', fontsize=8)
# 指定横纵坐标的字体以及字体大小，记住是fontsize不是size。yticks上我还用numpy指定了坐标轴的变化范围。

plt.legend(loc='lower right', prop={'family': 'Times New Roman', 'size': 8})
# 图上的legend，记住字体是要用prop以字典形式设置的，而且字的大小是size不是fontsize，这个容易和xticks的命令弄混

plt.title('1000 samples', fontdict={'family': 'Times New Roman', 'size': 8})
# 指定图上标题的字体及大小

plt.xlabel('iterations', fontdict={'family': 'Times New Roman', 'size': 8})
plt.ylabel('accuracy', fontdict={'family': 'Times New Roman', 'size': 8})
# 指定横纵坐标描述的字体及大小

plt.savefig('F:/where-you-want-to-save.png', dpi=300, bbox_inches="tight")
# 保存文件，dpi指定保存文件的分辨率
# bbox_inches="tight" 可以保存图上所有的信息，不会出现横纵坐标轴的描述存掉了的情况

plt.show()
# 记住，如果你要show()的话，一定要先savefig，再show。如果你先show了，存出来的就是一张白纸。
