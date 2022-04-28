import bme280

# Definição de temperatura máxima
temp_max = 30
temp_min = 12
DEVICE1 = 0x76
DEVICE2 = 0x77

def temp_control():
    # Leitura da temperatura pelo sensor 
    temp1 = bme280.read_temp(DEVICE1) # Sensor porta
    temp2 = bme280.read_temp(DEVICE2) # Sensor coifa
    
    # Temperatura maior que temp_max -> Sistema de resfriamento desligado
    if(temp1 > temp_max):        
        # Ativando atuadores (peltier e coolers)
        GPIO.output(5,0)
        GPIO.output(6,0)
        GPIO.output(13,0)
        GPIO.output(19,0)
    elif(temp1 < temp_max or temp2 <= temp_min):
        # Desativando atuadores (peltier e coolers)
        GPIO.output(5,1)
        GPIO.output(6,1)
        GPIO.output(13,1)
        GPIO.output(19,1)
    
    return temp1


    
    



