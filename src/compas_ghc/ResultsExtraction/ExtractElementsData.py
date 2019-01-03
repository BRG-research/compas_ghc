import collections
try:
    from Grasshopper import DataTree
    from Grasshopper.Kernel.Data import GH_Path
except:
    pass


def ExtractElementsData (cDtaStruct, char_ElemTyp, str_FltrByAttrName = None):
	_str_FltrByAttrName = list(str_FltrByAttrName) if str_FltrByAttrName is not None and isinstance(str_FltrByAttrName,list) else str_FltrByAttrName
	if char_ElemTyp == 'v': #node
		_elemDta 			= cDtaStruct.RetrieveVertexData(bool_ExclExt=True)
		_str_KeyName 		= 'vKey'
	elif char_ElemTyp == 'e': #edge
		_elemDta 			= cDtaStruct.RetrieveEdgeData(bool_ExclExt=True)
		_str_KeyName 		= 'eKeyUV'
	elif char_ElemTyp == 'f': #space
		_elemDta 			= cDtaStruct.RetrieveFaceData(bool_ExclExt=True)
		_str_KeyName 		= 'fKey'

	_GHDtaTr_Lgds, _GHDtaTr_Vals = DataTree[object](), DataTree[object]()
	_GHPath = GH_Path(0)

	_i = 0
	for _ind, _dta in _elemDta.items():
		_GHPath = GH_Path(int(_i))
		_GHDtaTr_Lgds.Add(_str_KeyName, _GHPath)
		_GHDtaTr_Vals.Add(_ind,_GHPath)
		for _dtaKey, _dtaVal in _dta.items():
			_bool_StoDta = False if _str_FltrByAttrName is not None and _dtaKey not in _str_FltrByAttrName else True
			if _bool_StoDta:
				_GHDtaTr_Lgds.Add(str(_dtaKey),_GHPath)
				_GHDtaTr_Vals.Add(_dtaVal,_GHPath)
		_i += 1

	return _GHDtaTr_Lgds, _GHDtaTr_Vals;