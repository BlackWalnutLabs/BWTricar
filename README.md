# BWTricar

A Python library that easily controls the Navigator

## Install

``` shell
python3 setup.py build
python3 setup.py install --user
```

## Sample

``` python
import bwtricar

bwtricar.v2.init()
bwtricar.v2.setSpeed(5)
bwtricar.v2.sendCommand('straight')

bwtricar.v2.sendCommandDirectly({'o': 0, 'v': 0, 'c': 0, 'd': 0, 'r': 0, 'a': 0})
```