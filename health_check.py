#!/usr/bin/env python3

import socket
import psutil
import shutil
import emails
import os

def check_disk_usage(disk,min_percent):
  du = shutil.disk_usage(disk)
  percent_avail = 100 * du.free / du.total
  if percent_avail < min_percent:
    return True
  return False

def check_avail_memory(disk,min_MB):
  du = shutil.disk_usage(disk)
  avail_mem_MB = du.free / 2**20 
  #print("AvailableMemory: "+str(avail_mem_MB))
  if avail_mem_MB < min_MB:
    return True
  return False

def check_CPU_usage():
  usage = psutil.cpu_percent(1)
  return usage > 80

def check_no_network():
    """Returns True if it fails to resolve localhost, False otherwise"""
    try:
        socket.gethostbyname("127.0.0.1")
        return False
    except:
        return True

if __name__ == "__main__":

    #print("A")

    checks=[
        (check_disk_usage("/",20), "Error - Available disk space is less than 20%"),
        (check_avail_memory("/",500.0), "Error - Available memory is less than 500MB"),
        (check_CPU_usage(),"Error - CPU usage is over 80%"),
        (check_no_network(), "Error - localhost cannot be resolved to 127.0.0.1"),
    ]
    
    for check, msg in checks:
        if check == True:
            #print(msg)
            sender = "automation@example.com"
            receiver ="student-00-46d2007e55ad@example.com" #"{}@example.com".format(os.environ["USER"])
            subject = msg
            body = "Please check your system and resolve the issue as soon as possible."

            message = emails.generate_email(sender, receiver, subject, body)
            emails.send_email(message)
