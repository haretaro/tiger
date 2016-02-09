# -*- coding: utf-8 -*-
import multiprocessing

#7バイト目
l_x = '00'
l_y = '01'
r_x = '02'
r_y = '03'

def read_axis(raw_value):
    value = int(raw_value, 16)
    if value >= 128:
	value = - 256 + value
    return value

def poll(f, file):
	with open(file, 'r') as js:
		data = []
		while True:
			for c in js.read(1):
				data.append('%02X' % ord(c))
				if len(data) == 8:
					#if data[6] == '01' and (data[4] == '00' or data[4] == '01'):
					#	f(data[4] == '01', data[7])
					if data[6] == '02' and (data[7] == l_x or data[7] == r_x):
					    axis = data[7]
					    value = read_axis(data[5])
					    f(value, axis)
					if data[6] == '02' and (data[7] == l_y or data[7] == r_y):
					    axis = data[7]
					    value = read_axis(data[5])
					    f(-value, axis)
					data = []

def queue(file):
	q = multiprocessing.Queue()
	f = lambda x, y: q.put((x, y))
	p = multiprocessing.Process(target=poll, args=(f, file))
	return (p, q)
