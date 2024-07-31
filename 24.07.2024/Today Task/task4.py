import os
import shutil 

#copy file from one location to other 

destinationpath=r"D:\Development\Live Class and Student Document\python\Python Module\two\file1.docx"
sourcepath=r"D:\Development\Live Class and Student Document\python\Python Module\one\file1.docx"

shutil.move(sourcepath,destinationpath)
print("Successfully Moved")