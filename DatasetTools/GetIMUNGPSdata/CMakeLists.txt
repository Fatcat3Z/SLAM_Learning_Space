cmake_minimum_required(VERSION 3.17)
project(data_process)

set(CMAKE_CXX_STANDARD 14)
find_package( OpenCV )
include_directories( ${OpenCV_INCLUDE_DIRS} )


include_directories( "/usr/include/eigen3" )

add_executable(data_process readdate.cpp readimu.cpp readimu.hpp)

