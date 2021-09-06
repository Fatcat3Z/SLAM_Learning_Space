import csv
import pandas as pd
import sys


# 从包含GPS信息的csv文件中筛选需要的GPS数据帧
# datatype的输入格式datatype = ['GPGGA', 'GPTRA', 'HEADING']
# 将上述datatype中包含的GPS帧数据删除
# 常用的GPS语句为KSXT 包含经纬度 欧拉角 rtk结算坐标值 速度
def choosedataincsv(filepath, savepath, datatype, intervals):
    df = pd.read_csv(filepath)
    df = df.astype(str)
    datasize = len(datatype)
    alldata = ''
    for i in range(datasize):
        alldata += datatype[i] + '|'
    alldata = alldata[: -1]
    print(alldata)
    y = df[df['type'].str.contains(alldata)]
    if intervals > 1:
        for i in y.index:
            interval = (interval + 1) % intervals
            if interval == 0:
                continue
            df.drop(i, inplace=True)
    else:
        for i in y.index:
            df.drop(i, inplace=True)
    df.rename(columns={'type': 'type',
                       'Unnamed: 2': 'UTCtime',
                       'Unnamed: 3': 'longtitude',
                       'Unnamed: 4': 'latitude',
                       'Unnamed: 5': 'top',
                       'Unnamed: 6': 'yaw',
                       'Unnamed: 7': 'pitch',
                       'Unnamed: 8': 'velocity angle',
                       'Unnamed: 9': 'velocity',
                       'Unnamed: 10': 'roll',
                       'Unnamed: 11': 'main antenna',
                       'Unnamed: 12': 'secd antenna',
                       'Unnamed: 13': 'main satellites',
                       'Unnamed: 14': 'secd satellites',
                       'Unnamed: 15': 'east position',
                       'Unnamed: 16': 'north position',
                       'Unnamed: 17': 'top position',
                       'Unnamed: 18': 'east velocity',
                       'Unnamed: 19': 'north velocity',
                       'Unnamed: 20': 'top velocity',
                       'Unnamed: 21': 'save',
                       'Unnamed: 22': 'check',
                       'Unnamed: 23': 'rostime',
                       'Unnamed: 24': 'nan',
                       'Unnamed: 25': 'nan',
                       'Unnamed: 26': 'nan',
                       'Unnamed: 27': 'nan',
                       'Unnamed: 28': 'nan'},inplace=True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    df.drop(['nan'], axis=1, inplace=True)
    df.drop(['roll'], axis=1, inplace=True)
    df = df.to_csv(savepath, index=0)


# choose KSXT
# 只取经纬度'GPGGA', 'GPTRA', 'HEADING', 'KSXT'
# 筛选前需要把第一列空出来
datatype = ['GPGGA', 'GPTRA', 'HEADING']
gpsall = sys.argv[1]
gpsksxt = sys.argv[2]
choosedataincsv(gpsall, gpsksxt, datatype, 0)