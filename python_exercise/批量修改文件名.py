import os
import sys

path = r"E:\电影\纯音乐（2）\女子十二乐坊 - 敦煌 2005"

for (path, dirs, files) in os.walk(path):
    for filename in files:
            newname="女子十二乐坊_敦煌 "+filename
            os.rename(path + "\\" + filename, path + "\\" + newname)