from Modulos.imports import *

adc = Adafruit_ADS1x15.ADS1015()
som_media = 1371

def read_noise():
    
    som = adc.read_adc(0, gain=(2/3))
    som = som - som_media + random.randint(-10,10)
    som = abs(som)
    dB = 20 * math.log10(som)
        
    return dB