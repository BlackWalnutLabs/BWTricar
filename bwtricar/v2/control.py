# coding=utf-8

#
# Copyright (c) 2019, BlackWalnut Labs.  All rights reserved.
#
# BlackWalnut Labs. and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from BlackWalnut Labs. is strictly prohibited.
#

from periphery import Serial
import json

serial = None

speedParams = [{
    'left': {'o': 0, 'v': 6, 'c': 0, 'd': 0, 'r': 20000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 5, 'c': 0, 'd': 0, 'r': 9000, 'a': 0},
    'right': {'o': 0, 'v': 6, 'c': 0, 'd': 1, 'r': 20000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 5, 'c': 0, 'd': 1, 'r': 9000, 'a': 0},
    'straight': {'o': 0, 'v': 7, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 1000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround':{'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 6000, 'a': 0}
}, {
    'left': {'o': 0, 'v': 12, 'c': 0, 'd': 0, 'r': 18000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 0, 'r': 7000, 'a': 0},
    'right': {'o': 0, 'v': 12, 'c': 0, 'd': 1, 'r': 18000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 1, 'r': 7000, 'a': 0},
    'straight': {'o': 0, 'v': 14, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 1000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround':{'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 6000, 'a': 0}
}, {
    'left': {'o': 0, 'v': 15, 'c': 0, 'd': 0, 'r': 15000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 0, 'r': 7000, 'a': 0},
    'right': {'o': 0, 'v': 15, 'c': 0, 'd': 1, 'r': 15000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 1, 'r': 7000, 'a': 0},
    'straight': {'o': 0, 'v': 21, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 1000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround':{'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 6000, 'a': 0}
}, {
    'left': {'o': 0, 'v': 24, 'c': 0, 'd': 0, 'r': 13000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 0, 'r': 7000, 'a': 0},
    'right': {'o': 0, 'v': 24, 'c': 0, 'd': 1, 'r': 13000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 1, 'r': 7000, 'a': 0},
    'straight': {'o': 0, 'v': 28, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 1000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround':{'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 6000, 'a': 0}
}, {
    'left': {'o': 0, 'v': 29, 'c': 0, 'd': 0, 'r': 10000, 'a': 0},
    'leftQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 0, 'r': 7000, 'a': 0},
    'right': {'o': 0, 'v': 29, 'c': 0, 'd': 1, 'r': 10000, 'a': 0},
    'rightQuickly': {'o': 0, 'v': 10, 'c': 0, 'd': 1, 'r': 7000, 'a': 0},
    'straight': {'o': 0, 'v': 35, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'around': {'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 1000, 'a': 180},
    'stop': {'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0},
    'keepAround':{'o': 0, 'v': 0, 'c': 0, 'd': 1, 'r': 6000, 'a': 0}
}]

currentAbsSpeed = speedParams[2]

interfaceDict = {
    'UART': '/dev/ttyTHS1',
    'USB': '/dev/ttyUSB0'
}

def init(interfaceType = 'UART'):
    global serial

    if(interfaceDict.get(interfaceType) != None):
        serial = Serial(interfaceDict[interfaceType], 115200)
    else:
        print('Interface type not exist, please concat us.')

def setSpeed(speed):
    global currentAbsSpeed

    currentAbsSpeed = speedParams[speed - 1]

def sendCommand(command):
    serial.write(bytes(json.dumps(currentAbsSpeed[command]), encoding="utf8"))

def sendCommandDirectly(command):
    serial.write(bytes(json.dumps(command), encoding="utf8"))

def sendCommandDirectlyWithoutJSON(command):
    serial.write(command)