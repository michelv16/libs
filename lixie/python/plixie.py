#!/usr/bin/env python3
# Module to control Lixie displays
# Author: Michel Verlaan (michel.verl@gmail.com)
#

import time
from rpi_ws281x import PixelStrip, Color

LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

LIXIE_ELEMENTS = 4
LIXIE_LEDS_PER_ELEMENT = 20

pixelStrip = PixelStrip((LIXIE_LEDS_PER_ELEMENT*LIXIE_ELEMENTS), LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

class Element:
    def __init__(self, elementNumber):
        self.elementNumber = elementNumber
        self.offset_begin = elementNumber * LIXIE_LEDS_PER_ELEMENT
        self.offset_end = self.offset_begin + LIXIE_LEDS_PER_ELEMENT
        
        # Corresponding LED numbers, for example: number 0 has LED 6 and 16
        self.numberToLeds = [6, 5, 7, 9, 1, 3, 4, 2, 0, 8]

        pixelStrip.begin()

    # Clear the element
    def Clear(self):
        i = self.offset_begin
        while i < self.offset_end:
            pixelStrip.setPixelColor(i, Color(0, 0, 0))
            pixelStrip.show()
            i += 1

    def SetElement(self, number, color):
        pixelStrip.setPixelColor((self.offset_begin + self.numberToLeds[number]), color)
        pixelStrip.setPixelColor(self.offset_begin + (self.numberToLeds[number] + 10), color)
        pixelStrip.show()
