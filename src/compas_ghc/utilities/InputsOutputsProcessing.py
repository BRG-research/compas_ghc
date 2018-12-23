
def GrasshopperInputsGate(inp, str_TypName):
	if inp is not None:
		if inp.__class__.__name__ == str_TypName:
			return True
	return False

def SetDefaultInput (dta_Inp, dta_DfltVal):
	_dta_Inp = dta_Inp
	if _dta_Inp is None:
		_dta_Inp = dta_DfltVal
	return _dta_Inp



# inp = []
# res = GrasshopperInputsGate(inp, 'list')
# print (res)