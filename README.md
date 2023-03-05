# smartGate

Real-Time License Plate Recognition using Raspberry Pi and Python

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
