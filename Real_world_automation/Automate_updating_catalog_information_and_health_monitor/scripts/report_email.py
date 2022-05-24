#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import datetime
import json
import os
import calendar

import reports, emails
json_folder = "/home/student-00-3a23dd64b206/supplier-data/json_folder"

if __name__ == "__main__":
    pdf_list = []
    temp_str = ""
    for json_data in os.listdir(json_folder):
        if json_data.split('.')[-1] == "json":
            with open(os.path.join(json_folder, json_data), "r") as f:
                d = json.load(f)
                temp_dic = {"name": d["name"], "weight": str(d["weight"]) + " lbs"}
                pdf_list.append(temp_dic)
    for dic in pdf_list:
        temp_str = temp_str + "name: {}<br/>weight: {}<br/><br/>".format(dic["name"], dic["weight"])
    now_time = datetime.datetime.now()

    title = "Processed Update on {} {}, {}".format(calendar.month_abbr[now_time.month], now_time.day, now_time.year)
    reports.generate_report(temp_str,title,"/tmp/processed.pdf")
    message = emails.generate_email("automation@example.com", "student-00-3a23dd64b206@example.com", "Upload Completed - Online Fruit Store",
                       "All fruits are uploaded to our website successfully. A detailed list is attached to this "
                       "email.",
                       "/home/student-00-3a23dd64b206/processed.pdf")
    emails.send_email(message)
