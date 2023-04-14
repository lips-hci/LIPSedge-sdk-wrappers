#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openni import openni2
import platform
import numpy as np
import cv2
import threading

# Initialize OpenNI
if platform.system() == "Windows":
    openni2.initialize("C:/Program Files/OpenNI2/Redist")  # Specify path for Redist
else:
    openni2.initialize()  # can also accept the path of the OpenNI redistribution

oniVersion = openni2.get_version()
print(f'OpenNI is initialized -- version:{oniVersion.major}.{oniVersion.minor}.{oniVersion.maintenance}.{oniVersion.build}')

# Device Listener for OpenNI
class MyDeviceListener(openni2.DeviceListener):
    def __init__(self, win):
        super().__init__()
        self.win = win
        self.dev = None
        self.depth_stream = None
        self.mutex = threading.Lock()

    def on_connected(self, devinfo):
        print("+++++++++++")
        print(f'  Device {devinfo.uri} Connected')
        print("  Let's open openni2 device and stream")
        self.start_dev_and_stream()
        print("+++++++++++")

    def on_disconnected(self, devinfo):
        print("-----------")
        print(f'  Device {devinfo.uri} Disconnected')
        print("  Let's close openni2 device and stream")
        self.close_dev_and_stream()
        print("-----------")

    def on_state_changed(self, devinfo, state):
        print(f'Device {devinfo.uri} error state changed to {state}')

    def start_dev_and_stream(self):
        with self.mutex:
            # Connect and open device
            self.dev = openni2.Device.open_any()

            # Create depth stream
            self.depth_stream = self.dev.create_depth_stream()

            # Register frame listener
            self.depth_stream.register_new_frame_listener(self.win.on_new_frame)
            self.depth_stream.start()

    def close_dev_and_stream(self):
        with self.mutex:
            self.depth_stream.stop()
            self.depth_stream.unregister_new_frame_listener(self.win.on_new_frame)
            self.depth_stream.close()

            self.depth_stream=None
            self.dev.close()
            self.dev=None

class MyWindow(object):
    def __init__(self):
        self.image = np.zeros((600, 800, 3), dtype = "uint8")
        self.image_lock = threading.Lock()

    def show(self):
        cv2.namedWindow("Depth View", cv2.WINDOW_NORMAL)
        with self.image_lock:
            # Display image
            cv2.imshow("Depth View", self.image)

    def on_new_frame(self, stream):
        frame = stream.read_frame()
        while(True):
            with self.image_lock:
                self.image = self.depth_processing(frame)
                break

    def depth_processing(self, frame):
        frame_data = frame.get_buffer_as_uint16()
        depth_array = np.asarray(frame_data).reshape((60, 80))

        # Trimming depth_array
        max_distance = 7000
        min_distance = 0
        out_of_range = depth_array > max_distance
        too_close_range = depth_array < min_distance
        depth_array[out_of_range] = max_distance
        depth_array[too_close_range] = min_distance

        # Scaling depth array
        depth_scale_factor = 255.0 / (max_distance - min_distance)
        depth_scale_offset = -(min_distance * depth_scale_factor)
        depth_array_norm = depth_array * depth_scale_factor + depth_scale_offset

        rgb_frame = cv2.applyColorMap(depth_array_norm.astype(np.uint8), cv2.COLORMAP_JET)

        # Replacing invalid pixel by black color
        rgb_frame[np.where(depth_array == 0)] = [0, 0, 0]
        rgb_frame = cv2.resize(rgb_frame, (800, 600), interpolation=cv2.INTER_AREA)

        return rgb_frame

###############
# Main program
###############
win = MyWindow()

listener = MyDeviceListener(win)
listener.start_dev_and_stream()

try:
    while(True):
        win.show()
        key = cv2.waitKey(1)
        # press key q or Esc can quit the window
        if key & 0xFF == ord('q') or key & 0xFF == 27:
            break

finally:
    listener.close_dev_and_stream()
    openni2.unload()
    print("Bye bye!")