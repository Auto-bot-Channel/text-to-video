import os
import time

os.system('ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4')
time.sleep(3)
os.system('ffmpeg -i output.mp4 -i text.mp3 -c:v copy -c:a aac final_movie.mp4')
time.sleep(3)
print('final_movie.mp4 FINISHED')