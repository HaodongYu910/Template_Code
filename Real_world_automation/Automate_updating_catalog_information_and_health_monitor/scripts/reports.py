#!/usr/bin/env python3
import datetime
import json
import os
import calendar

from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

json_folder = "/home/student-00-3a23dd64b206/supplier-data/json_folder"


# def get_pdf_list(json_folder):
#     """
#     从储存了json文件的folder中提取需要的信息，储存在一个list中
#     """
#     pdf_list = []
#     for json_data in os.listdir(json_folder):
#         if json_data.split('.')[-1] == "json":
#             with open(os.path.join(json_folder, json_data), "r") as f:
#                 d = json.load(f)
#                 temp_dic = {"name": d["name"], "weight": str(d["weight"]) + " lbs"}
#                 pdf_list.append(temp_dic)
#     return pdf_list


def generate_report(paragraph, title, attachment):
    # 定义style
    styles = getSampleStyleSheet()

    # 定义输出文件路径
    report = SimpleDocTemplate(attachment)

    # 定义文件title，以及title格式
    now_time = datetime.datetime.now()
    report_title = Paragraph(title, styles["h1"])

    # 从一个list里面分离出发送pdf的文本内容,并定义文件body
    report_body = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1, 20)

    # 输出文件
    report.build([report_title, empty_line, report_body])

