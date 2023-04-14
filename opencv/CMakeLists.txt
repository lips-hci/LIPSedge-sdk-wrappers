cmake_minimum_required (VERSION 3.1)
project(LIPSedgeOpenCVWrapper LANGUAGES CXX C)

## Setup Building Environment
include(${CMAKE_SOURCE_DIR}/CMake/SetupBuildEnvironment.cmake)
include(${CMAKE_SOURCE_DIR}/CMake/SetupOpenCV.cmake)

# Add our samples
add_subdirectory(Ni2SimpleViewer-cv)
