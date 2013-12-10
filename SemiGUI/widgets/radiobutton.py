#! /usr/bin/python

from sgui_utils import *
from widget import Widget
from sgui_event import EventHook

class RadioButton(Widget):
	
	def __init__(self):
		Widget.__init__(self)
		self._selected = False
		
	def render(self):
		Widget.render(self)
		renderCommands = []
		if self._selected:
			selectedSymbol = Symbols.RADIOBUTTON_SELECTED
		else:
			selectedSymbol = Symbols.RADIOBUTTON_UNSELECTED
		#if visibleTextLength > 0:
		renderCommands.append(Utils.getMoveCursorCode(self._y, self._x))
		renderCommands.append(self._backColor + self._foreColor)
		renderCommands.append(selectedSymbol + ' ' + self._text[:self._width])
		Utils.render(renderCommands)
		
	def click(self):
		self.select()
		Widget.click(self)
		self.render()

	def select(self):
		if self._selected:
			self._selected = False
		else:
			self._selected = True
