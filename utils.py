import os
import numpy as np
import pandas as pd
import re
import pathlib
import json
from tqdm import tqdm,trange
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import matplotlib.pyplot as plt
import matplotlib
import time
import swifter
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from typing import Union, List
from copy import deepcopy
import pickle
from pprint import pprint

plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

## 查看dataframe的col_name列为item的行,item可以是List类型
def see_row(data:pd.DataFrame, col_name, item:Union[int,str,List[int],List[str]], reverse=False)->Union[pd.Series, pd.DataFrame]:
    if type(item)==str or type(item)==int:
        if reverse:
            return data[~(data[col_name]==item)]
        return data[data[col_name]==item]
    else:
        if len(item)>0:
            bools = np.array([False]*data.shape[0])
            for i in item:
                bools = bools|((data[col_name]==i).values)
            if reverse:
                return data[~bools]
            return data[bools]
        elif len(item)==0:
            if reverse:
                return data
            return pd.DataFrame(columns=data.columns)



## 把日期变到之后第n个交易日，当日期不在交易日列表范围内时特殊处理
## 输入：日期，交易日列表，n
def to_tradeday(date:str, tradedays_list:List, n=1):
    assert date>=tradedays_list[0], '日期在tradedays_list之前'
    assert date<=tradedays_list[-1], '日期在tradedays_list之后'
    if date not in tradedays_list:
        ## 如果date不是交易日，则把当前交易日（n=0）视为上一个交易日
        date = tradedays_list[(np.array(tradedays_list)<date).sum()-1]
        # if n>0:
        #     n=n-1
        if n<0:
            n=n+1
    if tradedays_list.index(date)+n<len(tradedays_list):
        return tradedays_list[tradedays_list.index(date)+n]
    return tradedays_list[-1]
## 获得两个日期之间间隔的交易日天数
## 输入：开始日期，结束日期，可以是长度相等的List；交易日列表；如果买入使用开盘，卖出使用收盘则最终间隔日期数加一
def trade_day_interval(start_day:Union[str,List[str]], end_day:Union[str,List[str]], tradedays_list, buy_open_sell_close=1)->Union[str,List[str]]:
    if type(start_day)==str and type(end_day)==str:
        start_day, end_day = to_tradeday(start_day, tradedays_list, 0), to_tradeday(end_day, tradedays_list, 0)
        return tradedays_list.index(end_day)-tradedays_list.index(start_day)+buy_open_sell_close
    else:
        assert len(start_day)==len(end_day), '日期数量不相等'
        start_day, end_day = [to_tradeday(i, tradedays_list, 0) for i in start_day], [to_tradeday(i, tradedays_list, 0) for i in end_day]
        return [tradedays_list.index(end_day[i])-tradedays_list.index(start_day[i])+buy_open_sell_close for i in range(len(start_day))]



## 标准化；通常是按日期进行pandas的groupby分组来用
EPS = 1e-12
def RobustCSZScoreNorm(x, clip_outlier=True):
    median = x.median()
    std = ((x-median).abs().median()+EPS)*1.4826
    x = (x-median)/std
    if clip_outlier:
        x.clip(-3,3, inplace=True)
    return x

