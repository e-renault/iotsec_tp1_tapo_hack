import serial
import time
import csv

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()
f = open("out/{}.csv".format(time.time()),"a")
writer = csv.writer(f,delimiter=",")

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        
        writer.writerow([time.time(),decoded_bytes])
    except KeyboardInterrupt:
        break
    except :
        print("Error")

print("Saving data...")
f.close()
