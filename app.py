import os 
import time

os.system('python3 audio.py')
time.sleep(1)
print('audio file made')
os.system('python3 req.py')
time.sleep(1)
print('alligned files')
os.system('python3 make.py')
time.sleep(1)

os.system('rm -r downl outd')
time.sleep(1)
os.system('rm output.mp4 list.txt')