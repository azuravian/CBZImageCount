import csv
from pathlib import Path
from tkinter import Tk, filedialog
from zipfile import ZipFile
import os
import time
from unrar import rarfile

root = Tk()
root.withdraw()

print('Select folder to scan for eComics...')
path = Path(filedialog.askdirectory())

print('Creating list of comics to search.')
cbz_list = [str(pp) for pp in path.glob("**/*.cbz")]
zip_list = [str(pp) for pp in path.glob("**/*.zip")]
file_list = cbz_list + zip_list

def cntimg(zipcontents):
    count = 0
    extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG', '.webp', '.WEBP')
    for i in zipcontents:
        if i.endswith(extensions):
            count += 1
    return count

#Check Files for JPG or PNG images
def check_zip(file):
    count = 0
    try:
        with ZipFile(file) as MyZip:
            zipcontents = MyZip.namelist()
            count = cntimg(zipcontents)
    except:
        pass
    return count    

for file in file_list:
    if ('.cbz' in file) or ('.zip' in file):
        num = check_zip(file)

    with open('Output.csv', mode='a', newline='', encoding='utf-8') as output:
        writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([file, str(num)])

print('Complete')
