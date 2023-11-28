import serial
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

distancia= []
tiempo = []
arduinoData = serial.Serial('COM29', 9600)
plt.ion()
fig=plt.figure()

while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline().decode().strip("\n")
    print(arduinoString)
    
    distancia.append(int(arduinoString))

    now = datetime.now()
    tmp=now.strftime("%H:%M:%S")
    tiempo.append(tmp)

    plt.plot(tiempo, distancia, label='Tiempo')
    plt.pause(0.05)

    if(len(distancia)>10):
        fig.clear()
        distancia.pop(0)
        tiempo.pop(0)
    
    plt.ylim(0, 120 if max(distancia)>50 else 50 if max(distancia)>20 else 20)
    plt.xticks(rotation=90)
 