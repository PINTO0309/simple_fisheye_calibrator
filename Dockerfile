FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ARG wkdir=/home/user

# dash -> bash
RUN echo "dash dash/sh boolean false" | debconf-set-selections \
    && dpkg-reconfigure -p low dash
WORKDIR ${wkdir}
COPY fisheye_test.jpg ${wkdir}/fisheye_test.jpg

# Install dependencies (1)
RUN apt-get update && apt-get install -y \
        python3-pip sudo libva-drm2 libva-x11-2 vainfo \
        libva-wayland2 libva-glx2 libva-dev libdrm-dev \
        xorg xorg-dev openbox libx11-dev libgl1-mesa-glx \
        libgl1-mesa-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies (2)
RUN pip3 install --upgrade pip \
    && pip install numpy==1.19.5 \
    && pip install cvui \
    && pip install Pillow \
    && pip install opencv_python \
    && pip install simple_fisheye_calibrator \
    && ldconfig \
    && pip cache purge \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Create a user who can sudo in the Docker container
ENV username=user
RUN echo "root:root" | chpasswd \
    && adduser --disabled-password --gecos "" "${username}" \
    && echo "${username}:${username}" | chpasswd \
    && echo "%${username}    ALL=(ALL)   NOPASSWD:    ALL" >> /etc/sudoers.d/${username} \
    && chmod 0440 /etc/sudoers.d/${username}
USER ${username}
RUN sudo chown ${username}:${username} ${wkdir}