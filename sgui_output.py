#! /usr/bin/python

from threading import Thread
from sgui_utils import *

class SemiGUIOutput(Thread):

	def __init__(self, context):
		Thread.__init__(self)
		self.running = True
		self.context = context

	def run(self):
		currentConsoleSize = ''
		while self.running:
			consoleSize = Utils.getUnparsedSize()
			if consoleSize != currentConsoleSize and consoleSize != '':
				Utils.clear()
				size = consoleSize.split()
				self.context.setHeight(int(size[0]))
				self.context.setWidth(int(size[1]))
				self.context.draw()
				currentConsoleSize = consoleSize