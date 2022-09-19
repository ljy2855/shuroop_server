"""
우선 디바이스가 Serial Port를 통하여서 통신하는데 준비할 시간 3초정도 필요
그 다음에 py_serial.wrie를 이용하여 디바이스에 command 전송
작동 시간을 기다려준 후 py_serial.close() 로 문닫기
"""

import serial
import time

def open():
    print("ok I'll open")
    py_serial = serial.Serial(port='COM7', baudrate=9600)
    time.sleep(3)
    print("serial open")
    commend = 'a'
    py_serial.write(commend.encode())
    time.sleep(5)
    print("serial close")
    py_serial.close()
    
def close():
    print("ok I'll close")
    py_serial = serial.Serial(port='COM7', baudrate=9600)
    time.sleep(3)
    print("serial open")
    commend = 'b'
    py_serial.write(commend.encode())
    time.sleep(5)
    print("serial close")
    py_serial.close()
