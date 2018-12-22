
def GrasshopperInputsGate(inp, str_TypName):
	if inp is not None:
		if type(inp).__name__ == str_TypName:
			return True
	return False


inp = []
res = GrasshopperInputsGate(inp, 'list')
print (res)