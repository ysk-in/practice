cmake_minimum_required(VERSION 3.13)
project(TestProject)

set(CMAKE_CXX_STANDARD 17)

include_directories(src)

add_executable(
        TestProject
        src/complex.cpp src/complex.h
        src/pch.cpp src/pch.h
        src/TestApplication.cpp src/TestApplication.h
        src/user.cpp
        src/Vector.cpp src/Vector.h
        src/Shape.cpp src/Shape.h
        src/vector_template.cpp src/vector_template.h src/Less_than.cpp src/Less_than.h)
