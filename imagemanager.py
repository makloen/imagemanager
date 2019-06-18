from os import walk, listdir, path
from shutil import copy

# Пошук всіх файлів з форматом .jpg або .png або .svg на диску E:\\
dirr = "E:\\"
dirs = [x[0] for x in walk(dirr)]

for row in dirs:
  for file in listdir(row):
    if file.endswith(".jpg"):
      try:
        copy(path.join(row, file), 'images\\jpg')
      except Exception as e:
        print(e)
    
    elif file.endswith(".png"):
      try:
        copy(path.join(row, file), 'images\\png')
      except Exception as e:
        print(e)
    
    elif file.endswith(".svg"):
      try:
        copy(path.join(row, file), 'images\\svg')
      except Exception as e:
        print(e)