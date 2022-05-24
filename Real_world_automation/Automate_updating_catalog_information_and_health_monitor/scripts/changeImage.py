#!/usr/bin/env python3

from PIL import Image
import os


def convert_image():
    file_dic = "/Real_world_automation/Automate_updating_catalog_information_and_health_monitor/supplier-data/images"
    new_save_place = "/Users/yuhaodong/Desktop/CODE/VScode/Template_Code/Real_world_automation" \
                     "/Automate_updating_catalog_information_and_health_monitor/new_image"
    # new_save_place = "/home/student-00-faeacee2a0d2/test"

    for file in os.listdir(file_dic):
        if file.split('.')[-1] == "tiff":
            full_path = os.path.join(file_dic, file)
            im = Image.open(full_path)
            # 改图片尺寸
            new_im = im.resize((600, 400)).convert('RGB')
            # # 改图片格式，背景
            # new_im = new_im.convert('RGB')
            # 定义新图片存储路径
            new_path = os.path.join(new_save_place, file.split('.')[0] + '.jpeg')
            new_im.save(new_path)


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


if __name__ == "__main__":
    convert_image()
