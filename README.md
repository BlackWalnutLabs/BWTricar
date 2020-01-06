# BWTricar

A Python library that can easily controls the Navigator based on `python-periphery`.

[README](README.md) | [中文文档](README_zh.md)

## Install

``` shell
git clone https://github.com/BlackWalnutLabs/BWTricar
cd BWTricar
python3 setup.py build
python3 setup.py install --user
```

## Import

``` python
import bwtricar
```

## Init

``` python
# Use 'ttyTHS1' by default
bwtricar.v2.init()
```

## Set speed

&emsp;&emsp;There are `5` gears in speed, based on linear speed. The values ​​correspond to 7, 14, 21, 28, 35 in the API documentation. The default speed is gear three.

``` python
bwtricar.v2.setSpeed(3)
```

## Simple Control

&emsp;&emsp;Developers can simply send orientation commands to control Navigator, such as 'left', 'right', 'straight' and 'stop'.

&emsp;&emsp;One command corresponds to one behavior, you can send commands frequently, but there is a priority between the commands, and the interval between sending commands can not be less than 150ms.

``` python
# Turn left
bwtricar.v2.sendCommand('left')

# Turn left quickly
bwtricar.v2.sendCommand('leftQuickly')

# Turn right
bwtricar.v2.sendCommand('right')

# Turn right quickly
bwtricar.v2.sendCommand('rightQuickly')

# Go straight
bwtricar.v2.sendCommand('straight')

# Turn around
bwtricar.v2.sendCommand('around')

# Stop
bwtricar.v2.sendCommand('stop')

# Still turn around until another command comes
bwtricar.v2.sendCommand('keepAround')
```

## Send API Command

&emsp;&emsp;Send control instructions based on [API documentation](docs/api_doc.pdf).

``` python
bwtricar.v2.sendCommandDirectly({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0})
```

## Serial port to send data directly

&emsp;&emsp;Send data directly to the serial port without preprocessing.

``` python
bwtricar.v2.sendCommandDirectlyWithoutJSON(bytes(json.dumps({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0}), encoding="utf8"))
```

## Command Priority

&emsp;&emsp;If there are two commands A and B, when the A command is issued and the vehicle has not completed the action required by the A command, the B command is issued, then the vehicle will judge what action should be run according to the priority of the AB command. If the A command has a higher priority than B, it will continue to run the A action and permanently discard the B command. If the priority of the B command is higher than A, the action of the A command is terminated, and the action of the B command is immediately executed. If A and B have the same priority, the action of the B command is executed.

|  Function Code   | Function Description  |
|  ----  | ----  |
| F1  | Free panning: keep the head facing unchanged and pan at any angle |
| F2  | Directional rotation: Rotate the specified degree in situ at the specified rate |
| F3  | Speed ​​control: control the speed and direction of the Navigator's in-situ rotation |
| F4  | Mixed motion: Free translation and simultaneous rotation, superimposed on each other. |
| F5  | Brake: Navigator stops moving |

**F5 > F2 > F4 = F3 = F1**

## Sample

* [Turn Left](sample/left.py)
* [Turn Left Quickly](sample/leftQuickly.py)
* [Turn Right](sample/right.py)
* [Turn Right Quickly](sample/rightQuickly.py)
* [Go Straight](sample/straight.py)
* [Turn Around](sample/around.py)
* [Stop](sample/stop.py)
* [Keep Turn Around](sample/keepAround.py)

## Change log

* 2020.01.06:
    * Turn slower.
    * Add `pan` command to `3rd` speed.
    * Add `turn` command to `3rd` speed.
* 2019.12.26:
    * Update reference.
* 2019.12.17:
    * Compatible with the previous usage of `2019.12.12`, the` ttyTHS1` serial port is used by default.
* 2019.12.12:
    * Added `USB` to serial port support (`ttyUSB0`).
    * Add change log.
    * Support sending data directly to serial port.
* 2019.11.07:
    * Add `Navigator` series product control `API` document.
* 2019.11.06:
    * Added Chinese documentation.
* 2019.08.26:
    * Supports `Jetson Nano` dock (`ttyTHS1`).
    * Open source the project.
    * Added English documentation.