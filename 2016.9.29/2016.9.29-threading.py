#!/usr/bin/env python
'''
本程序内容主要通过urllib2 连接 亚马逊的api 但现在需要注册使用
	而本段讲解的是 多线程 在 I/O 阻塞应用的 的 效率性
'''

from atexit import register #装饰器
from re import compile #正则找出数据中想要的内容
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'https://amazon.com/dp/'
ISBNs = {'0132269937': 'Core Python Programming',} #isbn号 与书名

def getRanking(isbn):
	page = uopen('%s%s' % (AMZN, isbn)) # or str.format()
	data = page.read()
	page.close()
	return REGEX.findall(data)[0]

def _showRanking(isbn):
	print '- %r ranged %s' % (ISBNs[isbn], getRanking(isbn))

def _main():
	print "AT:", ctime(), "on Amazon..."
	for isbn in ISBNs:
		_showRanking(isbn)
		#上面是单线程
		#下面是多线程
		#
		#Thread(target=getRanking, args(isbn,)).start()
		# 

@register
def _atexit():
	print "all Done at: ", ctime()

if __name__ == '__main__':
	_main()
