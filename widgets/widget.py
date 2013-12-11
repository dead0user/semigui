#! /usr/bin/python

from sgui_utils import *
from sgui_event import EventHook

class Widget(object):

	def __init__(self):
		
		# Fields
		self._context = None				# context of a widget (ideally layout or sgui class)
		self._text = ''						# text which may be printed on a widget (unnesessary to use)
		self._width = 0
		self._height = 0
		self._x = 0
		self._y = 0
		self._align = Align.LEFT			# align widget in container
		self._contentAlign = Align.TOP_LEFT	# align content in widget (do we really need it?)
		self._margin = Margin()
		self._visible = True				# is widget visible or not
		self._focused = False				# is widget focused or not
		self._border = Border.NOBORDER		# border style
		self._backColor = Back.BLUE			# background color
		self._foreColor = Fore.WHITE		# foreground color
		self._backAltColor = Back.CYAN		# alternate background color (when focused)
		self._foreAltColor = Fore.BLACK		# alternate foreground color (when focused)

		# Events
		self.onClick = EventHook()
		self.onFocus = EventHook()
		self.onFocusLost = EventHook()
		self.onKeyPress = EventHook()
		self.onResize = EventHook()
		self.onRender = EventHook()
	
	def setContext(self, context):
		self._context = context
		
	def getContext(self):
		return self._context
		
	def setText(self, text):
		self._text = text
		
	def getText(self):
		return self._text
		
	def setWidth(self, width):
		self._width = width
	
	def getWidth(self):
		return self._width
		
	def setHeight(self, height):
		self._height = height
	
	def getHeight(self):
		if self._border == Border.NOBORDER:
			return self._height
		else:
			return self._height + 2
		
	def setX(self, x):
		self._x = x
		
	def getX(self):
		return self._x

	def setY(self, y):
		self._y = y
		
	def getY(self):
		return self._y

	def setPosition(self, y, x):
		if x > 0 and y > 0:
			self._y = y
			self._x = x
			
	def setSize(self, height, width):
		if width >= 0 and height >= 0:
			self._width = width
			self._height = height
			self.render()
			self.onResize.fire()

	def setAlign(self, align):
		self._align = align
		
	def getAlign(self):
		return self._align
		
	def setMargin(self, top, right, bottom, left):
		if top < 0 and right < 0 and bottom < 0 and left < 0: return None
		self._margin.top = top
		self._margin.right = right
		self._margin.bottom = bottom
		self._margin.left = left
		
	def setVisible(self, visible):
		self._visible = visible
		
	def getVisible(self):
		return self._visible

	def setFocused(self, focused):
		if (self._focused == False and focused == True) or (self._focused == True and focused == False):
			self._focused = focused
			# replace back- and foreground colors by alternative ones
			tempBackColor = self._backColor
			self._backColor = self._backAltColor
			self._backAltColor = tempBackColor
			tempForeColor = self._foreColor
			self._foreColor = self._foreAltColor
			self._foreAltColor = tempForeColor
			self.onFocus.fire(self)
			self.render()
			
	def getFocused(self):
		return self._focused
			
	def setBorder(self, border):
		"""if self._border == Border.NOBORDER and border != Border.NOBORDER:
			self._width += 2
			self._height += 2
		elif self._border != Border.NOBORDER and border == Border.NOBORDER:
			self._width -= 2
			self._height -= 2"""
		self._border = border
		self.render()
		
	def getBorder(self):
		return self._border
		
	def setBackColor(self, backColor):
		self._backColor = backColor
		
	def getBackColor(self):
		return self._backColor
		
	def setForeColor(self, foreColor):
		self._foreColor = foreColor
		
	def getForeColor(self):
		return self._foreColor
		
	def setBackAltColor(self, backAltColor):
		self._backAltColor = backAltColor
		
	def getBackAltColor(self):
		return self._backAltColor
		
	def setForeAltColor(self, foreAltColor):
		self._foreAltColor = foreAltColor
		
	def getForeAltColor(self):
		return self._foreAltColor
		
	def click(self):
		self.onClick.fire(self)
		
	def keyPress(self, code):
		self.onKeyPress.fire(self, code)

	def render(self):
		renderCommands = []
		renderCommands.append(self._backColor + self._foreColor)
		if self._border == Border.NOBORDER:
			for i in range(self._height):
				renderCommands.append(Utils.getMoveCursorCode(self._y + i, self._x) + " " * self._width + Utils.NewLine)
		else:
			borderX = self._x - 1
			borderY = self._y - 1
			borderWidth = self._width + 2
			borderHeight = self._height + 2
			renderCommands.append(Utils.getMoveCursorCode(borderY, borderX) + self._border['LEFT_TOP'] + self._border['HORIZONTAL'] * (borderWidth - 2) + self._border['RIGHT_TOP'] + Utils.NewLine)
			for i in range(borderHeight - 2):
				renderCommands.append(Utils.getMoveCursorCode(borderY + i + 1, borderX) + self._border['VERTICAL'] + " " * (borderWidth - 2) + self._border['VERTICAL'] + Utils.NewLine)
			renderCommands.append(Utils.getMoveCursorCode(borderY + borderHeight - 1, borderX) + self._border['LEFT_BOTTOM'] + self._border['HORIZONTAL'] * (borderWidth - 2) + self._border['RIGHT_BOTTOM'])
		Utils.render(renderCommands)