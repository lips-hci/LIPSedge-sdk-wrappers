# LIPSedge Python Wrapper

### Requirements

In order to run these python samples you need to do following requirements:

* On linux, you need:
    1. To install the **LIPSedge SDK**, check [here](https://www.lips-hci.com/lipssdk) to download latest SDK.

    2. Enter the SDK folder and type below command to launch installation.
       ``$ sudo ./install.sh``

    3. A development config text 'OpenNIDevEnvironment' is created for you, next time if you want to setup
       an OpenNI2 software development environment, just sourcing it in your shell.
       ``$ source OpenNIDevEnvironment``

    4. Copy the required OpenNI2 and LIPSedge driver libraries to here.
       ``$ cp -r $OPENNI2_REDIST ./``

    * After files copied, you should see libOpenNI2.so and directory 'OpenNI2/Drivers' in this folder.

* On Windows, you need:
    1. To install the **LIPSedge SDK** and click .exe file to complete installation.

    2. Copy the following OpenNI2 and LIPSedge driver libraries from "C:/Program Files/OpenNI2/Redist/" to here.
        * OpenNI2.dll
        * OPENNI2/Drivers/DeviceModule2.dll
        * OPENNI2/Drivers/RvcLib.dll

### Running samples

In both Linux and Windows, you will need **Python 3** with the following python modules:
    * openni==2.3.0
    * numpy
    * cv2

    * use pip command to install opencv for python.
      ``$ pip install --upgrade opencv-python``

Those modules can be installed using pip command with elevated privileges:
      ``$ pip install <module name>``

