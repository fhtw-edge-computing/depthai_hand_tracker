# OpenHab Smart Living Lab Hand Gesture Control
A computer vision based hand gesture control for Smart Home appliances using OAK-D, DepthAI, Raspberry Pi, and Raspberry Pi 7" Touch Display. It also gives an audio feedback if you connect speakers to your Pi. 

For information on DepthAI and OAK-D please visit https://docs.luxonis.com/en/latest/#.

This project uses partially modified https://github.com/geaxgx/depthai_hand_tracker.git.

## Raspberry Pi setup
This project is tested on a Raspberry Pi 3B with \
Raspberry Pi OS with desktop (64 bit) \
Release date: April 4th 2022 \
Kernel version: 5.15 \
downloaded from https://www.raspberrypi.com/software/operating-systems/ \
Python3.9.2 (comes with Raspberry Pi OS) \

### 1. Install dependencies needed by depthai
See also https://docs.luxonis.com/projects/api/en/latest/install/ for more information
```console
sudo curl -fL https://docs.luxonis.com/install_dependencies.sh | bash
```

### 2. Install pico TTS 

Install and test pico2wave tts.

```console
sudo apt-get install libttspico-utils
pico2wave -w /tmp/hello.wav "Hello from Raspberry Pi"
aplay /tmp/hello.wav
```

### 3. Clone this repository
In a folderq of your choice open a terminal and enter: 
```console
git clone https://github.com/fhtw-edge-computing/depthai_hand_tracker.git
```

### 4. Create virtual environment
```console
cd depthai_hand_tracker/
```
Create a virtual environment with name myvenv: 
```console
python3 -m venv hgc-living-lab 
```
Activate the virtual environment: 
```console
source hgc-living-lab/bin/activate 
```
Update pip, setuptools, wheel: 
```console
pip install -U pip setuptools wheel 
```
Install requirements:
```console
cd examples/remote_control
python3 -m pip install -r requirements-openhab-livinglab.txt
```

### 5. Add UDEV rule for OAK-D device
To check if the OAK-D is connected, enter in a terminal:
```console
lsusb | grep MyriadX
```
The output should be similar to: Bus 003 Device 002: ID 03e7:2485 Intel Movidius MyriadX

Add the udev rule before you use the device for the first time on a new OS. This rule is nessessary to access the device correctly. To add and apply the rule, please enter in a terminal: 
```console
echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

### 6. Run hand gesture control
(cd controls/) \
Optional - To check if your virtual environment is activated enter in the terminal: 
```console
which python
```
this should show the \<path to your install folder\>/myvenv/bin/python 

#### In your activated environment run:
```console
python 05_openhab-living-lab.py
```

###  Optional - autostart hand gesture control on reboot: 
In a terminal enter: 
```console
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
  
  Add following line at the end of the autostart file: 
  
  /\<path to your install folder\>/myvenv/bin/python /\<path to your install folder\>/itemControl.py 
  
  For example if you installed the hand gesture control in /home/pi/HGC the line looks like this: \
  /home/pi/HGC/hand_gesture_control/myvenv/bin/python /home/pi/HGC/hand_gesture_control/itemControl.py 
  
  Press CTRL+S to save and CTRL+X to exit nano 

```console
sudo reboot
```
