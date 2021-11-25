#!/usr/bin/env python3

import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

image_link = "supplier-data/images/"
images = os.listdir(image_link)

url = "http://localhost/upload/"

for image in images:
  if image.endswith(".jpeg"):
    with open(image_link+image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
