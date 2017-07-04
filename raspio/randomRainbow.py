'''
randomRainbow.py
Display a random set of colors using the RasPiO InsPiRing
Author: Darrell Little
Date: 7/3/2017
Licensed under the GNU General Public License v3.0
'''

import time
import colorsys
from random import random
import apa  # apa.py must be in the same folder with this file

numleds = 8  # Set to number of leds in array
brightness = 5  # Set between 0 (off) and 31 (full on *CAUTION: EXTREMELY BRIGHT*)
delay = 0.1  # Set in seconds, smaller number will be smoother transition between colors
hue = 0  # this variable will change inside the loop

ledstrip = apa.Apa(numleds)  # initialize the apa object

print("Press Control+C to end program\n")

try:
    while True:
        hue = int(time.time() * 100) % 360 # Uses the time in seconds for a random hue
        for x in range(numleds):
            h = (hue % 360) / 360
            s = random()
            v = random()
            r, g, b = [int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v)]
            ledstrip.led_set(x, brightness, b, g, r)
            ledstrip.write_leds()
            time.sleep(delay)

# Press CTRL+C to stop and cleanup
except KeyboardInterrupt:
    print("\nAll LEDS Off - Goodbye!\n")
    ledstrip.reset_leds()

