import os
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys


# 스티커 파일 입력받기

# 결과물을 저장할 폴더를 생성합니다.
out_dir ="스티커 인쇄"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# 스티커 로고파일 불러오기
logo = Image.open('Fullplan.png')

# 픽셀 지정
Xdim = 355
Ydim = 592

# # 흰색 배경 새로운 이미지 제작
# image = Image.new("RGBA", (Xdim, Ydim), "white")

# 프레임 삽입
# image.paste(logo)

# 스티커에 삽입할 폰트 결정

namefont = ImageFont.truetype("font/GmarketSansTTFMedium", 5)
infofont = ImageFont.truetype("font/GmarketSansTTFMedium", 3)

f = open('subscriber_Data1.csv', 'r')
rdr = csv.reader(f)

for line in rdr:

    # 명함에 들어갈 정보들만 추출
    name = line[0]
    gram = line[1]
    recipe = line[2]
    count = line[3]
    age = line[4]
    weight = line[5]
    Dog_type = line[6]
    sex = line[7]
    special_note = line[8]

    sticker = logo.copy()

logo.close()