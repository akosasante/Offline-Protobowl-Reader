import PyQt4
from enaml.widgets.api import Window, Container, Label


enamldef Main(Window):
	attr message = "Hello, world!"
	Container:
		Label:
			text = message