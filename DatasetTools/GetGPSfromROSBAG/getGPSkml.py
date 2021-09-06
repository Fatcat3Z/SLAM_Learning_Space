import sys
import pandas as pd


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


# Change GPS infos into kml files
gpsksxt = sys.argv[1]
kmlfile = sys.argv[2]
writekmlfile(gpsksxt, kmlfile)