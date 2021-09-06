import pandas as pd
import numpy as np
import sys


# 提取GPS数据中的位姿信息，分别是时间戳、北向坐标、东向坐标、天向坐标、qx、qy、qz、qw
def getGPSrtkposeinfo(csvfile, posefile):
    df = pd.read_csv(csvfile)
    poseinfo = open(posefile, 'w')
    choose_data = df[['rostime', 'east position', 'north position', 'top position']]
    data = np.array(choose_data)
    fournum = " 0 0 0 0"
    # print data
    for i in data:
        timestamp = i[0]
        eastposition = i[1]
        northposition = i[2]
        topposition = i[3]
        posedata = str(timestamp) + ' ' + str(eastposition) + ' ' + str(northposition) + ' ' + str(
            topposition) + fournum + '\n'
        poseinfo.write(posedata)
    poseinfo.close()


gpsksxt = sys.argv[1]
posetext = sys.argv[2]
getGPSrtkposeinfo(gpsksxt, posetext)