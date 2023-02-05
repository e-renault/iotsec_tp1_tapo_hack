# 8INF917 - Sécurité informatique pour l'Internet des Objets (Hiver 2023)  

## Log datas consumption on computer (plug arduino on your computer before)  

run python script :  
```
python3 datalogger.py  
```
If it doesn't work, consider to modify line5 to you serial port. (/dev/ttyACM0 is under linux, should be /usbX under windows)  
The output should appear in the "/out" folder.  


## Upload firmware on Arduino  

Upload src/main.cpp programm to the board. If you're using the official arduino software, you should remove the first include file (used by platformio)  
