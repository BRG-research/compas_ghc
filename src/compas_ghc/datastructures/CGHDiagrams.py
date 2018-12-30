from compas_tna.diagrams                                                import Diagram
from compas_tna.diagrams                                                import FormDiagram
from compas_tna.diagrams                                                import ForceDiagram
from compas_ghc.DataStructures.CGHDataTypesBase                         import CGHDataStructuresBase
from compas_ghc.DataStructures.CommonMethods.ElementsMappings           import ElementsMappings

class CGHDiagram(   CGHDataStructuresBase,
                    ElementsMappings,
                    Diagram):

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



class CGHFormDiagram(   CGHDataStructuresBase, 
                        ElementsMappings,
                        FormDiagram):
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

class CGHForceDiagram(      CGHDataStructuresBase, 
                            ElementsMappings,
                            ForceDiagram):
    def __init__ (self):
        ForceDiagram.__init__(self)  

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Space Vertices'       : len(self.vertex),
                            '# of Members'              : len(self.edgedata),
                            '# of Node Faces'           : len(self.face),
                        }
        return _dct_SmryDta

    def ToString(self):
        return self._ToString()

if __name__ == '__main__':
    _diag1 = CGHForceDiagram()
    _diag2 = _diag1.CreateDuplicate()
    print (_diag1)
