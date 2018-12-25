
from compas_tna.diagrams import Diagram
from compas_tna.diagrams import FormDiagram

class CGHDiagram(Diagram):
	def __init__ (self):
		super(CGHDiagram, self).__init__()

class CGHFormDiagram(FormDiagram):
	def __init__ (self):
		super(CGHFormDiagram, self).__init__()	

	def __repr__(self):
		return ('<CompasGH: FormDiagram>')