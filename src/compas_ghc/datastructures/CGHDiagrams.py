from compas_tna.diagrams                                                import Diagram
from compas_tna.diagrams                                                import FormDiagram
from compas_tna.diagrams                                                import ForceDiagram
from compas_ghc.DataStructures.CGHDataTypesBase                         import CGHDataStructuresBase
from compas_ghc.DataStructures.CommonMethods.ElementsMappings           import ElementsMappings

class CGHDiagram(   CGHDataStructuresBase,
                    Diagram):

    def __init__ (self):
        Diagram.__init__(self)
        # super(CGHDiagram, self).__init__()

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Nodes'    : self.number_of_vertices(),
                            '# of Members'  : self.number_of_edges(),
                            '# of Spaces'   : self.number_of_faces(),
                        }
        return _dct_SmryDta

    def ToString(self):
        return self._ToString()



class CGHFormDiagram(   CGHDataStructuresBase, 
                        FormDiagram):
    def __init__ (self):
        FormDiagram.__init__(self)  
        self.vec_GblArLd = [0,0,0]

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Nodes'    : self.number_of_vertices(),
                            '# of Members'  : self.number_of_edges(),
                            '# of Spaces'   : self.number_of_faces(),
                        }
        return _dct_SmryDta


    def CustomAttributesData(self):
        dct_AddtlDta = {}
        if hasattr(self,'vec_GblArLd'):
            dct_AddtlDta = {'vec_GblArLd': self.vec_GblArLd}
        return dct_AddtlDta

    def ToString(self):
        return self._ToString()

class CGHForceDiagram(      CGHDataStructuresBase, 
                            ForceDiagram):
    def __init__ (self):
        ForceDiagram.__init__(self)  

    def CompileToStringSummary (self):
        _dct_SmryDta = {    
                            '# of Space Vertices'       : self.number_of_vertices(),
                            '# of Members'              : self.number_of_edges(),
                            '# of Node Faces'           : self.number_of_faces(),
                        }
        return _dct_SmryDta

    def ToString(self):
        return self._ToString()

if __name__ == '__main__':
    _diag1 = CGHForceDiagram()
    _diag2 = _diag1.CreateDuplicate()
    print (_diag1)
