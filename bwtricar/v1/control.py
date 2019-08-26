# coding=utf-8
# module.py 常用模块

from periphery import Serial
import json

serial = None

speedParams = [{
    'left': {'CM': 5, 'TL': 40, 'TR': 92},
    'right': {'CM': 5, 'TL': 92, 'TR': 40},
    'straight': {'CM': 5, 'TL': 50, 'TR': 50},
    'around': {'CM': 6, 'TL': 50, 'TR': 50},
    'stop': {'CM': 5, 'TL': 0, 'TR': 0},
}, {
    'left': {'CM': 5, 'TL': 75, 'TR': 180},
    'right': {'CM': 5, 'TL': 180, 'TR': 75},
    'straight': {'CM': 5, 'TL': 100, 'TR': 100},
    'around': {'CM': 6, 'TL': 50, 'TR': 50},
    'stop': {'CM': 5, 'TL': 0, 'TR': 0},
}]

currentAbsSpeed = speedParams[1]

def init():
    global serial

    serial = Serial('/dev/ttyTHS1', 115200)

def setSpeed(speed):
    global currentAbsSpeed

    currentAbsSpeed = speedParams[speed - 1]


def sendCommand(command):
    serial.write(bytes(json.dumps(currentAbsSpeed[command]), encoding="utf8"))
