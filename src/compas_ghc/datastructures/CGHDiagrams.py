from compas_tna.diagrams                            import Diagram
from compas_tna.diagrams                            import FormDiagram
from compas_tna.diagrams                            import ForceDiagram
from compas_ghc.DataStructures.CGHDataTypesBase     import CGHDataTypesBase

class CGHDiagram(CGHDataTypesBase, Diagram):
    def __init__ (self):
        Diagram.__init__(self)
        # super(CGHDiagram, self).__init__()

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Nodes'    : len(self.vertex),
                            '# of Members'  : len(self.edgedata),
                            '# of Spaces'   : len(self.face),
                        }
        return _dct_SmryDta

    def ToString(self):
        return self._ToString()



class CGHFormDiagram(CGHDataTypesBase, FormDiagram):
    def __init__ (self):
        FormDiagram.__init__(self)  

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Nodes'    : len(self.vertex),
                            '# of Members'  : len(self.edgedata),
                            '# of Spaces'   : len(self.face),
                        }

        return _dct_SmryDta

    def ToString(self):
        return self._ToString()

class CGHForceDiagram(CGHDataTypesBase,ForceDiagram):
    def __init__ (self):
        ForceDiagram.__init__(self)  

    # @classmethod
    # def from_formdiagram(cls, formdiagram):
    #     return formdiagram.dual(cls)

    def ToString(self):
        return self._ToString()

if __name__ == '__main__':
    _diag = CGHForceDiagram()
    print (_diag)
