#!/usr/bin/env python3

import os
from PIL import Image

image_link = "supplier-data/images/"
images = os.listdir(image_link)
print(images)
for image in images:
  if image.endswith(".tiff"):
    new_image_name = (image.replace(".tiff",".jpeg"))
    im = Image.open(image_link+image)
    new_im = im.convert("RGB").resize((600,400))
    new_im.save(image_link + new_image_name ,"jpeg")


