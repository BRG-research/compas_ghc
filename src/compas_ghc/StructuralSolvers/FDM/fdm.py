try: 
    from compas.numerical import fd_numpy
    from numpy import array
    from numpy import float64
    from copy import deepcopy
except:
    pass

from compas_tna.utilities import LoadUpdater
from compas_ghc.DataStructures.CGHDiagrams import CGHFormDiagram as FormDiagram
from copy import deepcopy

def UpdateFormDiagramVertices (formDiag, coordsL_Vertices, dctMap__Ind_to_VKey):
    _formDiag = formDiag
    for _i in range (0, len(coordsL_Vertices)):
        _vKey = dctMap__Ind_to_VKey[_i]
        _formDiag.vertex[_vKey]['x'] = coordsL_Vertices[_i][0]
        _formDiag.vertex[_vKey]['y'] = coordsL_Vertices[_i][1]
        _formDiag.vertex[_vKey]['z'] = coordsL_Vertices[_i][2]

def ForceDensitySolver (formData, flt_TtlSWLd, bool_LdsRdistrByTrib = True, iMax_LdsRedistr = 5):
    _formDiag = FormDiagram.from_data(formData)

    _dctMap__Ind_to_VKey = _formDiag.IndexToVKey(bool_ExclExt=False)
    _dctMap__VKey_to_Ind = _formDiag.VKeyToIndex(bool_ExclExt=False)

    _vKeysL_Vertices    = _formDiag.VertexKeys(bool_ExclExt=False)
    _coordsL_Vertices   = _formDiag.RetrieveCoordinates(_vKeysL_Vertices)
    _eKeysL_Edges       = _formDiag.EdgeKeys(bool_ExclExt=False, bool_Ind=False)
    _eIndKeysL_Edges    = _formDiag.EdgeKeys(bool_ExclExt=False, bool_Ind=True)
    _vIndKeysL_Anchs    = [_dctMap__VKey_to_Ind[_vKey] for _vKey in list(_formDiag.anchors())]
    _fltsL_Q            = _formDiag.get_edges_attribute('q', 1.0)

    
    _vecsL_ApldLds  = _formDiag.get_vertices_attributes(['px', 'py', 'pz'])
    _vecsA_TtlLds   = array(_vecsL_ApldLds, dtype=float64)
    _vecsA_ApldLds  = array(_vecsL_ApldLds, dtype=float64)
    _LdUpdtr        = LoadUpdater(_formDiag, _vecsA_ApldLds, thickness=1.0, density=flt_TtlSWLd)

    _coordsL_Vertices_0 = deepcopy(_coordsL_Vertices)
    _fltsL_Q_0          = _fltsL_Q
    _iMax               = 10

    _cDctStructSolvOprDta = {'res':{'all':{}}}
    _i = 0
    while _i < _iMax:

        ##Update Loads
        _coordsAr_Vertices_0 = array(_coordsL_Vertices_0, dtype=float64)
        _LdUpdtr(_vecsA_TtlLds, _coordsAr_Vertices_0)
        _vecsL_TtlLds = _vecsA_TtlLds.tolist()

        _coordsL_Vertices_1, _fltsL_Q_1, _fltsL_EdgeForces, _fltsL_EdgeLgths, _flt_ResidForces = fd_numpy(_coordsL_Vertices_0, 
                                                                                                            _eIndKeysL_Edges, 
                                                                                                            _vIndKeysL_Anchs, 
                                                                                                            _fltsL_Q_0, 
                                                                                                            _vecsL_TtlLds)

        UpdateFormDiagramVertices (_formDiag, _coordsL_Vertices_1, _dctMap__Ind_to_VKey)

        _cDctFDRes = {          'lds':          _vecsL_TtlLds,
                                'coords':     _coordsL_Vertices_1,
                                'q':            _fltsL_Q_1,
                                'f':            _fltsL_EdgeForces,
                                'lgths':        _fltsL_EdgeLgths,
                                'fResid':       _flt_ResidForces    }
        _cDctFDRes_Prtl = {_kV: [_v[0] for _v in _lA ] for _kV, _lA in _cDctFDRes.items() if _kV not in ['lds', 'coords']}
        _cDctFDRes.update(_cDctFDRes_Prtl)  ##Remove the listed values
        _cDctStructSolvOprDta['res']['all'][int(_i)] = _cDctFDRes

        if bool_LdsRdistrByTrib == False:
            break
        elif _i >= iMax_LdsRedistr - 1: 
            break

        _coordsL_Vertices_0 = _coordsL_Vertices_1
        _i += 1

    _i_FnlIter = max(list(_cDctStructSolvOprDta['res']['all'].keys())) 
    _formDiag.SetEdgesAttributeWithValues(str_AttrNm='f',dtaL_AttrVals=_cDctStructSolvOprDta['res']['all'][_i_FnlIter]['f'],eKeysL=_eKeysL_Edges)
    _formDiag.SetEdgesAttributeWithValues(str_AttrNm='q',dtaL_AttrVals=_cDctStructSolvOprDta['res']['all'][_i_FnlIter]['q'], eKeysL=_eKeysL_Edges)
    _formDiag.SetEdgesAttributeWithValues(str_AttrNm='l',dtaL_AttrVals=_cDctStructSolvOprDta['res']['all'][_i_FnlIter]['lgths'], eKeysL=_eKeysL_Edges)
    _formDiag.SetVerticesAttributesWithValues(strsL_AttrsNms=['px','py','pz'],dtaLL_AttrsVals=_cDctStructSolvOprDta['res']['all'][_i_FnlIter]['lds'], vKeysL=_vKeysL_Vertices)
    _formDiag.SetVerticesAttributeWithValues(str_AttrNm='fR',dtaL_AttrVals=_cDctStructSolvOprDta['res']['all'][_i_FnlIter]['fResid'], vKeysL=_vKeysL_Vertices)

    _formData = _formDiag.to_data()
    return _formData, _cDctStructSolvOprDta;

