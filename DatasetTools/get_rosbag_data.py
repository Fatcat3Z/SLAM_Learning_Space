import rosbag
import csv
import pandas as pd
import numpy as np

# 获取GPS数据,将全部的NMEA语句存储为csv文件
def getGPSinfo(GPSsavefile, rosbagfile, 
  f = open(GPSsavefile, 'a')
  csv_writer = csv.writer(f)
  bag_file = rosbagfile
  bag = rosbag.Bag(bag_file, "r")
  bag_data = bag.read_messages('/nmea_sentence')
  k = []

  for topic, msg, t in bag_data:
      gpsdata = msg.sentence
      timestr = "%.6f" % msg.header.stamp.to_sec()
      result = gpsdata.strip("\n")
      linedata = gpsdata.split(',')
      linedata.append(timestr)
      csv_writer.writerow(linedata)
      print(linedata)

  f.close()

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
                       'Unnamed: 1': 'UTCtime',
                       'Unnamed: 2': 'longtitude',
                       'Unnamed: 3': 'latitude',
                       'Unnamed: 4': 'top',
                       'Unnamed: 5': 'yaw',
                       'Unnamed: 6': 'pitch',
                       'Unnamed: 7': 'velocity angle',
                       'Unnamed: 8': 'velocity',
                       'Unnamed: 9': 'roll',
                       'Unnamed: 10': 'main antenna',
                       'Unnamed: 11': 'secd antenna',
                       'Unnamed: 12': 'main satellites',
                       'Unnamed: 13': 'secd satellites',
                       'Unnamed: 14': 'east position',
                       'Unnamed: 15': 'north position',
                       'Unnamed: 16': 'top position',
                       'Unnamed: 17': 'east velocity',
                       'Unnamed: 18': 'north velocity',
                       'Unnamed: 19': 'top velocity',
                       'Unnamed: 20': 'save',
                       'Unnamed: 21': 'check',
                       'Unnamed: 22': 'rostime',
                       'Unnamed: 23': 'nan',
                       'Unnamed: 24': 'nan',
                       'Unnamed: 25': 'nan',
                       'Unnamed: 26': 'nan',
                       'Unnamed: 27': 'nan'},inplace=True)
    df.drop(['nan'], axis=1, inplace=True)
    df.drop(['roll'], axis=1, inplace=True)
    df = df.to_csv(savepath, index=0)               

# 生成可以在google earth显示的经纬度信息，将生成的kml文件中的kml数据复制到google earth生成的模板文件中即可
def writekmlfile(csvfile, kmlfile):
    df = pd.read_csv(csvfile)
    kml = open(kmlfile, 'w')
    choose_data = df[['longtitude', 'latitude', 'top']]
    data = np.array(choose_data)
    # print data
    for i in data:
        lon = i[0]
        lat = i[1]
        alt = i[2]
        gpsData = str(lon) + ',' + str(lat) + ',' + str(alt) + ' '
        kml.write(gpsData)
    kml.close()

# 提取GPS数据中的位姿信息，分别是时间戳、北向坐标、东向坐标、天向坐标、qx、qy、qz、qw               
def getGPSrtkposeinfo(csvfile, speedfile):
    df = pd.read_csv(csvfile)
    poseinfo = open(speedfile, 'w')
    choose_data = df[['rostime', 'east position', 'north position', 'top position']]
    data = np.array(choose_data)
    fournum = " 0 0 0 0"
    # print data
    for i in data:
        timestamp = i[0]
        eastposition = i[1]
        northposition = i[2]
        topposition = i[3]
        posedata = str(timestamp) + ' ' + str(eastposition) + ' ' + str(northposition) + ' ' + str(topposition) + fournum + '\n'
        poseinfo.write(posedata)
    poseinfo.close()
               
# Get GPS infos
# filpath = "/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/GPSdata.csv"
# savepath = "/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/GPSdata_choose_all.csv"
# # 只取经纬度'GPGGA', 'GPTRA', 'HEADING', 'KSXT'
# # 筛选前需要把第一列空出来
# datatype = ['GPGGA', 'GPTRA', 'HEADING']
# choosedataincsv(filpath, savepath, datatype, 0)

# Change GPS infos into kml files
# csvfile = '/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/GPSdata_rtk.csv'
# kmlfile = '/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/gpskml_all'
# writekmlfile(csvfile, kmlfile)               

# csvfile = '/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/GPSdata_choose_rtk.csv'
# speedtext = '/home/fatcat-lab/Desktop/graduate/SLAM_Workspace/dataset/loop_close/gpspose.txt'
# getGPSrtkposeinfo(csvfile, speedtext)               
