#coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.server import Server

class BaseDriver:
	def android_driver(self,i):
		print ("this is android_driver:",i)
		#devices_name adb devices
		#port
		write_file = WriteUserCommand()
		devices = write_file.get_value('user_info_'+str(i),'deviceName')
		port = write_file.get_value('user_info_'+str(i),'port')
		# capabilities = {
		#   "platformName": "Android",
		#   #"automationName":"UiAutomator2",
		#   "deviceName": devices,
		#   "app": "D:/mukeappium/app/MojiWeather.apk",
		#   "appWaitActivity":"com.moji.mjweather.LauncherActivity",
		#   "noReset":"true",
		#   # "platforVersion":"4.4.4",
		#   "appPackage":"com.moji.mjweather"
		#   #"newCommandTimeout":'180'
		# }
		caps = {}
		caps["platformName"] = "Android"
		caps["deviceName"] = devices
		caps['app'] = "D:/mukeappium/app/MojiWeather.apk"
		caps["appPackage"] = "com.moji.mjweather"
		caps["appActivity"] = "com.moji.mjweather.LauncherActivity"
		# caps['app'] = "C:/Users/Administrator/Desktop/111111.apk"
		# caps["appPackage"] = "net.changjinglu.mall"
		# caps["appActivity"] = "net.changjinglu.mall.HomeActivity"
		caps["noReset"] = "true"
		# caps["noSign"]: "true"
		driver = webdriver.Remote ("http://localhost:" + str (port) + '/wd/hub', caps)
		time.sleep (10)
		# driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
		# time.sleep(10)
		return driver

# if __name__ == '__main__':
#     Server.main()
#     time.sleep(20)
#     driver = BaseDrivre()
#     driver.android_driver(0)
