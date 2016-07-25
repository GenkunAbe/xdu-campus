from PIL import Image, ImageEnhance, ImageFont, ImageDraw
import time
import random

font = ImageFont.truetype('CloudSongDaGBK.ttf', 17)



def rand_num(txt):

    x = random.randint(1, 4)
    y = random.randint(0, 2)
    angle = random.randint(-15, 15)

    num = Image.new('RGBA', (15, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(num)
    draw.text((x, y), txt, (255, 255, 255, 255), font = font)
    num = num.rotate(angle)
    return num

def rand_lines():
    num = random.randint(3, 5)
    img = Image.new('RGBA', (60, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    line_color = (153, 128, 153)
    for i in range(num):
        begin = (random.randint(0, 30), random.randint(0, 10))
        end = (random.randint(30, 60), random.randint(10, 10))
        draw.line([begin, end], fill=line_color, width=1)
    return img

if __name__ == '__main__':

    random.seed(int(time.time())

    bg = Image.open('bg.jpg')
    
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    num1 = rand_num(str(a))
                    num2 = rand_num(str(b))
                    num3 = rand_num(str(c))
                    num4 = rand_num(str(d))
                    lines = rand_lines()

                    bg.paste(num1, (0, 0), num1.split()[3])
                    bg.paste(num2, (13, 0), num2.split()[3])
                    bg.paste(num3, (26, 0), num3.split()[3])
                    bg.paste(num4, (39, 0), num4.split()[3])
                    bg.paste(lines, (0, 0), lines, split()[3])

                    bg.save('./code/%d%d%d%d.gif' % (a, b, c, d))