import collections
try:
    from Grasshopper import DataTree
    from Grasshopper.Kernel.Data import GH_Path
except:
    pass

def ExtractElementsData (cDtaStruct, char_ElemTyp, str_FltrByAttrName = None):
	_str_FltrByAttrName = list(str_FltrByAttrName) if str_FltrByAttrName is not None and isinstance(str_FltrByAttrName,list) else str_FltrByAttrName
	if char_ElemTyp == 'v': #node
		_elemDta 			= cDtaStruct.vertex
		_dctMap__Key_to_Ind = cDtaStruct.key_index()
		_str_KeyName 		= 'vKey'
	elif char_ElemTyp == 'e': #edge
		_elemDta 			= cDtaStruct.edgedata
		_dctMap__Key_to_Ind = cDtaStruct.uv_index()
		_str_KeyName 		= 'eKeyUV'
	elif char_ElemTyp == 'f': #space
		_elemDta 			= cDtaStruct.facedata
		_dctMap__Key_to_Ind = {_fK: _i for _i, _fK in enumerate(_elemDta.keys())}
		_str_KeyName 		= 'fKey'

	_elemDta = {_dctMap__Key_to_Ind[_key]: _dta.update({_str_KeyName: _key}) for _key, _dta in _elemDta.items()}

	_GHDtaTr_Lgds, _GHDtaTr_Vals = DataTree[object](), DataTree[object]()
	_GHPath = GH_Path(0)

	for _key, _dta in _elemDta.items():
		_GHPath = GH_Path(int(_key))
		for _dtaKey, _dtaVal in _dta.items():
			_bool_StoDta = False if str_AttrName is not None and _dtaKey not in _str_FltrByAttrName else True
			if _bool_StoDta:
				_GHDtaTr_Lgds.Add(str(_dtaKey),_GHPath)
				_GHDtaTr_Vals.Add(_dtaVal,_GHPath)

	return _GHDtaTr_Lgds, _GHDtaTr_Vals;