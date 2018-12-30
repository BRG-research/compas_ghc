from compas_ghc.DataStructures.CGHDataTypesBase     import CGHTypesBase

__all__ = [
    'StructuralLoads',
]

class CGHStructuralLoad(CGHTypesBase):
    def __init__(self, coords_LdPos = None, vec_LdDirMag=None):
        self.coords         = coords_LdPos
        # self.i_LdPosFDiagVKey = None
        self.vec            = vec_LdDirMag
        self.bool_GblLd		= True if self.coords is None else False

    def IsGlobalLoad(self):
    	return self.bool_GblLd;

    def CompileToStringSummary(self):
        _msg    = 'Local Point Load' if not self.IsGlobalLoad() else 'Global Area Load'
        _smry   = {'Type ': _msg}
        return _smry

    def ToString(self):
        return self._ToString();

