from tkinter import * 
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT) # TRIG
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.IN)  # ECHO
GPIO.output(16,False)    # Borramos TRIG

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT) # TRIG
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(38,GPIO.IN)  # ECHO
GPIO.output(37,False)    # Borramos TRIG
reloj_s3_paro=0
reloj_s3_inicio=0
tiempo_s3=0
velocidad_s3=0


try:
    while True: # Bucle infinito
        GPIO.output (16,True)
        time.sleep(0.00001)
        GPIO.output(16,False)
        inicio_s1=time.time()
        
        while GPIO.input(18)==0:
            inicio_s1=time.time()
        while GPIO.input(18)==1:
            paro_s1=time.time()

        Tiempo_s1=paro_s1-inicio_s1
        Distancia_s1=(Tiempo_s1*34300)/2
        #print Distancia_s1 
        time.sleep(0.1)
        if Distancia_s1 > 10:
            GPIO.output(12,True)
            GPIO.output(15,False)
            #print ("continue1")
        else:
            GPIO.output(15,True)
            GPIO.output(12,False)
            #print ("PARE1")
        
        GPIO.output (37,True)
        time.sleep(0.00001)
        GPIO.output(37,False)
        inicio_s2=time.time()
        
        while GPIO.input(38)==0:
            inicio_s2=time.time()
        while GPIO.input(38)==1:
            paro_s2=time.time()

        Tiempo_s2=paro_s2-inicio_s2
        Distancia_s2=(Tiempo_s2*34300)/2
        #print Distancia_s2 
        time.sleep(0.1)
        if Distancia_s2 > 10:
            GPIO.output(12,True)
            GPIO.output(15,False)
            #print ("continue2")
        else:
            GPIO.output(15,True)
            GPIO.output(12,False)
            #print ("PARE2")

        if Distancia_s1<15:
            contador=100
            reloj_s3_inicio=time.time()
            print ("Reloj iniciado")
        
        if Distancia_s2<15:
            contador=200
            reloj_s3_paro=time.time()
            print ("Reloj parado")
            tiempo_s3=reloj_s3_paro-reloj_s3_inicio
            print (tiempo_s3)
            velocidad_s3= (400)/tiempo_s3
            red = round (velocidad_s3)
            print (red,"m/s")

            if red>65:
                ventana = Tk()
                ventana.title("TU VELOCIDAD ES DE ")
                widget = Label(ventana, text=(red,"m/s","HAS PASADO LA VELOCIDAD LÍMITE"))
                #widget = Label(ventana, text=(red,"m/s"))
                widget.pack(expand=YES, fill=BOTH)
                ventana.geometry("400x100")
                ventana.resizable(width=FALSE, height=FALSE)
                ventana.mainloop()
                break
            else:
                ventana = Tk()
                ventana.title("TU VELOCIDAD ES DE ")
                widget = Label(ventana, text=(red,"m/s","TU VELOCIDAD ES CORRECTA"))
                #widget = Label(ventana, text=(red,"m/s"))
                widget.pack(expand=YES, fill=BOTH)
                ventana.geometry("400x100")
                ventana.resizable(width=FALSE, height=FALSE)
                ventana.mainloop()
                break 
         
            
except KeyboardInterrupt:
    print("saliendodelprograma")
    GPIO.cleanup()