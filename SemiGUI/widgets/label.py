#! /usr/bin/python

from sgui_utils import *
from widget import Widget
from sgui_event import EventHook

class Label(Widget):

	def __init__(self):
		Widget.__init__(self)

	def render(self):
		Widget.render(self)
		renderCommands = []
		visibleTextLength = self._width - 1
		if visibleTextLength > 0:
			renderCommands.append(Utils.getMoveCursorCode(self._y, self._x))
			renderCommands.append(self._backColor + self._foreColor)
			renderCommands.append(self._text[:visibleTextLength])
		Utils.render(renderCommands)