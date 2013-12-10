#! /usr/bin/python

from sgui_utils import *
from widget import Widget
from sgui_event import EventHook

class CheckBox(Widget):
	
	def __init__(self):
		Widget.__init__(self)
		self._checked = False
		
	def setChecked(self, checked):
		if checked is bool:
			self._checked = checked
		
	def render(self):
		Widget.render(self)
		renderCommands = []
		visibleTextLength = self._width - 2
		if self._checked:
			checkedSymbol = Symbols.CHECKBOX_CHECKED
		else:
			checkedSymbol = Symbols.CHECKBOX_UNCHECKED
		if visibleTextLength > 0:
			renderCommands.append(Utils.getMoveCursorCode(self._y, self._x))
			renderCommands.append(self._backColor + self._foreColor)
			renderCommands.append(checkedSymbol + ' ' + self._text[:visibleTextLength])
		Utils.render(renderCommands)
		
	def click(self):
		self.check()
		Widget.click(self)
		self.render()
		
	def check(self):
		if self._checked:
			self._checked = False
		else:
			self._checked = True