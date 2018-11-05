This is what i did. Please let me know if there's a more elegant way to do this.
<br>
<br>
<br>
**Hardware**
- Raspberry Pi Model
- Raspberry Pi AC power supply
- Ethernet Cable
- Servo motor
- Three Male-to-female jumper cables

**RPi software setup**
- Download the latest Raspbian (Lite)     https://www.raspberrypi.org/downloads/raspbian/
- `sudo dd bs=1m if=raspbian.img of=/dev/rdiskx` 
  - To write image file to SD card,  x = SD card disk number
  - Reference: https://www.instructables.com/id/Set-Up-a-Raspberry-Pi-Using-a-Mac/
- Enable SSH manually https://www.raspberrypi.org/forums/viewtopic.php?t=191252
- Find RPi IP address https://www.raspberrypi.org/documentation/remote-access/ip-address.md
- `ssh pi@192.168.1.100` 
  - default password : raspberry
- `sudo apt-get update` 
- `sudo apt-get upgrade` 
- `sudo apt-get install rpi.gpio` 
- `sudo pip3 install apscheduler==2.1.2` 

**RPi hardware setup**
- Connect Servo Motor to GPIO 
  - Reference GPIO Pinout: https://pimylifeup.com/raspberry-pi-gpio/
