import smtplib
import getpass

from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from email.message import EmailMessage
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def generate_report():
    # 定义style
    styles = getSampleStyleSheet()

    # 定义输出文件路径
    report = SimpleDocTemplate("/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation"
                               "/auto_generate_pdf_send_by_email/report.pdf")

    # 定义文件title，以及title格式
    report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
    report_body = Paragraph("this is line 1 <br/> this is line 2", styles["BodyText"])

    # 定义水果字典
    fruit = {
        "elderberries": 1,
        "figs": 1,
        "apples": 2,
        "durians": 3,
        "bananas": 5,
        "cherries": 8,
        "grapes": 13
    }

    # 做一个表格
    table_data = []
    for k, v in fruit.items():
        table_data.append([k, v])
    # 定义table样式
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    # 做一个饼图
    # 饼图大小
    report_pie = Pie(width=3 * inch, height=3 * inch)
    report_pie.data = []
    report_pie.labels = []
    # 定义饼图数据
    for fruit_name in sorted(fruit):
        report_pie.data.append(fruit[fruit_name])
        report_pie.labels.append(fruit_name)
    # 饼图不能直接用，需要先画出来
    report_chart = Drawing()
    report_chart.add(report_pie)

    empty_line = Spacer(1, 20)
    # 输出文件
    report.build([report_title, empty_line, report_body, report_table, report_chart])


def send_email():
    # 配置email信息
    message = EmailMessage()
    sender = "me@example.com"
    recipient = "you@example.com"
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
    body = """Hey there! I'm learning to send emails using Python!"""
    message.set_content(body)


    # 准备发送email
    mail_server = smtplib.SMTP_SSL('smtp.example.com')
    mail_server.set_debuglevel(1)
    mail_pass = getpass.getpass('Password? ')
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == "__main__":
    generate_report()
