
#consider lists of requirements
#consider list of objects in each category
def GrasshopperInputsGate(inp, str_TypName):
	if inp is not None:
		if inp.__class__.__name__ == str_TypName:
			return True
	return False

def IsCompasDataStructure(inp, strsL_AddtlTypsNms=None):
	strsL_DfltTypsNms = ['FormDiagram','ForceDiagram','Network','Mesh']
	if strsL_AddtlTypsNms is not None and isinstance(strsL_AddtlTypsNms,list):
		strsL_DfltTypsNms.extend(strsL_AddtlTypsNms)
	_bool_IsCpDtaStruct = False
	for _str_TypNm in strsL_DfltTypsNms:
		_bool_IsCpDtaStruct = _bool_IsCpDtaStruct or _str_TypNm == inp.__class__.__name__
		if _bool_IsCpDtaStruct==True:
			break
	return _bool_IsCpDtaStruct



def SetDefaultInput (dta_Inp, dta_DfltVal, bool_LstOtp = False):
	_dta_Inp = dta_Inp
	if _dta_Inp is None:
		_dta_Inp = dta_DfltVal
	elif (isinstance(_dta_Inp, list)==True and len(_dta_Inp)<1):
		_dta_Inp = dta_DfltVal

	if bool_LstOtp:
		_dta_Inp = [_dta_Inp] if isinstance(_dta_Inp, list) == False else _dta_Inp
	return _dta_Inp


def MatchListsLengths (dtaL_Base, dtaL_ToMatch):
	_dtaL_Patn = dtaL_ToMatch

	_len_Base = len(dtaL_Base)
	_len_Patn = len(_dtaL_Patn)

	if (_len_Base > _len_Patn):
		_dtaL_Matched = []
		for _i in range (0, _len_Base):
			_iPatn = _i % _len_Patn
			_dtaL_Matched.append(_dtaL_Patn[_iPatn])
	elif (_len_Base <= _len_Patn):
		_dtaL_Matched = _dtaL_Patn[0:_len_Base]
	return _dtaL_Matched;

# aL = [1,2,3,4,5,5,6,7,8]
# bL = [2,2,1,4]
# bL2 = MatchListsLengths(bL, aL)
# print (bL2)
# inp = []
# res = GrasshopperInputsGate(inp, 'list')
# print (res)