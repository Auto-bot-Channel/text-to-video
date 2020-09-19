import requests
from googleImage import GoogleImage
import os
import time

def filt(w): 
    n = max([w.find('<'), w.find('>'),w.find('-')])
    m = len(w) < 4
    print(n,m)
    if n != -1 or m == True:
        return True
    return False


params = (
    ('async', 'false'),
)

files = {
    'audio': ('text.mp3', open('text.mp3', 'rb')),
    'transcript': ('text.txt', open('text.txt', 'rb')),
}

r = requests.post('http://gentle-demo.lowerquality.com/transcriptions', params=params, files=files)
r = r.json()

data = []
last = 0

for x in r['words']:
    try:
        if not filt(x['alignedWord']):
            data.append([x['alignedWord'] , 1/(x['end']-last) ])
            last = x['end']
    except:
        pass

Img = GoogleImage()
listf = open("list.txt", "w")
os.system('mkdir outd')

print(data)

count = 1
for x,_ in data:
	Img.getImg(name=x, count=count)
	listf.write(f"file './outd/out{count}.mp4'\n")
	count +=1 
listf.close
Img.close()

for x in range(1,len(data)+1):
	os.system(f'ffmpeg -framerate {data[x-1][1]} -i ./downl/i{x}.jpg  -s 1280x720 -r 30 -pix_fmt yuv420p ./outd/out{x}.mp4')
	time.sleep(0.1)

time.sleep(1)
