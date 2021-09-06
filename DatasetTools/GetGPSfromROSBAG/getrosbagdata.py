import rosbag
import csv
import sys


# 获取GPS数据,将全部的NMEA语句存储为csv文件
def getGPSinfo(rosbagfile, GPSsavefile):
    f = open(GPSsavefile, 'a')
    csv_writer = csv.writer(f)
    bag_file = rosbagfile
    bag = rosbag.Bag(bag_file, "r")
    bag_data = bag.read_messages('/nmea_sentence')
    k = []
    csv_writer.writerow(["type"])
    for topic, msg, t in bag_data:
        gpsdata = msg.sentence
        timestr = "%.6f" % msg.header.stamp.to_sec()
        result = gpsdata.strip("\n")
        linedata = gpsdata.split(',')
        linedata.append(timestr)
        csv_writer.writerow(linedata)
        print(linedata)

    f.close()


# Get GPS infos
filpath = sys.argv[1]
gpsall = sys.argv[2]
getGPSinfo(filpath, gpsall)






