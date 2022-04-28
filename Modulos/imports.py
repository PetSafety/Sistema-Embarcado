import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import math
import random
from picamera import PiCamera
import smbus
from ctypes import c_short
from ctypes import c_byte
from ctypes import c_ubyte
import subprocess
import sys
import os
import paho.mqtt.client as mqtt
import json
import base64
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Definindo GPIOs como saída 
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inicializando GPIOs em nível lógico alto
GPIO.output(5,1)
GPIO.output(6,1)
GPIO.output(13,1)
GPIO.output(19,1)

json_path = "/home/pi/Desktop/json.json"