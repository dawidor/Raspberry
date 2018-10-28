import time
import automationhat
import keyboard
import cv2

while True:
    try:
        if keyboard.is_pressed('q'):
            print('You Pressed A Key!')
            automationhat.relay.one.toggle()
            break
        else:
            continue
