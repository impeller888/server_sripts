#!/usr/bin/python
# coding: utf-8
#main script

import sys
from classes.server_class import Server
#from classes.isp_class import ISP_Server
import ConfigParser

cfg = ConfigParser.ConfigParser()
srv = Server("ns7.hosting.reg.ru","imir")

#try:
#	cfg.read('srv.ini')
#	print cfg.get('BCKP','RSYNC_PREPARE_FILES')
#except ConfigParser.ParsingError:
#	print sys.exc_info()[1]
#except ConfigParser.NoSectionError:
#	print sys.exc_info()[1]
#except ConfigParser.NoOptionError:
#	print sys.exc_info()[1]


srv.connect()
print srv.check_connection()
print srv.cmd("uptime")
#srv.cmd("sudo /usr/local/bin/killdomain vmditalia.ru")
srv.disconnect()
#print srv.vars
