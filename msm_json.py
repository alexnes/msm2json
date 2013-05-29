#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exc_info, getsizeof
import json
import datetime
import tarfile
from os import remove
from dictdiffer import DictDiffer
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

def debug_message(message):
	# converts the message to log-like format
	now_time = datetime.datetime.now()	
	return "%s\t %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), message)			

def get_data(file_path, debug = False):
	# Получить из файла список словарей {"par":{"id":<id>, "prop":<prop>}, "val":<val>}. Разные элементы списка могут иметь одинаковое значение ["par"]["id"]
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

def get_db(file_path):
	# Возвращает словарь {"<id>":{"<prop1>": <val1>, "<prop2>": <val2>, ...}}.
	data = {}
	f = open(file_path)
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
			try:
				line = json.loads(s)
				if data.get(line["par"]["id"]):
					data[line["par"]["id"]][line["par"]["prop"]] = line["val"]
				else:
					data[line["par"]["id"]] = {}
					data[line["par"]["id"]][line["par"]["prop"]] = line["val"]					
			except ValueError:
				Type, Value, Trace = exc_info()
	return data

def get_complete_db(
	path,
	source="FILE",
	msm_globals=('B1', 'B4', 'B9', 'B11', 'B12', 'B13', 'B14', 'B15', 'B18', 'B19', 'B27', 'B28',
	'B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40',	'B41', 'B42', 'B43', 'B44', 'B45',
	'B46', 'B47', 'B48', 'B49', 'B50', 'B51', 'B52', 'B53', 'B54'),
	debug=False):
	# Возвращает словарь, содержащий данные из всех (по умолчанию) или выбранных глобалей (msm_globals).
	# {"<global_name>": {"<id>": {"<prop1>": <val1>, "<prop2>": <val2>, ... }, ... }, ... }
	# В качестве источника данных выступает каталог с данными (path), выгруженными из MSM (source="FILE"),
	# каждая глобаль представлена в каталоге отдельным файлом с именем глобали,
	# или дамп полной базы в JSON-формате (source="JSON"), при этом в path передается полный путь к файлу
	data={}	
	if source.upper() == "FILE":
		if path[len(path) - 1] != '/': path += '/'
		for g in msm_globals:
			if debug:
				now_time = datetime.datetime.now()
				print "%s\t READ: processing file: %s%s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), path, g)
			data[g]= get_db(path + g)
	elif source.upper() == "JSON":
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t READ: processing file: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), path)		
		with open(path) as f:
		    data = json.load(f)	
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t READ: done." % (now_time.strftime("%d.%m.%Y %H:%M.%S"))		    
	return data

def dump_db(db, filename, debug=False):
	# Сохраняет словарь db в файл filename в формате JSONю
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP: processing file: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), filename)		
	with open(filename, 'w') as f:
		json.dump(db, f)	
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP: done." % (now_time.strftime("%d.%m.%Y %H:%M.%S"))		

def getdiff(db2, db1):
	# Возвращает словарь с такой же структурой, как и у db1 и db2. Словарь содержит записи, которые есть в db2 и отсутствуют в db1.
	diff = {}
	for global_name in db2:
		if db1.get(global_name) != None:
			for id2 in db2[global_name]:
				if db1[global_name].get(id2) == None:
					if diff.get(global_name) == None:
						diff[global_name] = {}
					diff[global_name][id2] = db2[global_name][id2]
		else:
			diff[global_name] = db2[global_name]
	return diff

def compress(archive=None, files=None, debug=False):
	# Создает archive (tar.bz2 архив) и добавляет в него файлы files
	if archive == None or files == None: pass
	tar = tarfile.open(archive, "w:bz2")
	for name in files:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t COMPRESS: processing file: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), name)
		tar.add(name)
	tar.close()	
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t COMPRESS: %s done" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), archive)

def extract(archive=None, path=".", debug=False):
	# Извлекает все файлы из архива archive в каталог path
	if archive == None: pass
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t EXTRACT: processing file: %s to %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), archive, path)	
	tar = tarfile.open(archive, "r:bz2")
	tar.extractall(path)
	tar.close()		
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t EXTRACT: %s done." % (now_time.strftime("%d.%m.%Y %H:%M.%S"), archive)		

def dump_compressed_db(db, filename, dbname="db.json", debug=False):
	# Сохраняет словарь db в сжатый tar.bz2 файл filename в формате JSON.
	dbname = "/tmp/" + dbname
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP_C: processing file: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), dbname)		
	with open(dbname, 'w') as f:
		json.dump(db, f)	
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP_C: compressing dump: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), filename)
	compress(filename, [dbname])
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP_C: removing temporary %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), dbname)		
	remove(dbname)
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t DUMP_C: done." % (now_time.strftime("%d.%m.%Y %H:%M.%S"))		

def get_file(remote_file, local_path, ip, username, password, debug=False):
	# Получает с удаленной машины файл remote_file с помощью scp и сохраняет его в local_path.
	if local_path[len(local_path) - 1] != '/': local_path += '/'
	ssh = SSHClient()
	ssh.set_missing_host_key_policy(AutoAddPolicy())
	ssh.load_system_host_keys()
	if debug:
		now_time = datetime.datetime.now()
		print "%s\t SCP: connecting to %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), ip)	
	try:
		ssh.connect(ip, username=username, password=password)
	except:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t SCP: failed to connect to %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), ip)			
	else:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t SCP: connected to %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), ip)					
	try:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t SCP: retrieving file %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), remote_file)					
		scp = SCPClient(ssh.get_transport())
		scp.get(remote_file, local_path)
	except:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t SCP: error: failed to retrieve file %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), remote_file)							
	else:
		if debug:
			now_time = datetime.datetime.now()
			print "%s\t SCP: file saved to %s folder" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), local_path)							
	ssh.close()		

if __name__ == '__main__':

	#data1 = get_complete_db("/home/alex/ZDOS/C/saved", source="file")
	#dump_db(data1, "db1.json")
	#data2 = get_complete_db("db2.json", source="json")
	#dump_compressed_db(data2, "db2.tar.bz2", "db2.json")
	#diff2 = getdiff(data2, data1)
	#dump_db(diff2, "diff2-1.json")

	#compress("diff.tar.bz2", ["diff2-1.json"])
	#extract("diff.tar.bz2", "saved/")

	#data = {}
	#for i in xrange(0,4):
	#	data[i] = get_complete_db("/home/alex/ZDOS/C/saved%d" % (i), source="file", debug=True)
	#	dump_db(data[i], "db%02d.json" % (i), debug=True)

	get_file("/home/admmsm/146200.tar", "saved", "192.168.20.2", "admmsm", "msm-bus", debug=True)


'''	d = DictDiffer(data2, data1)
	for i in d.changed():
		a = DictDiffer(data2[i], data1[i])
		for p in a.changed():
			b = DictDiffer(data2[i][p], data1[i][p])
			print i, p, b.changed()

	for gl in data1:
		for id1 in data1[gl]:
			if data2[gl].get(id1) != None:
				if data1[gl][id1] != data2[gl][id1]:
					print "==========================================="
					print gl, id1
					for prop in data1[gl][id1]:
						if data1[gl][id1][prop].encode('utf-8') != data2[gl][id1][prop].encode('utf-8'):
							print prop, data1[gl][id1][prop].encode('utf-8'), data1[gl][id1][prop].encode('utf-8')'''
