from compas_ghc.DataStructures.CGHDataTypesBase     import CGHTypesBase

__all__ = [
    'StructuralLoads',
]

class CGHStructuralLoad(CGHTypesBase):
    def __init__(self, coords_LdPos = None, vec_LdDirMag=None):
        self.coords         = coords_LdPos
        # self.i_LdPosFDiagVKey = None
        self.vec            = vec_LdDirMag

    def ToString(self):
        return self._ToString()