#!/usr/bin/python3
import gpiozero
import time
import sys

button = gpiozero.Button(12)
b = gpiozero.TonalBuzzer(17)
tone = gpiozero.tones.Tone

song = [ "D5", "A4", "B4", "F#4", "G4", "D4", "G4", "A4"]

def play(tones):
    for t in tones:
        b.play(tone(t))
        time.sleep(1)
        b.stop()

while True:
    if button.is_active is True:
        play(song)
