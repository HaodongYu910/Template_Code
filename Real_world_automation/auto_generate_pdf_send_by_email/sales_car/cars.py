#!/usr/bin/env python3

import json
import locale
import operator
import sys

from Real_world_automation.auto_generate_pdf_send_by_email.sales_car import emails, reports
from reports import generate


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    # 传入的data是一个从json转过来的dict
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0,
                   }
    max_sales = {"total_sales": 0}
    most_popular_year = {"year": 0, "this_year_total_sales": 0}
    sort_by_year = {}
    # 遍历json文件
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        # 找到收入最高的车子，total_sales * price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
        # 卖的最好的车型，什么车型，卖了多少钱
        item_count = item["total_sales"]
        if item_count > max_sales["total_sales"]:
            max_sales = item

        # TODO: also handle most popular car_year
        # 卖的最好的年份，哪年，卖了多少车。按照年份先存入sort_by_year字典
        item_year = item["car"]["car_year"]
        item_total_sales = item["total_sales"]
        if item_year in sort_by_year:
            sort_by_year[item_year] = sort_by_year[item_year] + item_total_sales
        else:
            sort_by_year[item_year] = item_total_sales

    # 用sort_by_year字典找到卖的最好的年
    for key, value in sort_by_year.items():
        if value > most_popular_year["this_year_total_sales"]:
            most_popular_year["year"] = key
            most_popular_year["this_year_total_sales"] = value
    # 输出summary
    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["total_sales"]),
        "The most popular year was {} with {} sales.".format(
            most_popular_year["year"], most_popular_year["this_year_total_sales"])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    # 处理一下数据，让数据根据total_sales的大小倒序排列
    data = sorted(car_data, key=operator.itemgetter('total_sales'), reverse=True)
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    summary_str_report = ""
    summary_str_emails = ""
    # 处理数据，让list变为string，并且增加换行字符<br/>
    for i in summary:
        summary_str_report = summary_str_report + i + "<br/>"
        summary_str_emails = summary_str_emails + i + "\n"
    print(summary_str_emails)
    table_data = cars_dict_to_table(data)
    # 引用reports.py中的generate方法
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", summary_str_report, table_data)
    # 引用emails.py中的generate方法，并用send方法发送邮件
    message = emails.generate("automation@example.com", "<user>@example.com", "Sales summary for last month", summary_str_emails, "/tmp/cars.pdf")
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
