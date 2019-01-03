
class AttributesSetters:
	def SetVerticesAttributeWithValues (self, str_AttrNm, dtaL_AttrVals, vKeysL):
		for _dta, _vKey in zip(dtaL_AttrVals, vKeysL):
			self.set_vertex_attribute(name=str_AttrNm, value=_dta, key=_vKey)

	def SetEdgesAttributeWithValues (self, str_AttrNm, dtaL_AttrVals, eKeysL):
		for _dta, _eKey in zip(dtaL_AttrVals, eKeysL):
			self.set_edge_attribute(name=str_AttrNm, value=_dta, key=_eKey)

