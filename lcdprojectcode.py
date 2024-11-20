
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('/GrovePi-EE250/Software/Python')
# This append is to support importing the LCD library.
sys.path.append('/GrovePi-EE250/Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import setRGB, setText_norefresh, setText


if __name__ == '__main__':
    
    PORT = 4    # D4
    setText("")

    buf = ''
    while len(channel_names) <=10:
        buf = buf + '|'
        setText_norefresh(buf)
        setRGB(255,255,0)
    
    setRGB(0,255,0)

          




