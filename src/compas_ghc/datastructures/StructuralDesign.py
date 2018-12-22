__all__ = [
    'StructuralDesign'
]

class StructuralDesign:
	def __init__(self):
		self.formDiag 		= None
		self.forceDiag 	 	= None

	def SetFormDiagram(self, formDiag):
		self.formDiag 		= formDiag

	def SetForceDiagram(self, forceDiag):
		self.forceDiag 		= forceDiag
	