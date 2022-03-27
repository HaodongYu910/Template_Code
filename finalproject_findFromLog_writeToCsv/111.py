#!/usr/bin/env python3
import re
import sys
import csv
import operator

def findError(log_file):
    with open(log_file, mode='r',encoding='UTF-8') as f:
        error_list = []
        error = {}
        user = {}
        for line in f.readlines():
            error_pattern = r'(ERROR )(\w+.*)( [(])(\w+.*)([)])'
            info_pattern = r'(INFO)( \w+.*)( [(])(\w+.*)([)])'
            if re.search(error_pattern,line):
                # 找到error情况,并把具体信息放进error_list
                result = re.search(error_pattern,line)
                error_list.append(result.group(2))
                if result.group(4) in user:
                    user[result.group(4)]['error'] = user[result.group(4)]['error'] + 1 ####大问题！！！！！
                else:
                    user.update({result.group(4):{'info':0,'error':1}})
            else:
                # 运行正常info情况
                result = re.search(info_pattern,line)
                if result.group(4) in user:
                    user[result.group(4)]['info'] = user[result.group(4)]['info']+1
                else:
                    user.update({result.group(4):{'info':1,'error':0}})
        for i in set(error_list): # 用error_list做error_dict
            error.update({i:error_list.count(i)})
    f.close
    error = dict(sorted(error.items(), key = operator.itemgetter(1), reverse=True))
    user = dict(sorted(user.items(), key = operator.itemgetter(0)))
    return error,user

def dicToCsv_sin(dictionary,report_file):
    # print(dictionary)
    # new_dict = dict(sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True))
    # new_dict = {'Timeout while retrieving information': 15, 'Connection to DB failed': 13, 'Tried to add information to closed ticket': 12, 'Permission denied while closing ticket': 10, 'The ticket was modified while updating': 9, "Ticket doesn't exist": 7}
    with open(report_file, "w") as f:
        fieldnames = ['Error', 'count']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key,value in sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True):
            writer.writerow({'Error':key,'count':value})
        f.close()

def dicToCsv_com(dic,report_file):
    # print(dic)
    # new_dict = dict(sorted(dic.items(), key = operator.itemgetter(0)))
    # print(new_dict)
    # new_dict = {'ac': {'info': 2, 'error': 1}, 'ahmed.miller': {'info': 2, 'error': 3}, 'blossom': {'info': 1, 'error': 6}, 'bpacheco': {'info': 0, 'error': 1}, 'breee': {'info': 1, 'error': 4}, 'britanni': {'info': 0, 'error': 1}, 'enim.non': {'info': 2, 'error': 2}, 'flavia': {'info': 0, 'error': 4}, 'jackowens': {'info': 2, 'error': 3}, 'kirknixon': {'info': 1, 'error': 1}, 'mai.hendrix': {'info': 0, 'error': 2}, 'mcintosh': {'info': 4, 'error': 2}, 'mdouglas': {'info': 1, 'error': 3}, 'montanap': {'info': 0, 'error': 3}, 'noel': {'info': 5, 'error': 3}, 'nonummy': {'info': 2, 'error': 2}, 'oren': {'info': 2, 'error': 6}, 'rr.robinson': {'info': 1, 'error': 1}, 'sri': {'info': 2, 'error': 1}, 'xlg': {'info': 0, 'error': 3}}
    with open(report_file, "w") as f:
        fieldnames = ['Username', 'INFO', 'ERROR']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key,value in sorted(dic.items(), key = operator.itemgetter(0)):
            writer.writerow({'Username':key,'INFO':value['info'],'ERROR':value['error']})
        f.close()

# def write():
#     dic_a = {'ac': {'info': 2, 'error': 1}, 'ahmed.miller': {'info': 2, 'error': 3}, 'blossom': {'info': 1, 'error': 6}, 'bpacheco': {'info': 0, 'error': 1}, 'breee': {'info': 1, 'error': 4}, 'britanni': {'info': 0, 'error': 1}, 'enim.non': {'info': 2, 'error': 2}, 'flavia': {'info': 0, 'error': 4}, 'jackowens': {'info': 2, 'error': 3}, 'kirknixon': {'info': 1, 'error': 1}, 'mai.hendrix': {'info': 0, 'error': 2}, 'mcintosh': {'info': 4, 'error': 2}, 'mdouglas': {'info': 1, 'error': 3}, 'montanap': {'info': 0, 'error': 3}, 'noel': {'info': 5, 'error': 3}, 'nonummy': {'info': 2, 'error': 2}, 'oren': {'info': 2, 'error': 6}, 'rr.robinson': {'info': 1, 'error': 1}, 'sri': {'info': 2, 'error': 1}, 'xlg': {'info': 0, 'error': 3}}
#     dic_b = {'Timeout while retrieving information': 15, 'Connection to DB failed': 13, 'Tried to add information to closed ticket': 12, 'Permission denied while closing ticket': 10, 'The ticket was modified while updating': 9, "Ticket doesn't exist": 7}
#     with open('/home/student-00-ce162051efeb/user_statistics.csv', "w") as f:
#         fieldnames = ['Username', 'INFO', 'ERROR']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         for key,value in dic_a.items():
#             writer.writerow({'Username':key,'INFO':value['info'],'ERROR':value['error']})
#         f.close()
#     with open('/home/student-00-ce162051efeb/error_message.csv', "w") as f:
#         fieldnames = ['Error', 'count']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         for key,value in dic_b.items():
#             print(key)
#             print(value)
#             writer.writerow({'Error':key,'count':value})
#         f.close()

# write()

result = findError("/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/finalproject/syslog.log")
dicToCsv_sin(result[0],"/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/finalproject/error_message.csv")
dicToCsv_com(result[1],"/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/finalproject/user_statistics.csv")
