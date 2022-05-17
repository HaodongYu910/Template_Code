#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate(filename, title, additional_info, table_data):
    # 定义样式
    styles = getSampleStyleSheet()
    # 定义文件名字和路径
    report = SimpleDocTemplate(filename)
    # 定义报告标题
    report_title = Paragraph(title, styles["h1"])
    # 定义报告内容
    report_info = Paragraph(additional_info, styles["BodyText"])
    # 定义报告内表格样式
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER')]
    # 定义表格内容
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    # 空行
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])
