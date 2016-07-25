from PIL import Image, ImageEnhance, ImageFont, ImageDraw
import time
import random
import hashlib

font = ImageFont.truetype('CloudSongDaGBK.ttf', 18)

def rand_num(txt):

	x = random.randint(1, 4)
	y = random.randint(0, 2)
	angle = random.randint(0, 1)

	num = Image.new('RGBA', (15, 20), (0, 0, 0, 0))
	draw = ImageDraw.Draw(num)
	draw.text((x, y), txt, (255, 255, 255, 255), font = font)
	num = num.rotate(angle)
	return num

def rand_lines():
	num = random.randint(2, 4)
	img = Image.new('RGBA', (60, 20), (0, 0, 0, 0))
	draw = ImageDraw.Draw(img)
	line_color = (101, 121, 151)
	for i in range(num):
		begin = (random.randint(0, 30), random.randint(0, 20))
		end = (random.randint(30, 60), random.randint(0, 20))
		draw.line([begin, end], fill=line_color, width=1)
	return img

if __name__ == '__main__':

	random.seed(int(time.time()))
	m = hashlib.md5()
	

	for a in range(10):
		for b in range(10):
			for c in range(10):
				for d in range(10):
					bg = Image.open('bg.jpg')
					num1 = rand_num(str(a))
					num2 = rand_num(str(b))
					num3 = rand_num(str(c))
					num4 = rand_num(str(d))
					lines = rand_lines()

					bg.paste(num1, (0, 0), num1.split()[3])
					bg.paste(num2, (13, 0), num2.split()[3])
					bg.paste(num3, (26, 0), num3.split()[3])
					bg.paste(num4, (39, 0), num4.split()[3])
					bg.paste(lines, (0, 0), lines.split()[3])

					m.update(str(time.time() * 1000 + random.randint(0, 100)))

					bg.save('./code/%d%d%d%d_%s.gif' % (a, b, c, d, m.hexdigest()[:6]))