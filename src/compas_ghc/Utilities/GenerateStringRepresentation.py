from textwrap import TextWrapper as TxtWrpr 

str_Dflt_CmpyNm = 'BRG'
str_Dflt_ProdNm = 'CompasGH'
str_Dflt_TitPfx = str_Dflt_ProdNm 

def GenerateStringRepresentation(CGHObj, dct_AddtlInfo = None, str_TitPfx = str_Dflt_TitPfx):
	def _DisplayAttribute (nm, val):
		_nSpc_1 = 2
		_nSpc_2 = 40
		_str_AttrDisp 		= ' '*_nSpc_1 #len(str(nm))
		if isinstance(_val, float):
			_str_AttrDisp 	+= '{_nm} : {_val:.3f}'.format(_nm=_nm, _val=_val) #rounding
		elif isinstance (_val, int):
			_str_AttrDisp 	+= '{_nm} : {_val:d}'.format(_nm=_nm, _val=_val)
		elif isinstance (_val, str):
			_str_AttrDisp 	+= '{_nm} : {_val}'.format(_nm=_nm, _val=_val) 
		return _str_AttrDisp;


	if isinstance(CGHObj, str):
		_str_ClsNm 			=  CGHObj
	else:
		_str_ClsNm 			= CGHObj.__class__.__name__

	_str_Tit 		= '[[ ' + str_TitPfx + " :: " + _str_ClsNm + ' ]]'

	_str_AttrsDisp	= ''
	if dct_AddtlInfo is not None:
		for _nm, _val in dct_AddtlInfo.items():
			_str_AttrsDisp += '\n'

			# _str_Indt_1		= ' '*_nSpc_1
			# _txtWrpr_1		= TxtWrpr(  initial_indent = _str_Indt_1,
			# 							width = 70,
			# 							subsequent_indent = _str_Indt_1)
			# _txt_Nm			= _txtWrpr_1.fill(_nm)

			# _str_Indt_2A	= _txt_Nm + ' '*(_nSpc_2 - len(_txt_Nm))
			# _str_Indt_2B	= ' '*_nSpc_2
			# _txtWrpr_2		= TxtWrpr(  initial_indent = _str_Indt_2A,
			# 							width = 70,
			# 							subsequent_indent = _str_Indt_2B)
			# _txt_EntrAttr	= _txtWrpr_2.fill(_val)

			_str_AttrsDisp += _DisplayAttribute(_nm, _val)
	
	_str_Otp		= _str_Tit + _str_AttrsDisp
	return _str_Otp;

if __name__ == "__main__":
	class testDataStructureWithLongFancyName ():
		def __init__(self):
			pass

	testObj = testDataStructureWithLongFancyName()
	testAttrs = {'a': int(123), 'b':'hello'}

	print (GenerateStringRepresentation(testObj, testAttrs))

