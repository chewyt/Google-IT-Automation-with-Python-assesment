#! /usr/bin/env python3


import os
import requests

desc_link = "supplier-data/descriptions/"
desc = os.listdir(desc_link)
#print(desc)
#create a dictionary to hold info
fruit_data={}
for info in desc:
  with open (desc_link + info) as information:
    line = information.read().split("\n")
    fruit_data = {'name':line[0],'weight':int(line[1].replace("lbs","")),'description':line[2],'image_name':info.replace(".txt",".jpeg")}
    #print(data)
    request = requests.post('http://34.122.29.100/fruits/',data = fruit_data)

