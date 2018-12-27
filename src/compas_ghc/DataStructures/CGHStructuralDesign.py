__all__ = [
    'StructuralDesign',
    'StructuralLoads',
]


class CGHStructuralDesign:
	def __init__(self):
		self.formDiag 		= None
		self.forceDiag 	 	= None

	def SetFormDiagram(self, formDiag):
		self.formDiag 		= formDiag

	def SetForceDiagram(self, forceDiag):
		self.forceDiag 		= forceDiag
	
	def SetDualDiagrams(self, formDiag, forceDiag):
		self.SetFormDiagram(formDiag)
		self.SetForceDiagram(forceDiag)

	def OutputDualDiagrams(self):
		return self.formDiag, self.forceDiag;

