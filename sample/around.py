#
# Copyright (c) 2019, BlackWalnut Labs.  All rights reserved.
#
# BlackWalnut Labs. and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from BlackWalnut Labs. is strictly prohibited.
#

import bwtricar

bwtricar.v2.init('UART')
bwtricar.v2.setSpeed(3)
bwtricar.v2.sendCommand('around')