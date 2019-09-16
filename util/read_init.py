#coding=utf-8
# import ConfigParser
import configparser
class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = '/Users/heboqiang/Desktop/代码/自动化代码/APP自动化/appium-hbq/config/LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path)
		return read_ini

	#通过key获取对应的value
	def get_value(self,key,section=None):
		if section == None:
			section = 'login_element'
		try:
			value = self.data.get(section,key)		
		except:
			value = None
		return value

if __name__ == '__main__':
	read_ini = ReadIni()
	print (read_ini.get_value("paizhao","login_element"))
	print (read_ini.get_value ("username", "login_element"))