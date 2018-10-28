from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.exposure_mode = 'beach'

camera.start_preview()
camera.capture('/home/pi/Desktop/image.jpg')
sleep(10)

for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)

camera.stop_preview()

camera.rotation = 180

camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
