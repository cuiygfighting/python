from PIL import Image
import os
import os.path

path_old = r"C:\Users\d\Desktop\20190225"
path_new = r"C:\Users\d\Desktop\20190226"

filelist = os.listdir(path_old)
total_num = len(filelist)
print(total_num)

for parent, dirnames, filenames in os.walk(path_old):
    for filename in filenames:
        print('parent is :' + parent)
        print('filename is :' + filename)
        currentPath = os.path.join(parent, filename)
        print('the fulll name of the file is :' + currentPath)

        im = Image.open(currentPath)
        out = im.transpose(Image.ROTATE_180)
        newname = path_new  + '\\' + filename
        out.save(newname)

#ng = im.transpose(img.ROTATE_180) #旋转 180 度角。
#ng = im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
#ng = im.transpose(img.FLIP_TOP_BOTTOM)  # 上下对换。

# ng = im.rotate(180) #逆时针旋转 45 度角。
# im.transpose(img.FLIP_LEFT_RIGHT) #左右对换。
# im.transpose(img.FLIP_TOP_BOTTOM) #上下对换。
# im.transpose(Image.ROTATE_90) #旋转 90 度角。

# im.transpose(Image.ROTATE_270) #旋转 270 度角。
# im.show()
# ng.show()
