# Smart Gate

Real-Time License Plate Recognition using Raspberry Pi and Python

The project aims to develop an Automatic Door Opening System Through Vehicle Registration Number Plate using Raspberry Pi, Pi Camera, IR Sensor, and Linear Actuator. The system will automatically recognize the vehicle's registration number plate and open the door, providing convenience and security for the user. The linear actuator will be used to control the door's opening and closing mechanism, while the IR sensor will detect any obstacle in the door's path. The project will be implemented using the L298N motor driver and Python programming language, providing a cost-effective and efficient solution for automatic door opening.

# Start the program

- Connect the Raspberry Pi to the same network as the computer
- Connect the Raspberry Pi with real vnc viewer
- Open terminal and go to the project directory
  ```bash
  cd smartGate
  ```
- Activate the virtual environment

  ```bash
  source .venv/bin/activate
  ```

- Run testProject.py to test the program and check the camera

  ```bash
  python3 testProject.py
  ```

- Run finalProject.py to start the program

  ```bash
  python3 finalProject.py
  ```

# All Setups

## Hardware Requirements

- Raspberry Pi
- Pi camera
- IR Sensor
- Motor Driver(L298N)
- Linear Actuator
- Power Supply (12V Battery).

## Raspberry Pi OS Information

- PRETTY_NAME="Raspbian GNU/Linux 11 (bullseye)"
- NAME="Raspbian GNU/Linux"
- VERSION_ID="11"
- VERSION="11 (bullseye)"
- VERSION_CODENAME=bullseye
- ID=raspbian
- ID_LIKE=debian
- HOME_URL="http://www.raspbian.org/"
- SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
- BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

## Software Setup

- Add repository to /etc/apt/sources.list

```bash
deb http://archive.raspbian.org/raspbian wheezy main contrib non-free
deb-src http://archive.raspbian.org/raspbian wheezy main contrib non-free
```

- Add repository key

```bash
wget https://archive.raspbian.org/raspbian.public.key -O - | sudo apt-key add -
```

- Update and upgrade

```bash
sudo apt-get update
```

## Install dependencies

- Install libopencv

```bash
sudo apt install libopencv-dev
```

- Install pip

```bash
sudo apt install python3-pip
```

- Install python dependencies

```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

- Install opencv dependencies

```bash
sudo apt-get install libhdf5-dev  libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 -y
```

- Install opencv contrib

```bash
pip install opencv-contrib-python==4.5.3.56
```

- Install opencv

```bash
pip install opencv-python
```

- Install other dependencies

```bash
sudo dpkg --configure -a
sudo apt-get install tesseract-ocr
pip install pytesseract
pip install pyttsx3
pip install imutils
pip install picamera
```

- Install deksop environment

enable autologin with gui using raspi-config

```bash
   sudo apt install lightdm lxsession -y
```
