#!/usr/bin/env python3

import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

#report_title = Paragraph("Processed Update on "+datetime.date.today(), styles["h1"])

def generate_report(filename, title, report_contents):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(report_contents, styles["BodyText"])
  empty_line = Spacer(1,20)

  report.build([report_title,empty_line,report_info,empty_line])
