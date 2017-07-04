from time import sleep     # RasPiO Inspiring scripts
import apa                 # http://rasp.io/inspiring
numleds = 8               # number of LEDs in our display
delay = 0.10               # seconds between frames
brightness = 5             # 0=OFF (224 or 0xE0), 31=FULL (255 or 0xFF)
ledstrip = apa.Apa(numleds)

def updown(b,g,r):
    for led in range(numleds):
        ledstrip.led_set(led, brightness, b, g, r) 
        ledstrip.write_leds()
        sleep(delay)    

    for led in range(numleds -1, -1, -1):
        ledstrip.led_set(led, brightness, 0, 0, 0) 
        ledstrip.write_leds()
        sleep(delay)         
try:
    while True:
        print("BLUE")
        updown(255,0,0)		#Blue
        print("GREEN")
        updown(0,255,0)		#Green
        print("RED")
        updown(0,0,255)		#Red
        print("CYAN")
        updown(255,150,0)	#Cyan
        print("YELLOW")
        updown(0,150,255)	#Yellow
        print("MAGENTA")
        updown(150,0,255)	# Magenta
        print("WHITE")
        updown(255,255,255)	# White
        print("MAROON")
        updown(0,0,128)		# Maroon
        print("OLIVE")
        updown(0,128,128)	# Olive
        print("PURPLE")
        updown(128,0,128)	# Purple
        print("CRIMSON")
        updown(60,20,220)	# Crimson
        # delay = delay * 0.9	# speeds up each iteration

finally:
    print("/nAll LEDs OFF - BYE!/n")
    ledstrip.reset_leds()
