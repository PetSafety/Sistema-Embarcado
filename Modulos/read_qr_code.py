from Modulos.imports import *

box_id = 0001
broker = "broker.com"
port = 1883
topic = "pet-safety/qr-code-read"
username = 'petsafety'
password = 'catdog1998'

def connect_mqtt() -> mqtt_client:
    client = mqtt_client.Client(box_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client
    
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
            global mensagem
            mensagem = int(msg.payload.decode())
    client.subscribe(topic)
    client.on_message = on_message
    
def qr_code_check():
    while mensagem != box_id:
        continue
    client.unsubscribe(topic)
    client.disconnect()
    cmd_qrcode = 'sudo ifconfig wlan0 down'
    os.system(cmd_qrcode)