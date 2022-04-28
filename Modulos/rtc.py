from Modulos.imports import *

def timestamp():
    tempo = subprocess.run(["sudo", "hwclock", "-r"], capture_output=True)
    tempo = str(tempo.stdout)
    tempo = tempo.replace("b'", "")
    tempo = tempo.replace("\\n'", "")
    data, hora = tempo.split(" ", 2)
    hora, gmt = hora.split(".", 1)
    hora, minuto, segundo = hora.split(":", 2)
    
    return data, hora, minuto, segundo
