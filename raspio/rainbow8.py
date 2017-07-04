'''
rainbow8.py
Display a rainbow of colors with the RasPiO InsPiRing
Author: Darrell Little
Date: 7/3/2017
Licensed under the GNU General Public License v3.0
Portions of this software Copyright (c) 2017 Pimoroni Ltd - MIT License
'''

import time
import colorsys
import apa  # apa.py must be in the same folder with this file

numleds = 8  # Set to number of leds in array
brightness = 3  # Set between 0 (off) and 31 (full on *CAUTION: EXTREMELY BRIGHT*
delay = 0.02  # Set in seconds, smaller number will be smoother transition between colors

ledstrip = apa.Apa(numleds)  # initialize the apa object

# Set the color spacing for the
# separation of colors across the led strip at a time
# Use a number between 1 (less) and 360 (more)
colorSpacing = 64
hue = 0   # This variable changes while in the loop

print("Press Control+C to end program\n")

try:
    while True:
        hue = int(time.time() * 100) % 360 # Uses the time in seconds for a random hue
        for x in range(numleds):
            offset = x * colorSpacing # The pixel number times the color spacing value
            h = ((hue + offset) % 360) / 360.0 # A number between 0 and 1 to use in hsv_to_rgb function
            r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            ledstrip.led_set(x, brightness, b, g, r)
            ledstrip.write_leds()
            time.sleep(delay)

# Press CTRL+C to stop and cleanup
except KeyboardInterrupt:
    print("\nAll LEDS Off - Goodbye!\n")
    ledstrip.reset_leds()
