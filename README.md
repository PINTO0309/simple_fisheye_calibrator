# simple_fisheye_calibrator
Simple GUI-based correction of fisheye images. The correction parameters specified on the screen can be diverted to opencv's fisheye correction parameters. Supports execution via Docker.

[![PyPI - Downloads](https://img.shields.io/pypi/dm/simple_fisheye_calibrator?color=2BAF2B&label=Downloads%EF%BC%8FInstalled)](https://pypistats.org/packages/simple_fisheye_calibrator) ![GitHub](https://img.shields.io/github/license/PINTO0309/simple_fisheye_calibrator?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/simple_fisheye_calibrator?color=2BAF2B)](https://pypi.org/project/simple_fisheye_calibrator/)

![001](https://user-images.githubusercontent.com/33194443/121445762-1142c800-c9cd-11eb-8f39-1a70d0020c8f.gif)

![005](https://user-images.githubusercontent.com/33194443/121450601-0ab94e00-c9d7-11eb-9173-f0dbb29adab6.gif)

- Fisheye image before calibration

![002](https://user-images.githubusercontent.com/33194443/121445230-02a7e100-c9cc-11eb-827b-078da31298b8.jpg)

![003](https://user-images.githubusercontent.com/33194443/121445245-0b001c00-c9cc-11eb-92db-6d13c0388814.png)

- (Sample) Fisheye image after calibration

![004](https://user-images.githubusercontent.com/33194443/121445265-15221a80-c9cc-11eb-85ea-7dc25f3a6cc4.jpg)

## 1. Install
### 1-1. Launching with Docker (with USB Camera / HostPC GUI, Docker Image size: 1.4GB)
- simple_capture
```bash
xhost +local: && \
docker run -it --rm \
-v `pwd`:/home/user/workdir \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
--device /dev/video0:/dev/video0:mwr \
--net=host \
-e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
-e DISPLAY=$DISPLAY \
--privileged \
pinto0309/simple_fisheye_calibrator:0.0.11 \
/bin/bash -c 'sudo simple_capture'

# 1. Capture one test image from the USB camera with "c" on the keyboard
# 2. Exit the capture application with "q" on the keyboard
```
- simple_fisheye_calibrator
```bash
# Still image
xhost +local: && \
docker run -it --rm \
-v `pwd`:/home/user/workdir \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
--device /dev/video0:/dev/video0:mwr \
--net=host \
-e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
-e DISPLAY=$DISPLAY \
--privileged \
pinto0309/simple_fisheye_calibrator:0.0.11 \
simple_fisheye_calibrator --file_path fisheye_test.jpg
```
or
```bash
# USB Camera: video0
xhost +local: && \
docker run -it --rm \
-v `pwd`:/home/user/workdir \
-v /tmp/.X11-unix/:/tmp/.X11-unix:rw \
--device /dev/video0:/dev/video0:mwr \
--net=host \
-e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
-e DISPLAY=$DISPLAY \
--privileged \
pinto0309/simple_fisheye_calibrator:0.0.11 \
/bin/bash -c 'sudo simple_fisheye_calibrator --file_path 0'
```
### 1-2. Installation on the host PC
```bash
$ pip3 install -U simple_fisheye_calibrator
```

## 2. Usage
```bash
$ simple_capture
# 1. Capture one test image from the USB camera with "c" on the keyboard
# 2. Exit the capture application with "q" on the keyboard

# Still image
$ simple_fisheye_calibrator --file_path xxx.jpg
# USB Camera: video0
$ simple_fisheye_calibrator --file_path 0
```

or

```bash
$ sudo pip3 install cvui Pillow opencv_python numpy --upgrade
$ git clone https://github.com/PINTO0309/simple_fisheye_calibrator.git && \
cd simple_fisheye_calibrator

$ python3 simple_fisheye_calibrator/simple_capture.py

# 1. Capture one test image from the USB camera with "c" on the keyboard
# 2. Exit the capture application with "q" on the keyboard

# USB Camera: video0
$ python3 simple_fisheye_calibrator/simple_fisheye_calibrator.py --file_path 0
```

## 3. Parameter
```
usage:
simple_fisheye_calibrator.py \
  [-h] \
  [--file_path FILE_PATH] \
  [--window_size_width WINDOW_SIZE_WIDTH] \
  [--window_size_height WINDOW_SIZE_HEIGHT]

optional arguments:
  -h, --help
      show this help message and exit
  --file_path FILE_PATH
      File path of the still image (e.g. xxx.jpg) or device number of the camera (e.g. 0)
  --window_size_width WINDOW_SIZE_WIDTH
      Default window size width
  --window_size_height WINDOW_SIZE_HEIGHT
      Default window size height
```
