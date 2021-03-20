#dispenser
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 

rele = 17 #Rele
Eco = 21  # Entrada de captura de eco	
Trig = 20 # Salida del ecco 
Off = 17  # Boton para finalizar el proceso

GPIO.setup(rele, GPIO.OUT) # output 1 RELE
GPIO.setup(Off,GPIO.IN)
GPIO.setup(Eco,GPIO.IN)
GPIO.setup(Trig, GPIO.OUT)

# Fase de inicializacion

GPIO.output(Trig,GPIO.LOW) # El pin de emision se queda desactivado

# Loop infinito hasta parar con el boton


# Initial state for LEDs: 
print("Testing RF out, Press CTRL+C to exit") 

while (GPIO.input(Off) == GPIO.LOW):

    GPIO.output(Trig,True) # Comenzamos a enviar pulsos
	time.sleep(0.0001)     # Una pausa antes de escuchar
	GPIO.output(Trig,False)# Silenciamos el ecco
	start = time.time()   # Comenzamos a contar el tiempo que tarda en volver el ecco
	while GPIO.input(Eco) == 0: # Sino recibe senal sigue contando tiempo
		start = time.time()
        GPIO.output(17, GPIO.HIGH) 
        print("ON")
        time.sleep(0.3) 
        GPIO.output(17, GPIO.LOW) 
        print("OFF") 
        time.sleep(0.3)
	while GPIO.input(Eco) ==1: # Cunado reciba senal guardamos el dato
		stop = time.time() 
    


GPIO.cleanup()