import os
import glob
last_dir = ''
dir = r'input'

os.chdir(dir)
dir = os.getcwd()
list = glob.glob('*.*')
for el in range(len(list)):
    print(list[el])
