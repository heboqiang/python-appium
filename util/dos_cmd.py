#coding=utf-8
import os
class DosCmd:
	def excute_cmd_result(self,command):
		devices = os.popen ('adb devices').readlines()[1:-1]
		if len (devices) != 0:
			device = []
			for a in devices:
				c = a.strip('\tdevice\n')
				device.append (c)
			return device
		else:
			return '设备未连接，请检查设备！'

	def excute_cmd(self,command):
		os.system(command)

if __name__ == '__main__':
	dos = DosCmd()
	print(dos.excute_cmd_result('adb devices'))
