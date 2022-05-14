from PIL import Image
import os

def convert_image():
    file_dic = "/home/student-00-faeacee2a0d2/images"
    new_save_place = "/opt/icons/"
    # new_save_place = "/home/student-00-faeacee2a0d2/test"

    for file in os.listdir(file_dic):
        if file == ".DS_Store":
            continue
        else:
            full_path = os.path.join(file_dic,file)
            im = Image.open(full_path)
            new_im = im.rotate(90).resize((128,128))
            new_im = _colorspace(new_im,'GRAY','jpeg')
            new_path = os.path.join(new_save_place,file[:-4]+'.jpg')
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
