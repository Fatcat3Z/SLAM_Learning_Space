import csv
import os
import pandas as pd
import cv2

def generatetimefile(filepath, timefile2save):
    timefile2save = open(filepath, 'a')
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        # rows = [row for row in reader]
        for row in reader:
            (_, imagename) = os.path.split(row[2])
            (onlyname, _) = os.path.splitext(imagename)
            timefile2save.write(onlyname + ' ' + row[0] + '\n')
    timefile2save.close()


#  intervals 连续删除间隔
def choosedataincsv(filepath, datatype, intervals):
    df = pd.read_csv(filepath)
    df = df.astype(str)
    y = df[df['type'].str.contains(datatype)]
    interval = 0
    if intervals > 1:
        for i in y.index:
            interval = (interval + 1) % intervals
            if interval == 0:
                continue
            df.drop(i, inplace=True)
    else:
        for i in y.index:
            df.drop(i, inplace=True)
    df = df.to_csv(filepath, index=0)


filename = '/home/fatcat/Desktop/graduate_project/project_zrd/dso/river/vignette.png'
img = cv2.imread(filename)
dim = (800, 600)
imgresized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print(imgresized.shape)
cv2.imwrite('/home/fatcat/Desktop/graduate_project/project_zrd/dso/river/vignette_after.png', imgresized)