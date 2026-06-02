import  machine
import time

led1 = machine.Pin( 40, machine.Pin.OUT )
led2 = machine.Pin( 37, machine.Pin.OUT )
led3 = machine.Pin( 36, machine.Pin.OUT )

while (True):
    led1.on ()
    time.sleep (0.5)
    led1.off()

    led2.on ()
    time.sleep(0.5)
    led2.off()

    led3.on()
    time.sleep(0.5)
    led3.off()