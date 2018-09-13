#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Amazfit Bip(米动手表 青春版) 한글 글자 비트맵 이미지 생성기
Amazfit Bip(米动手表 青春版) Korean Hangul glyph bitmap image generator
Copyright (c) 2018 Youngbin Han <sukso96100@gmail.com>

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PIL import ImageFont, ImageDraw, Image

hangulJamosRange = (0x1100, 0x11ff)
hangulSyllablesRange = (0xAC00, 0xD7AF)
# germanUmlauts = [0x00C4, 0x00E4, 0x00D6, 0x00F6, 0x00DX, 0x00FC, 0x1E9E, 0x00DF] 
print("""Amazfit Bip(米动手表 青春版) 한글 비트맵 이미지 생성기\n
      ©2018 Youngbin Han(sukso96100@gmail.com)\n
      이 스크립트는 한글 자모(U+1100~U+11FF) 와 한글 글자마디(U+AC00~U+D7AF) 에 헤당하는 파일만 생성합니다.""")
fontPath = input("사용할 글꼴 파일(*.ttf/*.otf) 경로 또는 이름 입력:")
destPath = input("""생성된 비트맵 이미지를 저장할 경로 입력. 마지막에 '/' 포함하여 입력. \n
                (이 스크립트 파일과 같은 경로에 저장하려면 비워두기)\n
                ~>""")
marginLeft = int(input("글자 왼쪽 간격 정수로 입력.(기본값:0)") or "0")
marginTop = int(input("글자 위쪽 간격 정수로 입력.(기본값:0)") or "0")


def printInRange(charRange, font):
    for i in range(charRange[0], charRange[1]):
        image = Image.new('1', (16, 16), "black")
        draw = ImageDraw.Draw(image)
        draw.text((marginLeft, marginTop), chr(i), font=font, fill="white")
        image.save("{}{:04x}4.bmp".format(destPath, i), "bmp")

def printInArray(charArray, font):
    for i in charArray:
        image = Image.new('1', (16, 16), "black")
        draw = ImageDraw.Draw(image)
        draw.text((marginLeft, marginTop), chr(i), font=font, fill="white")
        image.save("{}{:04x}4.bmp".format(destPath, i), "bmp")

print("글꼴 불러오는 중...")
font = ImageFont.truetype(fontPath, 15)

print("처리중...")
printInRange(hangulJamosRange, font)
printInRange(hangulSyllablesRange, font)
# printInArray(germanUmlauts, font)

print("작업 완료.")
