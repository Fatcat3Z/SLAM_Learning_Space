//
// Created by fatcat on 2/26/21.
//
#ifndef USELK_READIMU_H
#define USELK_READIMU_H
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <Eigen/Core>
#include <Eigen/Dense>
#include <Eigen/Geometry>

struct IMUdata {
    double speed[3];
    double gyro[3];
    double number;
};

IMUdata setIMU( double data[] );

class csvreader {
public:
    csvreader(const char*);
    int readline();
    double data[7];
    Eigen::Matrix3d eular2rotation (Eigen::Vector3d eulerangles);
private:
    std::ifstream _csvinput;
};

#endif //USELK_READIMU_H
