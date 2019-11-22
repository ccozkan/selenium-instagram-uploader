import time
from stuff import image_path, image_name

# Enter script code
keyboard.send_keys('<ctrl>+l')
keyboard.send_keys(image_path)

keyboard.send_keys('<enter>')
time.sleep(3)



keyboard.send_keys('<ctrl>+f')
keyboard.send_keys(image_name)
keyboard.send_keys('<enter>')

