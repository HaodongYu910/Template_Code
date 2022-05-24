# Template_Code
Documents introduction:
    find_error from log
        
        使用正则表达式对日志文件中的错误信息进行截取，并把错误信息打印出来
        

   linux_scripts
        
        biomind时期，写过的一些linux scripts，包括以下指令的一些用法：
            awk
            sed
            while loop
            grep
            cut
        

   read-write csv sample
        
        如何用python读取csv文件，主要用到csv.reader()，with open()等
        

   regular expression quiz - replace email
        
        使用正则表达式，把email address中的姓名颠倒，主要用到了正则中小括号分部分的方法
        

   unit_test
   
        使用unittest基础tamplate，python自带的测试方法
        
        
   change_linuxFileName
        
        在指定文件夹中，找到包含指定信息的文件，并将其重命名保存。


   debug_part_final
   
        debug.py
            对一个入职员工的csv文件做处理：如下要求
            1. 找到特定日期之后入职的员工
            2. 获得当前日期
            
            知识点：
                # 这个方法可以让遍历时对字典进行顺序操作，operator后面的item值可以选择特定域进行升序或者降序。
                for key,value in sorted(info_dic.items(), key = operator.itemgetter(0), reverse=False):
                    print("Started on {}: {}".format(key.strftime("%b %d, %Y"), value))
                
        employees-with-data.csv
            入职员工时间数据表
   
   
   finalproject_findFromLog_writeToCSV
        
        111.py
            python文件，如下要求：
            1. 使用正则表达式读取日志文件中的信息
            2. 统计error种类
            3. 统计每一个user日志下的error和info信息的数量
            
            知识点：
                将dic写为csv文件
                正则表达式
                对字典选择特定域进行升序或者降序排列遍历
        
        sys.log
            日志文件
            
            
   Occupy_a_port
        
        有趣的一个文件，在linux系统中启动可以占用特定的端口，并且给访问该端口回复特定信息
   
   
   Real_World_Automation：

        you've seen how you can modify images using Python Imaging Library; how you can interact with web services using the Python requests module, sending data in JSON format; how you can generate PDF files with the content you want; and how you can send emails with those PDFs as an attachment. 
        实际生活正可能用到的自动化例子：
        
        1. change_image_mode：
            利用python的external lib中的pillow库，对照片文件进行处理
            (1). 更改照片尺寸
            (2). 更改照片格式
            (3). 保存照片到一个新的位置
            知识点：
                可能会遇到os error 不能吧LA格式转换为JPG格式等，参考script.py中 “_colorspace”方法，即可解决
                
                def _colorspace(image, colorspace, format):
                    if colorspace == 'RGB':
                        # Pillow JPEG doesn't allow RGBA anymore. It was converted to RGB before.
                        if image.mode == 'RGBA' and format != 'JPEG':
                            return image  # RGBA is just RGB + Alpha
                        if image.mode == 'LA' or (image.mode == 'P' and 'transparency' in image.info):
                            if format == 'JPEG':
                                newimage = Image.new('RGB', image.size, '#eebbaa')
                                mask = image.convert('RGBA').split()[-1]
                                newimage.paste(image.convert('RGBA'), (0, 0), mask)
                            else:
                                newimage = image.convert('RGBA')
                                transparency = image.info.get('transparency')
                                if transparency is not None:
                                    mask = image.convert('RGBA').split()[-1]
                                    newimage.putalpha(mask)
                            return newimage
                        return image.convert('RGB')
                    if colorspace == 'GRAY':
                        return image.convert('L')
                    return image
        
        2. Process_txt_upload_to_web
            (1).利用python中的json方法，对txt文件中的内容编辑并输出json文件
            (2).读取json文件，转换为python可读取的dictionary，并使用request.post方法将其发送到指定服务器
            知识点：
                a. 可以用str.split('.')[-1]检查文件的后缀名
                b. 利用a=f.readlines(),返回值a为一个list，可以直接调用list中的序号得到特定行内容
        
        3. auto_generate_pdf_send_by_email
            (1). 处理json数据，找出销量最好的车，以及销量最好的年份
            (2). 将处理好的数据编辑出来一个table，并生成一个pdf文件
            (3). 使用email将pdf文件发送出去
            知识点：
                a. 以下方法可以得到文件的文件名，扩展名
                    with open(attachment_path, 'rb') as ap:
                        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
                b. 以下方法可以根据指定key，对list内嵌套字典排序
                    data = sorted(car_data, key=operator.itemgetter('total_sales'), reverse=True)
                c. 生成pdf的body文件中，字符串中使用<br/>可以进行换行
                d. 生成emails可以看emails.py，生成报告看reports.py
        
        4， 综合前三个
            (1). 处理图片，改为600*400，JPEG模式
            (2). 上传图片到url
            (3). 处理txt文档，转存为json文件，上传到url
            (4). 创建pdf文件，作为附件发送邮件
            (5). 机器运行状态监测，有问题发邮件
            
        
