import sys, os
from paramiko import SSHClient, AutoAddPolicy

class Server:
	def __init__(self, server, login):
		try: 
			self.__server = SSHClient()
			self.__server.set_missing_host_key_policy(AutoAddPolicy())
		except:
			print "Error: Could not create SSHClient object."
			sys.exit(1)
		try:
			self.__server.connect(server, username=login, look_for_keys=True)
		except:
			print "Error: Could not connect to "+server+" with login "+login+"."
			sys.exit(1)
   
	def cmd(self,command):
		return self.__server.exec_command(command)[1].read()#[:-1]
	def kill(self):
		self.__server.close()
