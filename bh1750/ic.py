#this script is use to check that your sensore is connected or not

from machine import I2C
i2c = I2C(0)
devices = i2c.scan()

for device in devices:
    print(hex(device))
print("helo")
