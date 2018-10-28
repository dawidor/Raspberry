from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

camera.annotate_text_size = 50
camera.brightness = 70
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

camera.resolution = (2592, 1944)
camera.framerate = 15

for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    camera.contrast = i
    sleep(0.1)

camera.annotate_text = "Hello world!"
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
