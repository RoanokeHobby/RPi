from time import sleep      # RasPiO Inspiring scripts
import apa                  # http://rasp.io/inspiring
numleds = 8                # number of LEDs in our display
brightness = 5             # 0 = OFF, 31 = FULL
ledstrip = apa.Apa(numleds)

try:
    while True:
        for x in range(numleds):
            ledstrip.led_set(x, brightness, 0, 0, 255)  # red
        ledstrip.write_leds()
        sleep(1)
        for x in range(numleds):
            ledstrip.led_set(x, brightness, 0, 255, 0)  # green
        ledstrip.write_leds()
        sleep(1)
        for x in range(numleds):
            ledstrip.led_set(x, brightness, 255, 0, 0)  # blue
        ledstrip.write_leds()
        sleep(1)

finally:
    print("/nAll LEDs OFF - BYE!/n")
    ledstrip.zero_leds()
    ledstrip.write_leds()
