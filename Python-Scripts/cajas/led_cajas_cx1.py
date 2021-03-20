#CX 1 
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 
i=1 

GPIO.setup(17, GPIO.OUT) # output 1 
# Initial state for LEDs: 
print("Testing RF out, Press CTRL+C to exit") 

while i <= 15: 
    i += 2 
    GPIO.output(17, GPIO.HIGH) 
    print("ON")
    time.sleep(0.3) 
    GPIO.output(17, GPIO.LOW) 
    print("OFF") 
    time.sleep(0.3)

GPIO.cleanup()