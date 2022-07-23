import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]



if bit == '32bit':
    from ss import mengeck_
    mengeck_()
