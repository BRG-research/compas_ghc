from compas_ghc.Utilities.GenerateStringRepresentation import GenerateStringRepresentation as GnrStrRepr

class CGHTypesBase():
    def __init__ (self):
        pass

    def CompileToStringSummary(self):
        return None
    def __str__(self):
        return GnrStrRepr(self, self.CompileToStringSummary())
    def __repr__(self):
        return GnrStrRepr(self, self.CompileToStringSummary())
    def ToString (self):
        return GnrStrRepr(self, self.CompileToStringSummary())
    def _ToString (self):
        return GnrStrRepr(self, self.CompileToStringSummary())

class CGHDataStructuresBase(CGHTypesBase):
    def __init__ (self):
        pass

    def CustomAttributesData(self):
        dct_AddtlDta = {}
        return dct_AddtlDta

    def CreateDuplicate(self):
        from copy import deepcopy
        _dtaStruct_Dup      = self.__class__.from_data(deepcopy(self.to_data()))
        _cstmAttrDta_Dup    = deepcopy(self.CustomAttributesData())
        for _attrNm, _attrVal in _cstmAttrDta_Dup.items():
            setattr(_dtaStruct_Dup, _attrNm, _attrVal)

        return _dtaStruct_Dup;
