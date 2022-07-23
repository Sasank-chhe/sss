import os, platform
try:
   import requests
except:
   os.system('pip install requests')

import requests
bit = platform.architecture()[0]



if bit == '64bit':
    from ss import mengeck_
    mengecek_()
