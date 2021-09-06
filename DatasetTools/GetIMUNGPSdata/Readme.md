Get IMU and GPS data from Visual-Interial-Lake dataset
Compute the pose

#### readimu.cpp  
 Read imu datas from .csv files which may should be filtered before.  
 The format of the data read in this file is:
 > timestamp north velocity east velocity up velocity roll pitch azimuth (according to [The Visual-Inertial Canoe Dataset](https://experts.illinois.edu/en/datasets/the-visual-inertial-canoe-dataset-2))
 
 - tips: north velocity corresponds to the z-axis speed of the camera coordinate system, while east corresponds to x-axis and up corresponds to negative y-axis.

#### readdata.cpp
Get imu data and calculate the groundtruth trajectory which is saved as a .txt file.
Then we can use evo to evaluation the result.[evo](https://github.com/MichaelGrupp/evo)

#### choose_csv.py
Filter the data in .csv file and associate the image file with timestamp(provide the times.txt in DSO). 
