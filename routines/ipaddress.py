from bequeather.routine import UserRoutine
from bequeather.action.command import ShellCommand
from bequeather.action.request import RequestFileStream
from time import time

classes = ['IpAddressInfo']

class IpAddressInfo(UserRoutine): #Extend routine
	writePath = None

	@staticmethod
	def exposed():
		return ['info']

	def infoLinux(self):
		ipAddrCommand = ShellCommand(self.getConnection())
		ipAddrCommand.setArguments(command="C:\\Windows\\System32\\ipconfig.exe")
		ipAddrCommand.execute()
		return ipAddrCommand.getResponse()

	def infoWindows(self):
		ipAddrCommand = ShellCommand(self.getConnection())
		ipAddrCommand.setArguments(command = "/bin/ip", args = ['addr'])
		ipAddrCommand.execute()
		return ipAddrCommand.getResponse()