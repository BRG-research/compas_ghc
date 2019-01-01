try: 
    from compas.numerical import fd_numpy
    from numpy import array
    from numpy import float64
    from copy import deepcopy
except:
    pass

from compas_tna.utilities import LoadUpdater
from compas_tna.diagrams import FormDiagram
FormDiagram()

def CompileForceDensitySolverInputs (formDiag):
    _formDiag = formDiag
    _dctMap__VKey_to_Ind = _formDiag.key_index()

    _coordsL_Vertices   = _formDiag.RetrieveCoordinates(_formDiag.VertexKeys(bool_ExclExt=True))
    _eKeysL_Edges       = _formDiag.EdgeKeys(bool_ExclExt=True, bool_Ind=True)
    _vKeysL_Anchs       = _formDiag.Anchors(bool_ExclExt=True)
    _fltsL_Q            = [float(_v) for _v in _formDiag.get_edges_attribute('q', value=1.0, keys=_eKeysL_Edges)]
    # _coordsL_Vertices   = _formDiag.get_vertices_attributes('xyz')
    # _eKeysL_Edges       = [(_dctMap__VKey_to_Ind[_eKeyU], _dctMap__VKey_to_Ind[_eKeyV]) for _eKeyU, _eKeyV in _formDiag.edges(False)]
    # _vKeysL_Anchs       = [_dctMap__VKey_to_Ind[_vKey] for _vKey in list(_formDiag.anchors())]
    # _fltsL_Q            = _formDiag.get_edges_attribute('q', 1.0)

    return _coordsL_Vertices, _eKeysL_Edges, _vKeysL_Anchs, _fltsL_Q

def UpdateFormDiagramVertices (formDiag, coordsL_Vertices, dctMap__Ind_to_VKey):
    _formDiag = formDiag
    for _i in range (0, len(coordsL_Vertices)):
        _vKey = dctMap__Ind_to_VKey[_i]
        _formDiag.vertex[_vKey]['x'] = coordsL_Vertices[_i][0]
        _formDiag.vertex[_vKey]['y'] = coordsL_Vertices[_i][1]
        _formDiag.vertex[_vKey]['z'] = coordsL_Vertices[_i][2]
    # return formDiag;

def ForceDensitySolver (formData, flt_TtlSWLd, bool_LdsRdistrByTrib = True, iMax_LdsRedistr = 5):
    _formDiag = FormDiagram.from_data(formData)
    _dctMap__Ind_to_VKey = _formDiag.index_key()

    _coordsL_Vertices, _eKeysL_Edges, _vKeysL_Anchs, _fltsL_Q = CompileForceDensitySolverInputs(_formDiag)
    
    #From TNA
    _vecsL_ApldLds  = _formDiag.get_vertices_attributes(['px', 'py', 'pz'])
    _vecsA_TtlLds   = array(_vecsL_ApldLds, dtype=float64)
    _vecsA_ApldLds  = array(_vecsL_ApldLds, dtype=float64)
    update_loads    = LoadUpdater(_formDiag, _vecsA_ApldLds, thickness=1.0, density=flt_TtlSWLd)

    _coordsL_Vertices_0 = deepcopy(_coordsL_Vertices)
    _fltsL_Q_0 = _fltsL_Q
    _i = 0
    while _i < 1:

        _coordsAr_Vertices_0 = array(_coordsL_Vertices_0, dtype=float64)
        update_loads(_vecsA_TtlLds, _coordsAr_Vertices_0)
        _vecsL_TtlLds = _vecsA_TtlLds.tolist()

        _coordsL_Vertices_1, _fltsL_Q_1, _fltsL_EdgeForces, _fltsL_EdgeLgths, _flt_ResidForces = fd_numpy(_coordsL_Vertices_0, 
                                                                                                            _eKeysL_Edges, 
                                                                                                            _vKeysL_Anchs, 
                                                                                                            _fltsL_Q_0, 
                                                                                                            _vecsL_TtlLds)

        UpdateFormDiagramVertices (_formDiag, _coordsL_Vertices_1, _dctMap__Ind_to_VKey)

        _cDctFDSolvRes = {  'vertices0': _coordsL_Vertices,
                            'ld': _vecsL_TtlLds,
                            'vertices': _coordsL_Vertices_1,
                            'q': _fltsL_Q_1,
                            'f': _fltsL_EdgeForces,
                            'l': _fltsL_EdgeLgths,
                            'fR': _flt_ResidForces}

        if bool_LdsRdistrByTrib == False:
            break
        elif _i >= iMax_LdsRedistr - 1: #or if changes fall below threshold
            break

        _coordsL_Vertices_0 = _coordsL_Vertices_1
        _i += 1

    _formData = _formDiag.to_data()
    
    return _formData, _cDctFDSolvRes;



