#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from openni import openni2
import platform
import numpy as np
import cv2

# Initialize OpenNI
if platform.system() == "Windows":
    openni2.initialize("C:/Program Files/OpenNI2/Redist")  # Specify path for Redist
else:
    openni2.initialize()  # can also accept the path of the OpenNI redistribution

# Connect and open device
dev = openni2.Device.open_any()

# Create depth stream
depth_stream = dev.create_depth_stream()
depth_stream.start()

try:
    while True:

        #while cv2.waitKey(1) == -1 and cv2.getWindowProperty("Depth View", cv2.WND_PROP_FULLSCREEN) != -1:
        frame = depth_stream.read_frame()
        frame_data = frame.get_buffer_as_uint16()
        # Convert images to numpy arrays
        if len(frame_data) == 4800:
            depth_array = np.asarray(frame_data).reshape((60, 80))
        elif len(frame_data) == 76800:
            depth_array = np.asarray(frame_data).reshape((240, 320))
        elif len(frame_data) == 307200:
            depth_array = np.asarray(frame_data).reshape((480, 640))
        else:
            depth_array = np.asarray(frame_data).reshape((480, 640))

        # Trimming depth_array
        max_distance = 4000
        min_distance = 0
        out_of_range = depth_array > max_distance
        too_close_range = depth_array < min_distance
        depth_array[out_of_range] = max_distance
        depth_array[too_close_range] = min_distance

        # Scaling depth array
        depth_scale_factor = 255.0 / (max_distance - min_distance)
        depth_scale_offset = -(min_distance * depth_scale_factor)
        depth_array_norm = depth_array * depth_scale_factor + depth_scale_offset

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(depth_array_norm.astype(np.uint8), cv2.COLORMAP_JET)

        # Replacing invalid pixel by black color
        depth_colormap[np.where(depth_array == 0)] = [0, 0, 0]

        # Reshape to what we want
        depth_colormap = cv2.resize(depth_colormap, (640, 480), interpolation=cv2.INTER_LINEAR)

        # Display image
        cv2.namedWindow("Depth View", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Depth View", depth_colormap)

        key = cv2.waitKey(1)
        # press key q or Esc can quit the window
        if key & 0xFF == ord('q') or key & 0xFF == 27:
            break

finally:

    # Stop streaming
    depth_stream.stop()
    openni2.unload()
    print("Bye bye!")