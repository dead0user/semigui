#! /usr/bin/python
	
def onSemiGuiExit():
	Utils.clear()
	print "Terminating SemiGUI application..."
	sys.exit()

if __name__ == "__main__":
	from sgui import *
	from widgets import *
	from sgui_utils import *
	
	# uncomment the line below for remote debugging
	#import pydevd;pydevd.settrace()
	
	semigui = SemiGUI()
	
	label1 = Label()
	label1.setSize(1, 200)
	label1.setPosition(10, 10)
	label1.setFocused(True)
	label1.setBorder(Border.INVISIBLE)
	label1.setText('Label1')
	

	radiobutton1 = RadioButton()
	radiobutton1.setSize(5, 200)
	radiobutton1.setPosition(15, 85)
	radiobutton1.setText('RadioButton1')
	radiobutton1.setBorder(Border.THIN)
	
	
	checkbox1 = CheckBox()
	checkbox1.setSize(1, 200)
	checkbox1.setPosition(3, 20)
	checkbox1.setText('LongNamedcheckbox1')
	checkbox1.setBorder(Border.THIN)
	
	
	editBox1 = EditBox()
	editBox1.setSize(1, 200)
	editBox1.setPosition(8, 20)
	editBox1.setText('edit me!')
	editBox1.setBorder(Border.THIN)
	
	
	linearLayout1 = LinearLayout()
	linearLayout1.setSize(30, 80)
	linearLayout1.setPosition(2, 10)
	linearLayout1.setSpacing(1)
	linearLayout1.addWidget(label1)
	linearLayout1.addWidget(radiobutton1)
	linearLayout1.addWidget(checkbox1)
	linearLayout1.addWidget(editBox1)
	
	
	semigui.setLayout(linearLayout1)
	
	semigui.onExit += onSemiGuiExit

	semigui.init()