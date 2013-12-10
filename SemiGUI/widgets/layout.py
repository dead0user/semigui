#! /usr/bin/python

from sgui_utils import *
from widget import Widget
from sgui_event import EventHook

class Layout(Widget):

	def __init__(self):
		Widget.__init__(self)
		self._components = []
		self._spacing = 0
		
	def getComponents(self):
		return self._components
	
	def addWidget(self, widget):
		self.setContext(self)
		self._components.append(widget)
	
	def removeWidget(self, widget):
		self._components.remove(widget)
		
	def removeAllWidgets(self):
		self._components = []
		
	def setSpacing(self, spacing):
		if spacing >= 0:
			self._spacing = spacing

	def getSpacing(self):
		return self._spacing

	def keyPress(self, code):
		components_count = len(self._components)
		for i in range(components_count):
			if self._components[i].getFocused():
				self._components[i].keyPress(code)

	def click(self):
		components_count = len(self._components)
		for i in range(components_count):
			if self._components[i].getFocused():
				self._components[i].click()
				break

	def focus(self):
		components_count = len(self._components)
		for i in range(components_count):
			if self._components[i].getFocused():
				self._components[i].setFocused(False)
				self._components[i].render()
				if components_count > i + 1:
					self._components[i + 1].setFocused(True)
					self._components[i + 1].render()
				else:
					self._components[0].setFocused(True)
					self._components[0].render()
				break
		

class LinearLayout(Layout):
	
	VERTICAL = 0
	HORIZONTAL = 1
	
	def __init__(self):
		Layout.__init__(self)
		self._orientation = LinearLayout.VERTICAL
		
	def render(self):
		if self._orientation == LinearLayout.VERTICAL:
			self.renderVertically()
		else:
			self.renderHorizontally()
		
	def renderVertically(self):
		components_count = len(self._components)
		current_component_bottom = self._y
		for i in range(components_count):
			# set proper size (less than container) and position (one after another)
			component_width = self._components[i].getWidth()
			if component_width >= self._width:
				self._components[i].setWidth(self._width)
			self._components[i].setY(current_component_bottom)
			self._components[i].setX(self._x)
			current_component_bottom += self._components[i].getHeight() + self._spacing
			# finally render component
			self._components[i].render()
		Utils.clearStyles()
		
	def renderHorizontally(self):
		pass