from compas_ghc.DataStructures.CGHDataTypesBase     import CGHTypesBase

__all__ = [
    'StructuralDesign',
]


class CGHStructuralDesign(CGHTypesBase):
    def __init__(self):
        self.formDiag       = None
        self.forceDiag      = None
        self.vec_GblArLd      = [0,0,0]

    def AddGlobalLoad (self, vec_GblLdToAdd):
        self.vec_GblArLd = [_cnptSelf + _cnptInp for _cnptSelf, _cnptInp in zip(self.vec_GblArLd, vec_GblLdToAdd)]

    def SetFormDiagram(self, formDiag):
        self.formDiag       = formDiag
        if hasattr(self.formDiag, 'vec_GblArLd'):
            self.vec_GblArLd = self.formDiag.vec_GblArLd

    def SetForceDiagram(self, forceDiag):
        self.forceDiag      = forceDiag
    
    def SetDualDiagrams(self, formDiag, forceDiag):
        self.SetFormDiagram(formDiag)
        self.SetForceDiagram(forceDiag)


    def OutputDualDiagrams(self):
        return self.formDiag, self.forceDiag;

    def CreateDuplicate(self):
        from copy import deepcopy 
        _formDiag_Dup   = self.formDiag.CreateDuplicate()   if self.formDiag is not None else None
        _forceDiag_Dup  = self.forceDiag.CreateDuplicate()  if self.forceDiag is not None else None
        _structDsg_Dup  = self.__class__()
        _structDsg_Dup.SetDualDiagrams(_formDiag_Dup, _forceDiag_Dup)
        _structDsg_Dup.AddGlobalLoad(self.vec_GblArLd)
        return _structDsg_Dup

    def ToString(self):
        return self._ToString()

if __name__ == '__main__':
    # _diag = CGHStructuralDesign().CreateDuplicate()
    # print (_diag)
    pass