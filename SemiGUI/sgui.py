#! /usr/bin/python


"""
	Semi-graphical User Interface
"""


from threading import Thread
from sgui_input import *
from sgui_output import *
from sgui_utils import *
from sgui_event import EventHook
from widgets import *
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class SemiGUI(object):

	def __init__(self):
		self._width = 0
		self._height = 0
		self._layout = None
		self._keyBindings = {}
		self.onExit = EventHook()
		self.sguiOutput = SemiGUIOutput(self)
		self.sguiInput = SemiGUIInput(self)
		
	def init(self):
		self.bindKeys()
		self.sguiOutput.start()
		self.sguiInput.start()
		
	def setWidth(self, width):
		self._width = width
		
	def getWidth(self):
		return self._width

	def setHeight(self, height):
		self._height = height
		
	def getHeight(self):
		return self._height
			
	def setLayout(self, layout):
		self._layout = layout
		self._layout.setContext(self)
		#self.draw()

	def getLayout(self):
		return self._layout

	def changeFocus(self):
		self._layout.focus()

	def click(self):
		self._layout.click()
				
	def keyPress(self, code):
		if code in self._keyBindings:
			self._keyBindings.get(code)()
		else:
			self._layout.keyPress(code)
			
	def bindKeys(self):
		self._keyBindings = {
			Keys.ENTER: self.click,
			Keys.TAB: self.changeFocus,
			Keys.UP: self.changeFocus,
			Keys.DOWN: self.changeFocus,
			Keys.CTRLC: self.exit
		}

	def draw(self):
		sys.stdout.write(Back.BLACK)
		for i in range(self._height):
			sys.stdout.write(' ' * self._width)
		self._layout.render()
	
	"""
	def setLayout(self, layout):
		import xml.etree.ElementTree as ET
		# TODO handle exceptions
		if os.path.exists(layout):
			tree = ET.parse(layout)
			root = tree.getroot()
		else:
			root = ET.fromstring(layout)
		# iterate through the tree of widgets
		self.parseLayout(root)

	def parseLayout(self, layout):
		try:
			widget = globals()[layout.tag]()
			for widgetAttr in layout.attrib:
				print widgetAttr
		except KeyError:
			# Add some info to debug channel
			pass
		for widgetXml in layout:
			#print widget.tag, widget.attrib
			if issubclass(eval(widgetXml.tag), Layout):
				self.parseLayout(widgetXml)
			if issubclass(eval(widgetXml.tag), Widget):
				widget = eval(widgetXml.tag)()
				print widget
	"""
			
	def exit(self):
		self.sguiOutput.running = False
		self.sguiInput.running = False
		self.onExit.fire()