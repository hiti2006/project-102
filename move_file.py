import os
import shutil

from_dir="C:/Users/HP/Downloads"
to_dir="C:/Users/HP/Desktop/document_files"

listoffiles=os.listdir(from_dir)
#print(listoffiles)

for filename in listoffiles:
    name,ext=os.path.splitext(filename)
    #print(ext)
    #print(name)
    if ext=="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+"documentfiles"
        path3=to_dir+"/"+"documentfiles"+"/"+filename
        if os.path.exists(path2):
            print("moving"+filename)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+filename)
            shutil.move(path1,path3)