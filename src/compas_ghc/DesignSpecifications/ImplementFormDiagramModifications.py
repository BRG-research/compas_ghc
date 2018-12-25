from compas_ghc.utilities.InputsOutputsProcessing import MatchListsLengths as MatchLstLgths

def ImplementElementsModifications (formDiag, instsElemsAttrsModL):

	_instsElemsAttrsModL = instsElemsAttrsModL
	_formDiag = formDiag
	for _instsElemsAttrsMod in _instsElemsAttrsModL:
		_char_ElemsTyp = _instsElemsAttrsMod.char_ElemsTyp

		if _char_ElemsTyp == 'v':
			_keysL_AllDiagElems = _cDctDiagElems.keys()
		elif _char_ElemsTyp == 'e':
			_keysL_AllDiagElems = _formDiag.edges(False)

		_keysL_ElemsToMod 		= _instsElemsAttrsMod.keysL_Elems

		if len(_keysL_ElemsToMod) == 0:
			_keysL_ElemsToMod	= _keysL_AllDiagElems.keys()

		_dtaL_AttrVals 	= _instsElemsAttrsMod.dtaL_AttrVals 
		_dtaL_AttrVals 	= MatchLstLgths(_keysL_ElemsToMod, dtaL_AttrVals)
		_str_AttrNm 	= _instsElemsAttrsMod.str_AttrNm

		for __key, __attr in zip(_keysL_ElemsToMod, _dtaL_AttrVals):
			if _char_ElemsTyp == 'v':
				_formDiag.set_vertex_attribute(__key, _str_AttrNm, __attr)
			elif _char_ElemsTyp == 'e':
				_formDiag.set_edge_attribute(__key, _str_AttrNm, __attr)




