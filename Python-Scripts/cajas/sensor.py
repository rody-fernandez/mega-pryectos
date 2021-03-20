#importamos las librerias necesarias
import RPi.GPIO as GPIO  # Libreria relacionada con el GPIO
import time              # Libreria relacionada con el timpo

# Configuracion de las variables

GPIO.setmode(GPIO.BCM)  # Configuracion de como se van a leer los pines en la placa

	# Renombrar las variables

Eco = 21  # Entrada de captura de eco	
Trig = 20 # Salida del ecco 
Off = 17  # Boton para finalizar el proceso

	# Configuracion de los puertos

GPIO.setup(Off,GPIO.IN)
GPIO.setup(Eco,GPIO.IN)
GPIO.setup(Trig, GPIO.OUT)

# Fase de inicializacion

GPIO.output(Trig,GPIO.LOW) # El pin de emision se queda desactivado

# Loop infinito hasta parar con el boton

while (GPIO.input(Off) == GPIO.LOW):

	GPIO.output(Trig,True) # Comenzamos a enviar pulsos
	time.sleep(0.0001)     # Una pausa antes de escuchar
	GPIO.output(Trig,False)# Silenciamos el ecco
	start = time.time()   # Comenzamos a contar el tiempo que tarda en volver el ecco
	while GPIO.input(Eco) == 0: # Sino recibe senal sigue contando tiempo
		start = time.time()
	while GPIO.input(Eco) ==1: # Cunado reciba senal guardamos el dato
		stop = time.time() 
		
	diferencia = stop - start  # Se calcula la diferencia de tiempo 
	distancia = (diferencia * 34300)/2 # velocidad por tiempo entre 2
	  #Distancia en centímetros	
	print distancia  # Mostramos la distancia
	
	time.sleep (1)  # Tiempo de muestreo 1 segundo

# Finalizar programa

GPIO.cleanup() # Limpiar canales