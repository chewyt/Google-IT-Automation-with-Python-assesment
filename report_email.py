#!/usr/bin/env python3

import os
import datetime
import reports
import emails

if __name__ == "__main__":

  desc_link = "supplier-data/descriptions/"
  desc = os.listdir(desc_link)
  #print(desc)# for checking list of files in the descriptions directory
  contents=""

  for info in desc:
    if info.endswith(".txt"):
      with open (desc_link + info) as information:
        line = information.read().split("\n")
        contents += "name: "+line[0]+"<br/>"+"weight: "+line[1]+"<br/><br/>"

  #print(contents)#for checking pdf contents

  title = "Processed Update on " + str(datetime.date.today())
  #print(title)

  reports.generate_report("/tmp/processed.pdf",title,contents)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"

  #generate email for the online fruit store report and pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)

