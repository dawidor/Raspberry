from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.exposure_mode = 'beach'

camera.start_preview()

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
    print effect
