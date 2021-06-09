# simple_fisheye_calibrator
Simple GUI-based correction of fisheye images. The correction parameters specified on the screen can be diverted to opencv's fisheye correction parameters.

![ezgif com-gif-maker (22)](https://user-images.githubusercontent.com/33194443/121390002-ea15d780-c987-11eb-92b2-e98fb1efa5b5.gif)

- Fisheye image before calibration

![fisheye_test](https://user-images.githubusercontent.com/33194443/121391145-023a2680-c989-11eb-9800-220039d0541e.jpg)

![Screenshot 2021-06-10 01:12:23](https://user-images.githubusercontent.com/33194443/121391077-f2badd80-c988-11eb-9228-b5238df38968.png)

- (Sample) Fisheye image after calibration

![fisheye_test_-0 78_-0 01_0 0_0 0_0 53](https://user-images.githubusercontent.com/33194443/121390883-c3a46c00-c988-11eb-8856-0c6af68f366a.jpg)

# 1. Usage
```bash
$ sudo pip3 install cvui Pillow opencv_python numpy --upgrade
$ git clone https://github.com/PINTO0309/simple_fisheye_calibrator.git && cd simple_fisheye_calibrator
$ python3 simple_capture.py

# 1. Capture one test image from the USB camera with "c" on the keyboard
# 2. Exit the capture application with "q" on the keyboard

$ python3 simple_fisheye_calibrator.py
```
