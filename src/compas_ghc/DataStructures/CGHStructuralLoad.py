__all__ = [
    'StructuralDesign',
    'StructuralLoads',
]


class CGHStructuralLoad:
	def __init__(self, coords_LdPos = None, vec_LdDirMag=None):
		self.coords			= coords_LdPos
		# self.i_LdPosFDiagVKey	= None
		self.vec 			= vec_LdDirMag