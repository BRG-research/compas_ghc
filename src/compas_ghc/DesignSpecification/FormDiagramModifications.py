from compas_ghc.Utilities.InputsOutputsProcessing import MatchListsLengths as MatchLstLgths

def ImplementElementsModifications (formDiag, instsElemsAttrsModL):

	_instsElemsAttrsModL = instsElemsAttrsModL
	_formDiag = formDiag
	for _instsElemsAttrsMod in _instsElemsAttrsModL:
		_char_ElemsTyp = _instsElemsAttrsMod.char_ElemsTyp

		_keysL_ElemsToMod 		= _instsElemsAttrsMod.keysL_Elems

		if len(_keysL_ElemsToMod) == 0:
			if _char_ElemsTyp == 'v':
				_keysL_AllDiagElems 	= _formDiag.VertexKeys()
				# _dctMap__VInd_to_VKey 	= _formDiag.IndexToVKey()
			elif _char_ElemsTyp == 'e':
				_keysL_AllDiagElems 	= _formDiag.EdgeKeys()
				# _dctMap__VInd_to_VKey 	= _formDiag.EIndKeysToEKeys()
			_keysL_ElemsToMod	= _keysL_AllDiagElems

		_dta_AttrVal 	= [_instsElemsAttrsMod.dta_AttrVal] 
		_dta_AttrVal 	= MatchLstLgths(_keysL_ElemsToMod, _dta_AttrVal)
		_str_AttrNm 	= _instsElemsAttrsMod.str_AttrNm

		for __key, __attr in zip(_keysL_ElemsToMod, _dta_AttrVal):
			if _char_ElemsTyp == 'v':
				_formDiag.set_vertex_attribute(__key, _str_AttrNm, __attr)
			elif _char_ElemsTyp == 'e':
				_formDiag.set_edge_attribute(__key, _str_AttrNm, __attr)




