from copy import deepcopy

def RPCDummyFunction (dta):
	_dta = deepcopy(dta)
	_dta.update({100:100})
	return _dta;
	