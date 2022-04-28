from Modulos.imports import *

JSON = {"temperatura": [], "ruido": [], "video": ""}
global dicionario 
dicionario = json.loads(JSON)

def adicionar_temp(valor):
    dicionario['temperatura'].append(str(valor))
    
def adicionar_ruido(valor):
    dicionario['ruido'].append(str(valor))
    
def adicionar_video():
    with open("/home/pi/Desktop/recording.h264", "rb") as videoFile:
        text = base64.b64encode(videoFile.read())
    dicionario['video'] = str(text)
    
def cria_arquivo():
    with open(json_path, 'w') as json_file:
        json.dump(dicionario, json_file)