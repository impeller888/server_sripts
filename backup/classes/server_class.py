import sys
from paramiko import SSHClient, AutoAddPolicy
import logging
import ConfigParser

logging.basicConfig()
logger = logging.getLogger()
hdlr = logging.FileHandler('./error.log')
logger.addHandler(hdlr) 
formatter = logging.Formatter('%(levelname)s: %(message)s')
hdlr.setFormatter(formatter)

cfg = ConfigParser.ConfigParser()

class Server:

	def __init__(self,s_name,s_login):
		self.__s_name = s_name
		self.__s_login = s_login
		self.vars = {}
		self.__config_name = "srv.conf"
		try: 
			self.__server = SSHClient()
			self.__server.set_missing_host_key_policy(AutoAddPolicy())
		except:
			logger.critical("Could not create SSHClient object.")

	def check_connection(self):
		return self.__s_login == self.cmd("whoami")

	def connect(self):
		try:
			self.__server.connect(self.__s_name, username=self.__s_login, look_for_keys=True)
		except:
			logger.error("Could not connect to "+self.__s_name+" with login "+self.__s_login+".")
			return 1

	def disconnect(self):
   		try:
			self.__server.close()
		except:
			logger.critical("Could not disconnect from server "+self.__s_name+".")
			return 1

	def cmd(self,command):
		try:
			return self.__server.exec_command(command)[1].read()[:-1]
		except:
			logger.critical("Could not execute command.")
			return 1

	def load_config(self):
		try:
			cfg.read('srv.ini')
			for item in self.vars:
				pass
			return 0
		except ConfigParser.ParsingError:
			logger.error("Loading config error: "+sys.exc_info()[1])
		except ConfigParser.NoSectionError:
			logger.error("Loading config error: "+sys.exc_info()[1])
		except ConfigParser.NoOptionError:
			logger.error("Loading config error: "+sys.exc_info()[1])
		return 1
	
	def uptime(self):
		return self.cmd("cat /proc/loadavg | awk '{print $1}'")
