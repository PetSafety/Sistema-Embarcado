from Modulos.imports import *

global camera = PiCamera()
camera.resolution = (640, 480)

def recording(flag):
    if flag == 1:
        camera.start_recording('/home/pi/Desktop/recording.h264')
    elif flag == 0:
        camera.stop_recording()
    else:
        pass

