from compas_tna.diagrams import FormDiagram
from compas.numerical import fd_numpy
from copy import deepcopy

def CompileForceDensitySolverInputs (formDiag):
    _formDiag = formDiag
    _dctMap__VKey_to_Ind = _formDiag.key_index()

    _coordsL_Vertices   = _formDiag.get_vertices_attributes('xyz')
    _eKeysL_Edges       = [(_dctMap__VKey_to_Ind[_eKeyU], _dctMap__VKey_to_Ind[_eKeyV]) for _eKeyU, _eKeyV in _formDiag.edges(False)]
    _vKeysL_Anchs       = [_dctMap__VKey_to_Ind[_vKey] for _vKey in list(_formDiag.anchors())]
    _fltsL_Q            = _formDiag.get_edges_attribute('q', 1.0)

    return _coordsL_Vertices, _eKeysL_Edges, _vKeysL_Anchs, _fltsL_Q

def CompileForceDensityLoads(formDiag, flt_TtlSWLd, bool_LdsRdistrByTrib = True):
    _formDiag = formDiag

    _vecsL_SWLds        = CalculateSelfWeightLoads(_formDiag, flt_TtlSWLd, bool_LdsRdistrByTrib)
    _vecsL_PtLds        = _formDiag.get_vertices_attributes(('px', 'py', 'pz'), (0.0, 0.0, -1.0))   
    _vecsL_TtlLds       = [[_vec_SWLd[_ax] + _vec_PtLd[_ax] for _ax in range (0,3)] for _vec_SWLd, _vec_PtLd in zip(_vecsL_SWLds, _vecsL_PtLds)]
    return _vecsL_TtlLds;

def CalculateSelfWeightLoads (formDiag, flt_TtlSWLd, bool_LdsRdistrByTrib = True):
    _formDiag       = formDiag
    _flt_TtlSWLd    = flt_TtlSWLd
    _vecsL_SWLds    = []

    if bool_LdsRdistrByTrib == False:
        _len_Vertices       = len(_formDiag.vertex.keys())
        _flt_SWLd           = _flt_TtlSWLd/_len_Vertices
        _vecsL_SWLds        = [[0,0,_flt_SWLd * 1] for _i in range(0, _len_Vertices)]
    else:
        _fltsL_VertexArs    = []
        [_fltsL_VertexArs.append(_formDiag.vertex_area(_vKey)) for _vKey in _formDiag.vertex.keys()]

        _flt_Sum_VertexArs  = sum(_fltsL_VertexArs)
        _flt_AdjFac         = _flt_TtlSWLd / _flt_Sum_VertexArs
        _vecsL_SWLds        = [[0,0,_flt_VAr * _flt_AdjFac * 1] for _flt_VAr in _fltsL_VertexArs]

    return _vecsL_SWLds;


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
    _vecsL_TtlLds = CompileForceDensityLoads (_formDiag, flt_TtlSWLd, bool_LdsRdistrByTrib)

    

    _coordsL_Vertices_0 = deepcopy(_coordsL_Vertices)
    _fltsL_Q_0 = _fltsL_Q
    _i = 0
    while _i < 1:
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
        # _fltsL_Q_0 = _fltsL_Q_1
        _vecsL_TtlLds = CompileForceDensityLoads (_formDiag, flt_TtlSWLd, bool_LdsRdistrByTrib)
        _i += 1

    _formData = _formDiag.to_data()
    
    return _formData, _cDctFDSolvRes;

