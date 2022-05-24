#!/usr/bin/env python3
import os

import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
file_dic = "/Real_world_automation/Automate_updating_catalog_information_and_health_monitor/new_image"


def upload_image():
    for file in os.listdir(file_dic):
        if file.split('.')[-1] == 'JPEG':
            full_path = os.path.join(file_dic, file)
            with open(full_path, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
    return r.status_code


if __name__ == "__main__":
    upload_image()
