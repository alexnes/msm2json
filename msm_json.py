#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exc_info, getsizeof
import json


def get_data(file_path, debug = False):
	data = []
	f = open(file_path)
	if debug: n = 0
	lines = f.readlines()
	if len(lines) > 0:
		lines = lines[1 : len(lines) - 3]

		buf = ""
		lines_new = []
		for s in reversed(lines):
			if s[0] == '{':
				if buf != "":
					s += buf
					buf = ""
				lines_new.append(s.replace('\r', '').replace('\n', '').replace('\t', '').decode('koi8_r').encode('utf-8'))
			else:
				buf += s

		for s in reversed(lines_new):
			if debug:
				n += 1				
				print "Processing line %d" % (n)
				print s
			try:
				data.append(json.loads(s))
			except ValueError:
				Type, Value, Trace = exc_info()
				if debug:
					print Value	
	if debug: return data, getsizeof(data),
	else: return data

if __name__ == '__main__':
	path = '/home/alex/ZDOS/C/saved3/'
	data={}
	msm_globals=['B1', 'B4', 'B9', 'B11', 'B12', 'B13', 'B14', 'B15', 'B18', 'B19', 'B27', 'B28', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40', 'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47', 'B48', 'B49', 'B50', 'B51', 'B52', 'B53', 'B54']	
	size = 0
	for g in msm_globals:
		print "Processing file %s ..." % (path + g)
		data[g]= get_data(path + g)
		print "Done.\n"
#	data, size = get_data(path + 'B1', debug = True)
#	print size

#for record in data:
#	if record['par']['i3'] == '80' or record['par']['i3'] == '134':
#		print 'data[%s, %s, %s] = %s' % (record['par']['i1'], record['par']['i2'], record['par']['i3'], record['val'])
#.replace("\\", "\\\\").replace("\"\"", "\"\\\"")