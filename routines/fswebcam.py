from bequeather.routine import UserRoutine
from bequeather.action.command import ShellCommand
from bequeather.action.request import RequestFileStream
from time import time

classes = ['FsWebCam']

class FsWebCam(UserRoutine): #Extend routine
	writePath = None

	@staticmethod
	def exposed():
		return ['imageFileTransfer']

	def tempImageFilename(self):
		return '{tmpDir}fswebcam-%s.jpg' % (str(time()))
	
	def image(self):
		captureImageCommand = ShellCommand(self.getConnection())

		tmpFile = self.tempImageFilename()

		captureImageCommand.setArguments(command = '/usr/bin/fswebcam', args = [tmpFile])
		captureImageCommand.execute()

		return {**captureImageCommand.getResponse()} + {"file": tmpFile}

	def fetchFile(self, targetFile):
		stream = RequestFileStream(self.getConnection)
		stream.setArguments(targetFile = targetFile)
		stream.execute()

		return stream.getResponse()

	def imageFileTransfer(self):
		image = self.image()
		transfer = self.fetchFile(image.get('file'))
		
		return transfer