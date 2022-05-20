from machine import Pin, UART
import time

uart = UART(0, 9600)

laser = Pin(13, Pin.OUT)

while True:
    if uart.any():
        command = uart.read()
        print(command)
        
        if 'fire' in command:
            laser.high()
            uart.write('firing')
        elif 'stop' in command:
            laser.low()
            uart.write('stop firing')
        else:
            laser.low()