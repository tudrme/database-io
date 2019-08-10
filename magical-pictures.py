"""
Process the pics or something like that
"""

import os
from PIL import Image
for file in os.listdir("oof"):
    Image.open('oof/' + file).convert('RGB').save('oof_out/' + file + '.jpg')
    print(file)