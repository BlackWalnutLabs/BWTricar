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
