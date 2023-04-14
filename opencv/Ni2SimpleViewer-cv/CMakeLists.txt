cmake_minimum_required (VERSION 3.1)

set(TARGET_SAMPLE_NAME Ni2SimpleViewer-cv)

project(${TARGET_SAMPLE_NAME})

## Build Target Executable
add_executable(${TARGET_SAMPLE_NAME}
    Source/main.cpp
)

target_include_directories(${TARGET_SAMPLE_NAME} PRIVATE
    ${OPENNI2_INC}
    ${PROJECT_SOURCE_DIR}/../common
    ${OPENCV_INC}
)

target_link_libraries(${TARGET_SAMPLE_NAME}
    ${OPENNI2_LIB}
    ${OPENCV_LIB}
)

set_property(TARGET ${TARGET_SAMPLE_NAME} PROPERTY CXX_STANDARD 11)

## Installation
install(TARGETS ${TARGET_SAMPLE_NAME} DESTINATION .)