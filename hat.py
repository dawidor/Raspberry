import time

import automationhat
value = automationhat.analog.one.read()
print(value)
#while True:
automationhat.relay.one.toggle()
time.sleep(10.5)
