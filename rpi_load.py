#GROVEPI STUFF

import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('/GrovePi-EE250/Software/Python')
# # This append is to support importing the LCD library.
sys.path.append('/GrovePi-EE250/Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import setRGB, setText_norefresh, setText

grovepi.set_bus("RPI_1")
setText("")
buf = ''
time.sleep(25)
for i in range(20):
    time.sleep(1)
    buf = buf + '#'
    setText_norefresh(buf)
    setRGB(225,165,0)
    setText_norefresh('\nLoading...')
setRGB(135,202,100)
setText_norefresh('\nComplete!')
