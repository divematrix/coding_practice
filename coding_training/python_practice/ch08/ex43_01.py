# 연습문제 43. 웹사이트 생성자

import os

def sethtml(title, author):
	base = []
	base.append('<!DOCTYPE html>\n')
	base.append('<html lang="en">\n')
	base.append('<head>\n')
	base.append('\t<meta charset="UTF-8">\n')
	base.append('<meta name="author" content="{}">\n'.format(author))
	base.append('\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n')
	base.append('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
	base.append('\t<title>{}</title>\n'.format(title))
	base.append('</head>\n')
	base.append('<body>\n')
	base.append('\t<b>자동 index.html 생성기</b>\n')
	base.append('</body>\n')
	base.append('</html>\n')
	return base

title = input("Site name : ")
author = input("Author : ")
js = input("Do you want a folder for JavaScript? ")
css = input("Do you want a folder for CSS? ")

os.makedirs('./coding_training/python_practice/ch08/ex43', exist_ok=True)

# 인코딩 설정 안하면 한글이 깨진다.
f = open('./coding_training/python_practice/ch08/ex43/index.html', 'w', encoding='utf-8')
f.writelines(sethtml(title, author))
f.close()

if js == 'y':
	os.makedirs('./coding_training/python_practice/ch08/ex43/js', exist_ok=True)

if css == 'y':
	os.makedirs('./coding_training/python_practice/ch08/ex43/css', exist_ok=True)