#! /usr/bin/python

import os, sys

class Utils(object):
	NewLine = '\n'
	#CtrlZ = '\032'
	ESC = '\033['
	EscPattern = '\033\[[0-9]{1,2}m'
	CLEAR = 'clear'

	@staticmethod
	def getMoveCursorCode(y, x):
		return Utils.ESC + str(y) + ';' + str(x) + 'H'
		
	@staticmethod
	def moveCursor(y, x):
		sys.stdout.write(Utils.ESC + str(y) + ';' + str(x) + 'H')

	@staticmethod
	def clear():
		os.system(Utils.CLEAR)
		
	@staticmethod
	def clearStyles():
		sys.stdout.write(Style.NORMAL)
		sys.stdout.flush()

	@staticmethod
	def getUnparsedSize():
		return os.popen('stty size', 'r').read()

	@staticmethod
	def render(renderCommands):
		for i in range(len(renderCommands)):
			sys.stdout.write(renderCommands[i])
		Utils.clearStyles()



class Keys:
	BACKSPACE = 127
	TAB = 9
	SPACE = 32
	ENTER = 13
	CTRLZ = 26
	CTRLC = 3
	
	LEFT = 68
	UP = 65
	RIGHT = 67
	DOWN = 66
	
	
class Symbols:
	CHECKBOX_CHECKED = unichr(9747) #9745 u"\u2611" 
	CHECKBOX_UNCHECKED = unichr(9744)
	
	RADIOBUTTON_SELECTED = unichr(9679)
	RADIOBUTTON_UNSELECTED = unichr(9675)
	
	CURSOR = unichr(9608)
	
	
class Margin:
	
	def __init__(self):
		self.top = 0
		self.right = 0
		self.bottom = 0
		self.left = 0


class Border:
	NOBORDER = None
	
	INVISIBLE = {'LEFT_TOP' : ' ',
				'HORIZONTAL' : ' ',
				'CENTER_TOP' : ' ',
				'RIGHT_TOP' : ' ',
				'VERTICAL' : ' ',
				'LEFT_CENTER' : ' ',
				'CENTER' : ' ',
				'RIGHT_CENTER' : ' ',
				'LEFT_BOTTOM' : ' ',
				'CENTER_BOTTOM' : ' ',
				'RIGHT_BOTTOM' : ' '}
	
	THIN = {'LEFT_TOP' : unichr(9484),
			'HORIZONTAL' : unichr(9472),
			'CENTER_TOP' : unichr(9516),
			'RIGHT_TOP' : unichr(9488),
			'VERTICAL' : unichr(9474),
			'LEFT_CENTER' : unichr(9500),
			'CENTER' : unichr(9532),
			'RIGHT_CENTER' : unichr(9508),
			'LEFT_BOTTOM' : unichr(9492),
			'CENTER_BOTTOM' : unichr(9524),
			'RIGHT_BOTTOM' : unichr(9496)}
	#THICK = 3
	#DOUBLE = 4


class Align:
	CENTER = [0, 0]
	LEFT = [0, -1]
	RIGHT = [0, 1]
	TOP = [-1, 0]
	BOTTOM = [1, 0]
	TOP_LEFT = [-1, -1]
	TOP_RIGHT = [-1, 1]
	BOTTOM_LEFT = [1, -1]
	BOTTOM_RIGHT = [1, 1]



class Fore:
	BLACK = Utils.ESC + '30m'
	RED = Utils.ESC + '31m'
	GREEN = Utils.ESC + '32m'
	YELLOW = Utils.ESC + '33m'
	BLUE = Utils.ESC + '34m'
	MAGENTA = Utils.ESC + '35m'
	CYAN = Utils.ESC + '36m'
	WHITE = Utils.ESC + '37m'
	DEFAULT = Utils.ESC + '39m'


class Back:
	BLACK = Utils.ESC + '40m'
	RED = Utils.ESC + '41m'
	GREEN = Utils.ESC + '42m'
	YELLOW = Utils.ESC + '43m'
	BLUE = Utils.ESC + '44m'
	MAGENTA = Utils.ESC + '45m'
	CYAN = Utils.ESC + '46m'
	WHITE = Utils.ESC + '47m'
	DEFAULT = Utils.ESC + '49m'


class Style:
	NORMAL = Utils.ESC + '00m'
	BOLD = Utils.ESC + '01m'
	FAINT = Utils.ESC + '02m'
	STANDOUT = Utils.ESC + '03m'
	UNDERLINE = Utils.ESC + '04m'
	BLINK = Utils.ESC + '05m'
	REVERSE = Utils.ESC + '07m'
	INVISIBLE = Utils.ESC + '08m'