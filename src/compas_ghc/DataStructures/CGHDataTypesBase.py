from compas_ghc.Utilities.GenerateStringRepresentation import GenerateStringRepresentation as GnrStrRepr

class CGHDataTypesBase():
	def __init__ (self):
		pass

	def CompileToStringSummary(self):
		return None

	def __str__(self):
		return GnrStrRepr(self, self.CompileToStringSummary())
	def __repr__(self):
		return GnrStrRepr(self, self.CompileToStringSummary())
	def ToString (self):
		return GnrStrRepr(self, self.CompileToStringSummary())
	def _ToString (self):
		return GnrStrRepr(self, self.CompileToStringSummary())
