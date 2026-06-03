# Async
A custom esp-32 based console to play multiple fun games.

## Setup
To start playing amazing console games you will need to first install micropython on your esp-32.
You will need esptool (pip install esptool).
First erase the flash of your esp-32 by using the command:
```
esptool.py --chip esp32 --port COM3 erase_flash
```

Than flash micropython by using the command:
```
esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 micropython\ESP32_GENERIC-v1.28.0.bin
```