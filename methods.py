"""contributor------LD"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pylab as mpl     

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 设置DataFrame中文显示对齐
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)


def transition(name,n=50):
    '''
    过度行，长度50个减号，效果如下：
    ---------------过度-----------
    不论输入为奇数还是偶数，长度都控制在50
    '''
    numbers = (n - len(name)*2)//2
    print('-'*numbers+name+'-'*numbers)
    
    
def variable_show(data):
    '''
    显示DataFrame的变量信息
    离散变量多少个，每个变量取值个数多少
    连续变量同上
    '''
    object_data = data.select_dtypes(include='O')
    object_data = pd.DataFrame({
        '离散型变量'+(str(len(object_data.columns)))+'个':[i for i in object_data],
        '  ':[' ' for i in object_data],
        '取值个数':[len(object_data[i].unique()) for i in object_data],
        '占比':[len(object_data[i].unique())/len(data) for i in object_data],
        '  ':[' ' for i in object_data]})
    
    num_data = data.select_dtypes(exclude='O')
    num_data = pd.DataFrame({
        '  ':[' ' for i in num_data],
        '连续型变量'+(str(len(num_data.columns)))+'个':[i for i in num_data],
        '  ':[' ' for i in num_data],
        '取值个数':[len(num_data[i].unique()) for i in num_data],
        '占比':[len(num_data[i].unique())/len(data) for i in num_data]})
    return pd.concat([object_data,num_data],axis=1).fillna(' ')

def show_info(data,n=50):
    '''
    输出DataFrame的基本信息，将常用方法封装
    '''
    transition('前五行')
    print(data.head())
    
    transition('形状')
    print(data.shape)
    
    transition('空值')
    print(data.isnull().sum())
    
    transition('重复值')
    print(data.duplicated().sum())
    
    transition('变量统计')
    print(variable_show(data))
    
    
# 离散变量可视化
def discrete_show(data,figsize=(12,8),sort=None,titlesize=20,fontsize=15,datasize=11,color='steelblue',labelrotation=0):
    select_data = data.select_dtypes(include='O')

    titlesize = titlesize
    fontsize = fontsize
    datasize = datasize
    
    for i in select_data:
        
        if sort == 'up':
            fig_data = select_data[i].value_counts(ascending=True)
        elif sort == 'down':
            fig_data = select_data[i].value_counts()
        else:
            fig_data = select_data[i].value_counts().sort_index()

        
        fig,ax = plt.subplots(figsize=figsize)
        ax = fig_data.plot(kind='bar',rot=0,color=color)
        
        ax.set_title(i,fontsize=titlesize)
        ax.tick_params(labelsize=fontsize,labelrotation=labelrotation)
        
        j = range(len(fig_data))
        k = fig_data.values

        for a,b in zip(j,k):
            ax.text(a,b, '%.0f' % b, ha='center',va='bottom', fontsize=datasize)
  
        plt.show()

    
# 连续值分布可视化
def num_show(data,col=3,figsize=(12,8),titlesize = 20,fontsize = 15,wspace=0.5,hspace=0.2,labelrotation=0):
    num_data = data.select_dtypes(exclude='O')
    col = col
    row = round(len(num_data.columns)/col)

    titlesize = titlesize
    fontsize = fontsize
    
    fig,ax = plt.subplots(row,col,figsize=figsize)
    ax = ax.flat
    n = 0
    for i in num_data:

        sns.kdeplot(num_data[i],shade=True,ax = ax[n])
        ax[n].set_title(i,fontsize=titlesize)
        ax[n].tick_params(labelsize=fontsize,labelrotation=labelrotation)

        n += 1
    plt.subplots_adjust(wspace=wspace,hspace=hspace)
    plt.show()
    
    
    
    
# 离散型×连续型 交叉分析
def cross_show(data,x,y,kind='kde',row=3,col=3,figsize=(12,8),titlesize=20,fontsize=15,wspace=0.5,hspace=0.2,labelrotation=0):

    col = col
    row = row

    titlesize = titlesize
    fontsize = fontsize
    
    fig,ax = plt.subplots(row,col,figsize=figsize)
    ax = ax.flat
    n = 0
    
    if row*col<len(data.groupby(x)):
        print('wrong：子图行列数与分组数不一致')
    
    
    for i in  data.groupby(x):
        if kind == 'distplot':
            sns.distplot(i[1][y],kde_kws={"color": "steelblue", "lw": 2},ax = ax[n])
        else:
            sns.kdeplot(i[1][y],shade=True,ax = ax[n])
        ax[n].set_title(i[0],fontsize=titlesize)
        min_max = data[y].max()/10
        ax[n].set_xlim(data[y].min()-min_max,data[y].max()+min_max)  
        ax[n].tick_params(labelsize=fontsize,labelrotation=0)

        n += 1
    plt.subplots_adjust(hspace=hspace,wspace=wspace)
    plt.show()

# 离散型×连续型 汇总
def total_cross(data,x,y,height=8):
    pairgrid = sns.pairplot(
                    data=data[[x,y]],
                    hue=x,
                    height=height)
    plt.legend()
    plt.show()
    
    
# 离散特征两两交叉组合
def discrete_group(data):
    
    object_columns = data.select_dtypes(include='O').columns.tolist()
    object_group = [[object_columns[i],object_columns[j]] for i in range(len(object_columns)) for j in range(i+1,len(object_columns)) ]
    return object_group
    
# 得到相关矩阵
def corr_tril(data,method="pearson"):
    corr_data = data.corr(method = method)  # 相关矩阵
    mask = np.ones(corr_data.shape)  # 构造相关矩阵 bool型
    mask[np.triu_indices_from(mask)] = 0  # 设置对角线(mask)
    return mask*corr_data

# 计算众数
def mode(data):
    mode_data = pd.DataFrame({
        '变量':[i for i in data],
        '众数':[data[i].value_counts().index[0] for i in data],
        '占比':[str(round(data[i].value_counts().values[0]/len(data)*100,1))+'%' for i in data] 
    })
    return mode_data



# 统计每列特征的数据类型个数，以及每列是否需要处理，以及每个特征数据类型的索引
def type_count(data):
    percent = []
    type_index = {}
    for i in data.columns:
        meta_dict = {'int':0,'float':0,'str':0,'Null':0}
        type_index[i] = {'int':[],'float':[],'str':[],'Null':[]}

        for j in zip(data[i].index,data[i]):
            val = str(j[1])
            if pd.isnull(j[1]):
                meta_dict['Null'] += 1
                type_index[i]['Null'].append(j[0])
            else:
                if val.replace('.','',1).isdigit():
                    if '.' in val:
                        meta_dict['float'] += 1
                        type_index[i]['float'].append(j[0])

                    else:
                        meta_dict['int'] += 1
                        type_index[i]['int'].append(j[0])

                else:
                    meta_dict['str'] += 1
                    type_index[i]['str'].append(j[0])
        percent.append(meta_dict)
        
        
    count = pd.DataFrame(percent,index=data.columns)
    count['数据一致'] = [ 'right' if i==3 else '需要处理' for i in count.T.replace(0,np.nan).isnull().sum().values]
    return count,type_index

__version__ = "0.1"
