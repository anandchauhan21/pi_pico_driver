from bmp180 import BMP180
from time import sleep
from machine import I2C, Pin                        # create an I2C bus object accordingly to the port you are using
# bus = I2C(1, baudrate=100000)           # on pyboard
bus = I2C(0)
#bus =  I2C(scl=Pin(17), sda=Pin(16), freq=100000)
#bus =  I2C(scl=Pin(4), sda=Pin(5), freq=100000)# on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

while True:
    tempc = bmp180.temperature
    Pressure = bmp180.pressure
    tempf = tempc*9/5+32
    p = bmp180.pressure
    altitude = bmp180.altitude
    # print(temp,(temp*9/5+32:.F2), p, altitude)
    # print("Temp: {0:.2f}C TempF: {1:.2f} Pressure: {2:.2f}  Altitude {3}".format(tempc,tempf,p*0.0002953,altitude))
    print('Temp: {0:.2f}'.format(tempc))
    print('pressure: {0:.2f}'.format(Pressure))
    sleep(5)