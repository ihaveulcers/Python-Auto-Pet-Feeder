This is what i did. Please let me know if there's a more elegant way to do this.
<br>
<br>
<br>
**My Pre-conditions**
- it has to be headless setup
- Unstable internet, so it has to run on its own 

**Hardware**
- Raspberry Pi Model B (rev1)
- Raspberry Pi AC power supply
- Ethernet Cable
- Servo motor
- Three Male-to-female jumper cables

**RPi Servo Motor setup**
- Connect Servo Motor to GPIO 
  - Reference GPIO Pinout: https://cdn.pimylifeup.com/wp-content/uploads/2015/09/Raspberry-Pi-GPIO-pinout-diagram-new.png
- My setup
  - red wire: power #2
  - black wire : ground #6
  - white wire : signal #18

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
  
**Python script**
- `sudo nano feeder.py`
  - create new python file in nano editor
- Paste the python script
- To save and exit the nano editor, press CRTL+X then Y then Enter

**Launch Python script on boot**
- `sudo crontab -e`
  - Reference : https://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/
- At the very bottom of the nano editor add `@reboot sleep 60s && python3 /home/pi/feeder.py`
  - Add delay reference : https://www.raspberrypi.org/forums/viewtopic.php?t=193438 
- To save and exit the nano editor, press CRTL+X then Y then Enter

**DONE**









