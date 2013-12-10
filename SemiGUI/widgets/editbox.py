#! /usr/bin/python

from sgui_utils import *
from widget import Widget
from sgui_event import EventHook

class EditBox(Widget):
	
	def __init__(self):
		Widget.__init__(self)
		self.onChangeText = EventHook()
		self._cursorColor = Fore.GREEN
		
	def setCursorColor(self, cursorColor):
		self._cursorColor = cursorColor
	
	def getCursorColor(self):
		return self.cursorColor
		
	def render(self):
		Widget.render(self)
		renderCommands = []
		text_length = len(self._text)
		visibleTextLength = self._width - 1
		if visibleTextLength > 0:
			renderCommands.append(Utils.getMoveCursorCode(self._y, self._x))
			renderCommands.append(self._backColor + self._foreColor)
			if self._focused:
				cursor = self._cursorColor + Symbols.CURSOR
			else:
				cursor = self._cursorColor + ''
			if text_length - visibleTextLength > 0:
				renderCommands.append(self._text[text_length - visibleTextLength:] + cursor)
			else:
				renderCommands.append(self._text + cursor)
		Utils.render(renderCommands)
		
	def keyPress(self, code):
		if code == Keys.UP:
			#self._text = 'You pressed UP key'
			print 'You pressed UP key'
			return None
		if code == Keys.BACKSPACE:
			self._text = self._text[:-1]
		else:
			self._text += unichr(code)
		self.render()
		Widget.keyPress(self, code)