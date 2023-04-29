#import needed libraries
from serial import Serial
import time
import json
import requests


def read_serial():
    """read serial data from arduino"""
    ser = Serial('COM8', 9600, timeout=1) #initialize serial connection
    ser.flush() #flush serial buffer
    while True:
        if ser.in_waiting > 0: #if there is data in the serial buffer
            line = ser.readline().decode('utf-8').rstrip() #read the data
            send_data(line) #send the data to the server
            ser.write(b"1") #send some data to the arduino to tell it the connection is still alive
        

def send_data(data):
    """send data to server
    data: string"""
    print(data)
    data = json.dumps(data) #convert data to json
    data = data.encode('utf-8') #encode data to utf-8
    requests.request("POST", "http://127.0.0.1:5000/api/v1/data", data=data) #send data to server


def main():
    """main function"""
    read_serial()


if __name__ == "__main__":
    main()
