class ElementsAttributesModificationInstructions:
	def __init__ (self, char_ElemsTyp, str_AttrNm, dtaL_AttrVals, keysL_Elems = None):
		self.char_ElemsTyp 		= char_ElemsTyp
		self.str_AttrNm 		= str_AttrNm
		self.keysL_Elems		= []
		self.dtaL_AttrVals		= dtaL_AttrVals

		if len(keysL_Elems) > 0:
			if char_ElemsTyp=='e':
				#Convert string into tuple
				self.keysL_Elems = [tuple([int(_vKey) for _vKey in _strKey.strip('()').split(',')]) for _strKey in keysL_Elems]
			elif char_ElemsTyp=='v':
				self.keysL_Elems = [int(_vKey) for _vKey in keysL_Elems]

	def __repr__(self):
		return "elements modification instructions"