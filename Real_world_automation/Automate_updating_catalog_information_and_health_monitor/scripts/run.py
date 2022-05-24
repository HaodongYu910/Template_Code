#! /usr/bin/env python3
import json
import os
import requests

remote_url = '1.1.1.1'
txt_folder = "/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation/Automate_updating_catalog_information_and_health_monitor/supplier-data/descriptions"
json_folder = "/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation/Automate_updating_catalog_information_and_health_monitor/json_folder"

# remote_url = 'http://34.70.2.245/feedback'
# txt_folder = "/data/feedback"
# json_folder = "/home/student-00-faeacee2a0d2/json_folder"




def readTXT():
    """
    从linux文档中读取多个txt文件，并按照name，weight，description，image_name的格式存入json字符串
    """
    for file in os.listdir(txt_folder):
        if file.split('.')[-1] == "txt":
            print("now we open {}".format(file))
            with open(os.path.join(txt_folder, file), "r") as f:
                a = f.readlines()
                data = {
                    "name": a[0].strip(),
                    "weight": int(a[1].split()[0].strip()),
                    "description": a[2].strip(),
                    "image_name": file.split('.')[0].strip() + ".JPEG"
                }
            with open(os.path.join(json_folder, file.split('.')[0] + ".json"), "w") as f:
                json.dump(data, f, indent=2)

def uploadToWeb(json_folder):
    """
    遍历json_folder，把其中的json格式的文件变为dict使用post方式上传到指定网站
    """
    for json_data in os.listdir(json_folder):
        if json_data.split('.')[-1] == "json":
            with open(os.path.join(json_folder,json_data),"r") as f:
                d = json.load(f)
                reponse = requests.post(url=remote_url, data = d)
                print(reponse.status_code)
                print(reponse.reason)






if __name__ == "__main__":
    readTXT()
    # uploadToWeb(json_folder)



