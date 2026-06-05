# Async
A custom esp-32 based reconfigurable console to play multiple fun games.
https://github.com/Simone2048/Async/blob/78a8a7d3b7f829bab3eee6961448f61c30fdf5e1/Images/IMG_9364.jpg

## Hardware
This is the hardware used for the basic controller console configuration:
- Esp-32 Wroom (Az-Delivery)
- 0.96" Oled display
- 5X Buttons

## Setup
To start playing amazing console games you will need to first install micropython on your esp-32.
You will need esptool (pip install esptool).
First erase the flash of your esp-32 by using the command:
```
python -m esptool --chip esp32 --port YOUR_COM_PORT erase-flash
```

Than flash micropython by using the command:
```
python -m esptool --chip esp32 --port YOUR_COM_PORT --baud 460800 write-flash -z 0x1000 micropython\ESP32_GENERIC-v1.28.0.bin
```

Then run the copy-scripts.bat file and you're all set.
Reset your board and you are ready to play.
