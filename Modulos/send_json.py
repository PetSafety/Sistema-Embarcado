from Modulos.imports import *

API_ENDPOINT = "http://endpoint.com/post"

def enviar_json():
    cmd_qrcode = 'sudo ifconfig wlan0 up'
    os.system(cmd_qrcode)
    arquivo_json = json.load(json_path)
    r = requests.post(url = API_ENDPOINT, data = arquivo_json)