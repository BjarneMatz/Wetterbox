# read serial data from arduino output and save to file via database skript on backend server

from serial import Serial
import time
import json
import datetime
import os

def read_serial():
    """read serial data from arduino"""
    ser = Serial('COM8', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            send_data(line)
            ser.write(b"1")
        


def send_data(data):
    """send data to backend server"""
    print(data)
    pass

def main():
    """main function"""
    read_serial()

if __name__ == "__main__":
    main()
