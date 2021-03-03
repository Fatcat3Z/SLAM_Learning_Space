//
// Created by fatcat on 2/26/21.
//
#include "readimu.h"

using namespace std;

csvreader::csvreader(const char *path)
{
    _csvinput.open(path);
}

IMUdata setIMU(double data[])
{
    IMUdata imudata;
    imudata.number = data[0];
    for (int i = 0; i < 3; i++)
    {
        imudata.speed[i] = data[i + 1];
        imudata.gyro[i] = data[i + 4];
    }
    return imudata;
}


//读取csv文件数据
int  csvreader::readline()
{
    //定义一行数据为字符串
    string _Oneline;
    //读取一行数据
    getline(_csvinput, _Oneline);
    //cout << "数据：" << _Oneline << endl;
    //如果读取到首行数据(设置标志位)，返回失败
    if (_Oneline[0] == 'P'){
        return EXIT_FAILURE;
    }

    //定义字符串流对象
    istringstream _Readstr(_Oneline);
    //定义一行数据中的各个字串
    string _partOfstr;
    //将一行数据按'，'分割
    for(int i = 0; i < 7; i++)
    {
        getline(_Readstr, _partOfstr, ',');
            data[i] = atof(_partOfstr.c_str());
//            cout<<fixed<<data[0]<<endl;

    }
    //判断是否读完数据
    if ((data[0]||data[1]||data[3]) == 0){
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

Eigen::Matrix3d csvreader::eular2rotation( Eigen::Vector3d  eulerAngles)
{
    double roll = eulerAngles(0);
    double pitch = eulerAngles(1);
    double yaw = eulerAngles(2);

    double cr = cos(roll); double sr = sin(roll);
    double cp = cos(pitch); double sp = sin(pitch);
    double cy = cos(yaw); double sy = sin(yaw);

    Eigen::Matrix3d RIb;
    RIb<< cy*cp ,   cy*sp*sr - sy*cr,   sy*sr + cy* cr*sp,
            sy*cp,    cy *cr + sy*sr*sp,  sp*sy*cr - cy*sr,
            -sp,         cp*sr,           cp*cr;
    return RIb;
}
