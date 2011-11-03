import sys
from server_class import Server

class ISP_Server(Server):

	def __init__(self,s_name,s_login):
		Server.__init__(self,s_name,s_login)
		self.vars = {"CHOWN":None,"MV":None,"CHMOD":None,"TAR":None,"CAT":None,"AWK":None,"DU":None,"FIND":None,"IPTABLES":None,"CP":None,"DBROOT":None,"SITE_DIR":None}

	def get_site_dir(domain):
		return self.cmd("")
	
	
	#def 
