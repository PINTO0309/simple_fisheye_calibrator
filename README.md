# simple_fisheye_calibrator
Simple GUI-based correction of fisheye images. The correction parameters specified on the screen can be diverted to opencv's fisheye correction parameters.

![ezgif com-gif-maker (22)](https://user-images.githubusercontent.com/33194443/121390002-ea15d780-c987-11eb-92b2-e98fb1efa5b5.gif)

# 1. Usage
```bash
$ sudo pip3 install cvui Pillow opencv_python numpy --upgrade
$ git clone https://github.com/PINTO0309/simple_fisheye_calibrator.git && cd simple_fisheye_calibrator
$ python3 simple_capture.py

# 1. Capture one test image from the USB camera with "c" on the keyboard
# 2. Exit the capture application with "q" on the keyboard

$ python3 simple_fisheye_calibrator.py
```
