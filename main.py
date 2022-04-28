from Modulos.imports import *
import Modulos.imports
import Modulos.sensor_ruido
import Modulos.fita_led_ldr
import Modulos.camera
import Modulos.temp_control
import Modulos.read_qr_code
import Modulos.rtc
import Modulos.codificacao_json
import Modulos.send_json

client = connect_mqtt()
subscribe(client)
camera_flag = 0

while True:
    qr_code_check()
    
    camera_flag = 1
    recording(camera_flag)
    minuto = timestamp()[2]
    while (GPIO.input(20) != GPIO.HIGH):
        led_control()
        data, hora, minuto_atual, segundo = timestamp()
        if (int(minuto_atual) == int(minuto) + 1):
            adicionar_temp(temp_control())
            adicionar_ruido(read_noise())
            minuto = minuto_atual
    
    camera_flag = 0
    recording(camera_flag)
    adicionar_video()
    cria_arquivo()
    enviar_json()
    
    