import time

import automationhat


import keyboard
import cv2


while True:
        try: 
                   
            if keyboard.is_pressed('q'):#if key 'q' is pressed 
                print('You Pressed A Key!')
                break#finishing the loop
            else:
                pass

while True:
        print('-')
        k = cv2.waitKey(2) & 0xFF
        if k == ord('q'):
            break
        elif k == ord('b'):
            value = automationhat.analog.one.read()
            print(value)
            continue
        elif k == ord('o'):
            automationhat.relay.one.toggle()
            continue

    #time.sleep(1.0)
