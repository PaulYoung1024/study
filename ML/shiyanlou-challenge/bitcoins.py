
# coding: utf-8

# <img style="float: right;" src="https://img.shields.io/badge/%E6%A5%BC+-%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98-red.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iOXB4IiBoZWlnaHQ9IjE0cHgiIHZpZXdCb3g9IjAgMCA5IDE0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgogICAgPCEtLSBHZW5lcmF0b3I6IFNrZXRjaCA1Mi4yICg2NzE0NSkgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+CiAgICA8dGl0bGU+c2hpeWFubG91X2xvZ288L3RpdGxlPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iUGFnZS0xIiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4KICAgICAgICA8ZyBpZD0ic2hpeWFubG91X2xvZ28iIGZpbGw9IiMwOEJGOTEiIGZpbGwtcnVsZT0ibm9uemVybyI+CiAgICAgICAgICAgIDxnIGlkPSLlvaLnirZfMTBf5ou36LSdXzNfMzRfIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik00LjUyNTU4MTQsMC4yNjA0NjUxMTYgQzQuNTI1NTgxNCwwLjI2MDQ2NTExNiAxLjQ5NzY3NDQyLDQuMiAwLjU1MzQ4ODM3Miw1Ljk5MDY5NzY3IEMtMC40MjMyNTU4MTQsNy44MTM5NTM0OSAxLjU5NTM0ODg0LDEwLjA5MzAyMzMgMS41OTUzNDg4NCwxMC4wOTMwMjMzIEMxLjU5NTM0ODg0LDEwLjA5MzAyMzMgNC44MTg2MDQ2NSw1LjE3Njc0NDE5IDUuMjA5MzAyMzMsNC42MjMyNTU4MSBDNi4zNDg4MzcyMSwyLjk2Mjc5MDcgNC41MjU1ODE0LDAuMjYwNDY1MTE2IDQuNTI1NTgxNCwwLjI2MDQ2NTExNiBaIE03LjQyMzI1NTgxLDMuOTA2OTc2NzQgQzcuNDIzMjU1ODEsMy45MDY5NzY3NCA0LjM5NTM0ODg0LDcuODQ2NTExNjMgMy40NTExNjI3OSw5LjYzNzIwOTMgQzIuNDc0NDE4NiwxMS40Mjc5MDcgNC41MjU1ODE0LDEzLjczOTUzNDkgNC41MjU1ODE0LDEzLjczOTUzNDkgQzQuNTI1NTgxNCwxMy43Mzk1MzQ5IDcuNzQ4ODM3MjEsOC44MjMyNTU4MSA4LjEzOTUzNDg4LDguMjY5NzY3NDQgQzkuMjEzOTUzNDksNi42MDkzMDIzMyA3LjQyMzI1NTgxLDMuOTA2OTc2NzQgNy40MjMyNTU4MSwzLjkwNjk3Njc0IFoiIGlkPSLlvaLnirYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+&longCache=true&style=flat-square"></img>

# # 比特币价格预测挑战

# ---

# ### 挑战介绍

# ![image](https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531374478384.png)

# > 比特币（英语：Bitcoin，缩写：BTC）被部分观点认为是一种去中心化，非普遍全球可支付的电子加密货币，而多数国家则认为比特币属于虚拟商品，并非货币。比特币由中本聪（化名）于 2009 年 1 月 3 日，基于无国界的对等网络，用共识主动性开源软件发明创立。自比特币出现至今为止，比特币一直是目前法币市场总值最高的加密货币。([维基百科](https://zh.wikipedia.org/wiki/%E6%AF%94%E7%89%B9%E5%B8%81))
# 
# 一段时间以来，比特币的价值饱受质疑。有人认为是严重的「泡沫」，也有人认为是物有所值。但无论哪一种观点，我们都见证了比特币暴涨暴跌。本次挑战收集到了 `2010-2018` 年比特币历史数据。其中包含交易价格、区块数量、交易费率等信息。我们将尝试使用多项式回归和岭回归方法来预测比特币价格变化趋势。

# ### 挑战知识点

# - 使用 Pandas 数据处理
# - 使用 Matplotlib 绘图
# - 使用 scikit-learn 训练多项式回归预测模型

# ---

# ## 挑战内容

# ### 数据准备

# 首先，需要导入比特币历史数据集，并预览数据集前 5 行。数据集名称为 `challenge-2-bitcoin.csv`。

# In[1]:


# 下载数据集
get_ipython().system('wget -nc http://labfile.oss.aliyuncs.com/courses/1081/challenge-2-bitcoin.csv')


# ---

# **<font color='red'>挑战</font>：使用 Pandas 加载数据集 CSV 文件，并预览前 `5` 行数据。**

# In[ ]:


import pandas as pd

### 代码开始 ### (≈ 2 行代码)
df = None
### 代码结束 ###


# In[2]:


import numpy as np
import pandas as pd
df=pd.read_csv("challenge-2-bitcoin.csv")
df.head()


# **期望输出：**

# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Date</th>
#       <th>btc_market_price</th>
#       <th>btc_total_bitcoins</th>
#       <th>btc_market_cap</th>
#       <th>btc_trade_volume</th>
#       <th>btc_blocks_size</th>
#       <th>btc_avg_block_size</th>
#       <th>btc_n_orphaned_blocks</th>
#       <th>btc_n_transactions_per_block</th>
#       <th>btc_median_confirmation_time</th>
#       <th>...</th>
#       <th>btc_cost_per_transaction_percent</th>
#       <th>btc_cost_per_transaction</th>
#       <th>btc_n_unique_addresses</th>
#       <th>btc_n_transactions</th>
#       <th>btc_n_transactions_total</th>
#       <th>btc_n_transactions_excluding_popular</th>
#       <th>btc_n_transactions_excluding_chains_longer_than_100</th>
#       <th>btc_output_volume</th>
#       <th>btc_estimated_transaction_volume</th>
#       <th>btc_estimated_transaction_volume_usd</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>2010-02-23 00:00:00</td>
#       <td>0.0</td>
#       <td>2110700.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.000216</td>
#       <td>0.0</td>
#       <td>1.0</td>
#       <td>0.0</td>
#       <td>...</td>
#       <td>25100.000000</td>
#       <td>0.0</td>
#       <td>252.0</td>
#       <td>252.0</td>
#       <td>42613.0</td>
#       <td>252.0</td>
#       <td>252.0</td>
#       <td>12600.0</td>
#       <td>50.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>2010-02-24 00:00:00</td>
#       <td>0.0</td>
#       <td>2120200.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.000282</td>
#       <td>0.0</td>
#       <td>1.0</td>
#       <td>0.0</td>
#       <td>...</td>
#       <td>179.245283</td>
#       <td>0.0</td>
#       <td>195.0</td>
#       <td>196.0</td>
#       <td>42809.0</td>
#       <td>196.0</td>
#       <td>196.0</td>
#       <td>14800.0</td>
#       <td>5300.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>2010-02-25 00:00:00</td>
#       <td>0.0</td>
#       <td>2127600.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.000227</td>
#       <td>0.0</td>
#       <td>1.0</td>
#       <td>0.0</td>
#       <td>...</td>
#       <td>1057.142857</td>
#       <td>0.0</td>
#       <td>150.0</td>
#       <td>150.0</td>
#       <td>42959.0</td>
#       <td>150.0</td>
#       <td>150.0</td>
#       <td>8100.0</td>
#       <td>700.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>2010-02-26 00:00:00</td>
#       <td>0.0</td>
#       <td>2136100.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.000319</td>
#       <td>0.0</td>
#       <td>1.0</td>
#       <td>0.0</td>
#       <td>...</td>
#       <td>64.582059</td>
#       <td>0.0</td>
#       <td>176.0</td>
#       <td>176.0</td>
#       <td>43135.0</td>
#       <td>176.0</td>
#       <td>176.0</td>
#       <td>29349.0</td>
#       <td>13162.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>2010-02-27 00:00:00</td>
#       <td>0.0</td>
#       <td>2144750.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.0</td>
#       <td>0.000223</td>
#       <td>0.0</td>
#       <td>1.0</td>
#       <td>0.0</td>
#       <td>...</td>
#       <td>1922.222222</td>
#       <td>0.0</td>
#       <td>176.0</td>
#       <td>176.0</td>
#       <td>43311.0</td>
#       <td>176.0</td>
#       <td>176.0</td>
#       <td>9101.0</td>
#       <td>450.0</td>
#       <td>0.0</td>
#     </tr>
#   </tbody>
# </table>

# 可以看到，原数据集中包含的数据较多，本次挑战中只使用其中的 3 列，分布是：**比特币市场价格**、**比特币总量**、**比特币交易费用**。它们对应的列名依次为：`btc_market_price`，`btc_total_bitcoins`，`btc_transaction_fees`。

# ---

# **<font color='red'>挑战</font>：分离出仅包含 `btc_market_price`，`btc_total_bitcoins`，`btc_transaction_fees` 列的 DataFrame，并定义为变量 `data`。**

# In[ ]:


"""从原数据集中分离出需要的数据集（DataFrame）
"""

### 代码开始 ### (≈ 1 行代码)
data = 
### 代码结束 ###


# In[3]:


data=df[['btc_market_price','btc_total_bitcoins','btc_transaction_fees']]
data.head()


# **运行测试：**

# In[ ]:


data.head()


# **期望输出：**

# <table border="1" class="dataframe">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>btc_market_price</th>
#       <th>btc_total_bitcoins</th>
#       <th>btc_transaction_fees</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>0.0</td>
#       <td>2110700.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>0.0</td>
#       <td>2120200.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>0.0</td>
#       <td>2127600.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>0.0</td>
#       <td>2136100.0</td>
#       <td>0.0</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>0.0</td>
#       <td>2144750.0</td>
#       <td>0.0</td>
#     </tr>
#   </tbody>
# </table>

# 下面，我们将 3 列数据，分别绘制在横向排列的 3 张子图中。

# ---

# **<font color='red'>挑战</font>：分别绘制 `data` 数据集 3 列数据的线形图，并以横向子图排列。**

# **<font color='brown'>要求</font>**：需设置各图横纵轴名称，横轴统一为 `time`，纵轴为各自列名称。

# **<font color='green'>提示</font>**：使用 `set_xlabel()` 设置横轴名称。

# In[ ]:


"""绘制数据图像
"""

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16,5))


### 代码开始 ### (≈ 9 行代码)


### 代码结束 ###


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(16,5))

axes[0].plot(data.index,data['btc_market_price'],'green')
axes[0].set_xlabel('time')
axes[0].set_ylabel('btc_market_price')

axes[1].plot(data.index,data['btc_total_bitcoins'],'blue')
axes[1].set_xlabel('time')
axes[1].set_ylabel('btc_total_bitcoins')

axes[2].plot(data.index,data['btc_transaction_fees'],'red')
axes[2].set_xlabel('time')
axes[2].set_ylabel('btc_transaction_fees')


# **期望输出（可忽略颜色）：**

# <img width="600px" src="https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531374478620.png"></img>

# 本次挑战中，数据集的特征（features）是`比特币总量`和`比特币交易费用`，而目标值为`比特币市场价格`。所以，下面将数据集拆分为训练集和测试集。其中，训练集占 `70%`，而测试集占 `30%`。

# ---

# **<font color='red'>挑战</font>：划分 `data` 数据集，使得训练集占 `70%`，而测试集占 `30%`。**

# **<font color='brown'>要求</font>**：训练集特征、训练集目标、测试集特征、测试集目标分别定义为 `train_x`, `train_y`, `test_x`, `test_y`，并作为 `split_dataset()` 函数返回值。

# In[ ]:


"""划分数据集函数
"""

def split_dataset():
    """
    参数:
    无

    返回:
    train_x, train_y, test_x, test_y -- 训练集特征、训练集目标、测试集特征、测试集目标
    """
    
    ### 代码开始 ### (≈ 6 行代码)

    
    ### 代码结束 ###
    
    return train_x, train_y, test_x, test_y


# In[14]:


def split_dataset():
    features=data[['btc_total_bitcoins','btc_transaction_fees']]
    target=data['btc_market_price']
    split_num=int(len(data)*0.7)
    
    train_x=features[:split_num]
    train_y=target[:split_num]
    
    test_x=features[split_num:]
    test_y=target[split_num:]
    
    return train_x,train_y,test_x,test_y


# **运行测试：**

# In[15]:


len(split_dataset()[0]),len(split_dataset()[1]),len(split_dataset()[2]),len(split_dataset()[3]),split_dataset()[0].shape,split_dataset()[1].shape,split_dataset()[2].shape,split_dataset()[3].shape


# In[ ]:


len(split_dataset()[0]), len(split_dataset()[1]), len(split_dataset()[2]), len(split_dataset()[3]), split_dataset()[0].shape, split_dataset()[1].shape, split_dataset()[2].shape, split_dataset()[3].shape


# **期望输出：**

# <div align="center">**`(2043, 2043, 877, 877, (2043, 2), (2043, 1), (877, 2), (877, 1))`**</div>

# ### 3 次多项式回归预测挑战

# 划分完训练数据和测试数据之后，就可以构建多项式回归预测模型。挑战要求使用 scikit-learn 完成。

# In[18]:


# 加载必要模块
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 加载数据
train_x = split_dataset()[0]
train_y = split_dataset()[1]
test_x = split_dataset()[2]
test_y = split_dataset()[3]


# In[20]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

train_x=split_dataset()[0]
train_y=split_dataset()[1]
test_x=split_dataset()[2]
test_y=split_dataset()[3]


# ---

# **<font color='red'>挑战</font>：构建 3 次多项式回归预测模型**

# **<font color='brown'>要求</font>**：使用 scikit-learn 构建 3 次多项式回归预测模型，并计算预测结果的 MAE 评价指标，同时作为 `poly3()` 函数返回值。

# In[ ]:


"""3 次多项式回归预测模型
"""

def poly3():
    
    """
    参数:
    无

    返回:
    mae -- 预测结果的 MAE 评价指标
    """
    
    ### 代码开始 ### (≈ 7 行代码)

    
    ### 代码结束 ###
    
    return mae


# In[25]:


def poly3():
    poly_features=PolynomialFeatures(degree=3,include_bias=False)
    poly_train_x=poly_features.fit_transform(train_x)
    poly_test_x=poly_features.fit_transform(test_x)
    
    model=LinearRegression()
    model.fit(poly_train_x,train_y)
    
    mae=mean_absolute_error(test_y,model.predict(poly_test_x).flatten())
    return mae


# **运行测试：**

# In[26]:


poly3()


# **期望输出：**

# <div align="center">**`1955.8027790596564`**</div>

# ### N 次多项式回归预测绘图

# 接下来，针对不同的多项式次数，计算相应的 MSE 评价指标数值并绘图。

# ---

# **<font color='red'>挑战</font>：计算 `1,2,...,10` 次多项式回归预测结果的 `MSE` 评价指标**

# **<font color='brown'>要求</font>**：使用 scikit-learn 构建 N 次多项式回归预测模型，并计算 `1-10` 次多项式预测结果的 MSE 评价指标，同时作为函数 `poly_plot(N)` 的返回值。

# In[ ]:


"""N 次多项式回归预测模型
"""

from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

def poly_plot(N):
 
    """
    参数:
    N -- 标量, 多项式次数

    返回:
    mse -- N 次多项式预测结果的 MSE 评价指标列表
    """
    
    m = 1
    mse = []
    
    ### 代码开始 ### (≈ 6 行代码)

    
    ### 代码结束 ###
    
    return mse


# In[34]:


from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

def poly_plot(N):
    m=1
    mse=[]
    
    for m in np.arange(1,N+1):
        poly_features=PolynomialFeatures(degree=m,include_bias=False)
        poly_train_x=poly_features.fit_transform(train_x)
        poly_test_x=poly_features.fit_transform(test_x)
        
        model=LinearRegression()
        model.fit(poly_train_x,train_y)
        
        MSE=mean_squared_error(test_y,model.predict(poly_test_x).flatten())
        mse.append(MSE)
    return mse


# In[28]:


np.arange(1,10)


# **运行测试：**

# In[35]:


poly_plot(10)[:10:3]


# **期望输出（结果可能会稍有出入）：**

# <div align="center">**`[24171680.63629423, 23772159.453013, 919854753.0234015, 3708858661.222856]`**</div>

# ---

# **<font color='red'>挑战</font>：将 `MSE` 评价指标绘制成线型图**

# **<font color='brown'>要求</font>**：将 `poly_plot(10)` 返回的 `MSE` 列表绘制成组合图（线形图+散点图）。其中，线型图为红色。

# In[ ]:


mse = poly_plot(10)

### 代码开始 ### (≈ 2 行代码)

### 代码结束 ###

plt.title("MSE")
plt.xlabel("N")
plt.ylabel("MSE")


# In[46]:


mse=poly_plot(10)
#plt.plot([i for i in range(1,11)],mse,'red')
plt.plot(range(1,11),mse,'r')
plt.scatter([i for i in range(1,11)],mse)
plt.title("MSE")
plt.xlabel("N")
plt.ylabel("MSE")


# In[43]:


range(1,11)


# **期望输出：**

# ![image](https://doc.shiyanlou.com/document-uid214893labid6102timestamp1531374478818.png)

# ---

# <img src="https://img.shields.io/badge/%E5%AE%9E%E9%AA%8C%E6%A5%BC-%E7%89%88%E6%9D%83%E6%89%80%E6%9C%89-lightgrey.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iOXB4IiBoZWlnaHQ9IjE0cHgiIHZpZXdCb3g9IjAgMCA5IDE0IiB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgogICAgPCEtLSBHZW5lcmF0b3I6IFNrZXRjaCA1Mi4yICg2NzE0NSkgLSBodHRwOi8vd3d3LmJvaGVtaWFuY29kaW5nLmNvbS9za2V0Y2ggLS0+CiAgICA8dGl0bGU+c2hpeWFubG91X2xvZ288L3RpdGxlPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iUGFnZS0xIiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4KICAgICAgICA8ZyBpZD0ic2hpeWFubG91X2xvZ28iIGZpbGw9IiMwOEJGOTEiIGZpbGwtcnVsZT0ibm9uemVybyI+CiAgICAgICAgICAgIDxnIGlkPSLlvaLnirZfMTBf5ou36LSdXzNfMzRfIj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik00LjUyNTU4MTQsMC4yNjA0NjUxMTYgQzQuNTI1NTgxNCwwLjI2MDQ2NTExNiAxLjQ5NzY3NDQyLDQuMiAwLjU1MzQ4ODM3Miw1Ljk5MDY5NzY3IEMtMC40MjMyNTU4MTQsNy44MTM5NTM0OSAxLjU5NTM0ODg0LDEwLjA5MzAyMzMgMS41OTUzNDg4NCwxMC4wOTMwMjMzIEMxLjU5NTM0ODg0LDEwLjA5MzAyMzMgNC44MTg2MDQ2NSw1LjE3Njc0NDE5IDUuMjA5MzAyMzMsNC42MjMyNTU4MSBDNi4zNDg4MzcyMSwyLjk2Mjc5MDcgNC41MjU1ODE0LDAuMjYwNDY1MTE2IDQuNTI1NTgxNCwwLjI2MDQ2NTExNiBaIE03LjQyMzI1NTgxLDMuOTA2OTc2NzQgQzcuNDIzMjU1ODEsMy45MDY5NzY3NCA0LjM5NTM0ODg0LDcuODQ2NTExNjMgMy40NTExNjI3OSw5LjYzNzIwOTMgQzIuNDc0NDE4NiwxMS40Mjc5MDcgNC41MjU1ODE0LDEzLjczOTUzNDkgNC41MjU1ODE0LDEzLjczOTUzNDkgQzQuNTI1NTgxNCwxMy43Mzk1MzQ5IDcuNzQ4ODM3MjEsOC44MjMyNTU4MSA4LjEzOTUzNDg4LDguMjY5NzY3NDQgQzkuMjEzOTUzNDksNi42MDkzMDIzMyA3LjQyMzI1NTgxLDMuOTA2OTc2NzQgNy40MjMyNTU4MSwzLjkwNjk3Njc0IFoiIGlkPSLlvaLnirYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+&longCache=true&style=flat-square"></img>
