from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.exposure_mode = 'beach'

camera.start_preview()

camera.image_effect = 'posterise' 
camera.annotate_text = "Effect: posterise" 
sleep(10)


