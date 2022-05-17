#! /usr/bin/env python3
import json
import os
import requests

remote_url = '1.1.1.1'
txt_folder = "/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation/Process_txt_upload_to_web/feedback"
json_folder = "/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation/Process_txt_upload_to_web/json_folder"


# import json
# import os
# import requests
#
# remote_url = 'http://34.70.2.245/feedback'
# txt_folder = "/data/feedback"
# json_folder = "/home/student-00-faeacee2a0d2/json_folder"


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



def readTXT():
    """
    从linux文档中读取多个txt文件，并按照title，author，date，feedback的格式存入json字符串
    """
    for file in os.listdir(txt_folder):
        if file.split('.')[-1] == "txt":
            print("now we open {}".format(file))
            with open(os.path.join(txt_folder, file), "r") as f:
                a = f.readlines()
                data = {
                    "title": a[0].strip(),
                    "name": a[1].strip(),
                    "date": a[2].strip(),
                    "feedback": a[3].strip()
                }
            with open(os.path.join(json_folder, file.split('.')[0] + ".json"), "w") as f:
                json.dump(data, f, indent=2)


if __name__ == "__main__":
    readTXT()
    uploadToWeb(json_folder)



