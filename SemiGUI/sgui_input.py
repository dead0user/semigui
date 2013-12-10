#! /usr/bin/python

from threading import Thread
from sgui_utils import *
import sys, tty, termios

class SemiGUIInput(Thread):
	
	def __init__(self, context):
		Thread.__init__(self)
		self.running = True
		self.context = context

	def getChar(self):
		fd = sys.stdin.fileno()
		oldSettings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)
		return ch
		
	def run(self):
		Utils.moveCursor(0, 0)
		while self.running:
			char = self.getChar()
			code = ord(char)
			if char != '':
				self.context.keyPress(code)
				Utils.moveCursor(0, 0)