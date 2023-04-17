# Python Wrapper for LIPSedge SDK
In order to run these python samples you need to do following requirements:

Find out **LIPSedge SDK** for your LIPSedge 3D camera, check [here](https://www.lips-hci.com/lipssdk) to download latest SDK.

## Linux installation:
1. Once SDK is downloaded, untar it and enter the SDK folder, use below command to launch installation.
```
$ sudo ./install.sh
```

2. A development config file 'OpenNIDevEnvironment' is created for you to setup OpenNI2 software development environment.
   Two env. parameters `OPENNI2_INCLUDE` and `OPENNI2_REDIST` are exported to locate OpenNI2 include headers and library.
   Next time if you want to setup development env. quickly, source it in your shell before compilation.
```
$ source OpenNIDevEnvironment
```

3. Copy the required OpenNI2 and LIPSedge driver libraries to here. You will get `libOpenNI2.so` and directory `OpenNI2/Drivers` in current folder.
```
$ cp -r $OPENNI2_REDIST/* ./
```

## Windows installation:
1. Once SDK (.exe file) is downloaded, click it to launch installation.

2. Copy the following OpenNI2 and LIPSedge driver libraries from `C:/Program Files/OpenNI2/Redist/` to here.
   * OpenNI2.dll
   * OPENNI2/Drivers/DeviceModule2.dll (this is for LIPSedge camera DL/M3, replace it to your actual camera driver files)
   * OPENNI2/Drivers/RvcLib.dll

## Dependent python modules intallation:

In both Linux and Windows, you will need **Python 3** with the following python modules:

  * openni==2.3.0
     * ```$ pip install openni==2.3.0```
     * if you are interesting this package **OpenNI2 and NiTE2 python bindings**, visit its [Source](https://github.com/severin-lemaignan/openni-python) and the [Release 2.3.0](https://libraries.io/pypi/openni)

  * numpy
     * ```$ pip install numpy```

  * cv2
     * ```$ pip install --upgrade opencv-python```

## Running samples:
To run sample, use python3 to run it.
```
$ python3 ./cv_display_depth_frame.py
```

<p align="center"><img src="Screenshot-python3-cv-depth-frame-viewer.png" /></p>
