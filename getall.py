#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import check_output
import datetime

msm_globals=['B1', 'B4', 'B9', 'B11', 'B12', 'B13', 'B14', 'B15', 'B18', 'B19', 'B27', 'B28', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40', 'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47', 'B48', 'B49', 'B50', 'B51', 'B52', 'B53', 'B54']
folder_save="/home/alex/ZDOS/C/saved3/"


for g in msm_globals:
	now_time = datetime.datetime.now()
	print "%s\t\t Retrieving global: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), g)
	result = check_output(["./MSMCmd.pl", 'd ^GETGL("'+g+'")'])
	with open(folder_save + g, "w") as text_file:
	    text_file.write(result)	
	now_time = datetime.datetime.now()
	print "%s\t\t Global %s saved to file: %s" % (now_time.strftime("%d.%m.%Y %H:%M.%S"), g, folder_save + g)	    
