//
// Created by fatcat on 2/26/21.
//
#include "readimu.h"


using namespace std;

int main(){
    IMUdata imudata;
    const char* csvfile = "/home/fatcat/Desktop/graduate_project/project_zrd/dataset/visual_inertial/data/527-8_ins.csv";
    string savetrajtruth = "/home/fatcat/Desktop/graduate_project/project_zrd/dso/river/527-8_groundtruth.txt";
    ofstream fout(savetrajtruth);
    csvreader reader(csvfile);
    reader.readline();
    double timestamp = 0;
    int count = 1;
    Eigen::Matrix3d Rwc;    // 旋转矩阵
    Eigen::Vector3d twc;    // 平移矩阵
    Eigen::Vector3d eulerangles;    // 欧拉角，顺序：滚转角，俯仰角，偏航角
    double timestep = 0.1;
    double speed_last[3] = {0};
    double initialeular[3] = {0};
    double position[3] ={0};
    while (!reader.readline()){
        imudata = setIMU(reader.data);
//        cout<<"timestap:" << imudata.speed[0] <<endl;
        if(count  == 1){
            twc = Eigen::Vector3d::Zero();
            Rwc = Eigen::Matrix3d::Identity();
            Eigen::Quaterniond q(Rwc);
            timestamp = imudata.number;
            initialeular[0] = imudata.gyro[0];
            initialeular[1] = imudata.gyro[1];
            initialeular[2] = imudata.gyro[2];
            speed_last[0] = imudata.speed[1];           // 东向 对应x
            speed_last[1] = imudata.speed[0];           // 北向 对应z
            speed_last[2] = imudata.speed[2];           // 正向朝上 对应-y
            fout << fixed <<timestamp << " " <<twc(0) << " " << twc(1) << " " << twc(2) << " " << q.x()<< " " << q.y() << " " << q.z() << " " << q.w() <<endl;
        }else{
            timestamp = imudata.number;
            eulerangles(0) = imudata.gyro[0] - initialeular[0];
            eulerangles(1) = imudata.gyro[1] - initialeular[1];
            eulerangles(2) = 360 - (imudata.gyro[2] - initialeular[2]);
            Rwc = reader.eular2rotation(eulerangles);
            Eigen::Quaterniond q(Rwc);
            twc[0] = 0.5 * (imudata.speed[1] + speed_last[0]) * timestep;   // x
//            cout<<"t X:"<<twc[0]<<endl;
            twc[1] = 0.5 * (imudata.speed[0] + speed_last[1]) * timestep;   // z
            twc[2] = 0.5 * (imudata.speed[2] + speed_last[2]) * timestep;   // -y

            speed_last[0] = imudata.speed[1];
            speed_last[1] = imudata.speed[0];
            speed_last[2] = imudata.speed[2];

            position[0] += twc[0];
//            cout<<"position x:"<<position[0]<<endl;
            position[1] += twc[1];
            position[2] += twc[2];
            fout << fixed << timestamp << " " <<position[0] << " " << -position[2] << " " << -position[1] << " " << q.x()<< " " << q.y() << " " << q.z() << " " << q.w() <<endl;
        }
        count ++;
    }
    return 0;
}
