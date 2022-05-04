import machine 
import ssd1306 
import framebuf

WIDTH = 128
HIGHT = 64

#i2c= I2C(scl = Pin(17), sda = Pin(16), machine.I2C(0))

oled = ssd1306.SSD1306_I2C(WIDTH, HIGHT,machine.I2C(0))

oled.fill(0)

oled.text("hello world",0 ,0)
oled.text("this is me",50 ,50)
oled.show()