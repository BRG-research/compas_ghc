import compas
import compas_rhino
try:
    import rhinoscriptsyntax as rs
    import scriptcontext as sc

    find_object = sc.doc.Objects.Find

except ImportError:
    compas.raise_if_ironpython()

def DisassembleCompasDataStructures(cDtaStruct):
	_cDtaStruct = cDtaStruct
	_dct_DiasmdDta = {}

	_vKeysL_Vertices 			= _cDtaStruct.vertex.keys()
	_coordsL_Vertices 			= [(_a['x'], _a['y'], _a['z']) for _k, _a in _cDtaStruct.vertex.items()]
	_dct_DiasmdDta['vertices'] 	= {'vKeys': _vKeysL_Vertices, 'coords': _coordsL_Vertices}

	_eKeysL_Edges 				= [(_u,_v) for _u,_v in _cDtaStruct.edges() if _u != _v]
	_coordsLL_EdgesEndPts		= [_cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=list(_eKey)) for _eKey in _eKeysL_Edges]
	_dct_DiasmdDta['edges'] 	= {'eKeys': _eKeysL_Edges, 'coords': _coordsLL_EdgesEndPts}

	_fKeysL_Faces				= _cDtaStruct.face.keys()
	_vKeysLL_FacesVertices		= [_vL for _f, _vL in _cDtaStruct.face.items()]
	_coordsLL_FacesVertices 	= [_cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=_vKeysL) for _vKeysL in _vKeysLL_FacesVertices]
	_dct_DiasmdDta['faces'] 	= {'fKeys': _fKeysL_Faces, 'vKeys': _vKeysLL_FacesVertices, 'coords':_coordsLL_FacesVertices}

	_vKeysL_Anchs				= _cDtaStruct.vertices_where({'is_anchor':True})
	_coordsL_Anchs				= _cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=_vKeysL_Anchs)
	_dct_DiasmdDta['anchors'] 	= {'vKeys': _vKeysL_Anchs, 'coords': _coordsL_Anchs}

	tol_LdMag = 10e-4
	_vKeysL_LddVertices			= [_v for _v, _a in _cDtaStruct.vertex.items() if abs(_a['px'])> tol_LdMag or abs(_a['py'])>tol_LdMag or abs(_a['pz'])>tol_LdMag]
	_coordsL_LddVertices		= _cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=_vKeysL_LddVertices)
	_vecsL_VerticesLds			= _cDtaStruct.get_vertices_attributes(names=['px','py','pz'],keys=_vKeysL_LddVertices)
	_dct_DiasmdDta['loads'] 	= {'vKeys': _vKeysL_LddVertices, 'coords': _coordsL_LddVertices, 'vecs':_vecsL_VerticesLds}

	return _dct_DiasmdDta;

def DrawDisassembledCompasDataStructures(_dct_DiasmdDta):

	_rgPtsL_Vertices			= [rs.AddPoint(*_coords) for _coords in _dct_DiasmdDta['vertices']['coords']]
	_rgLnsL_Edges				= [rs.AddLine(*_coordsPair) for _coordsPair in _dct_DiasmdDta['edges']['coords']]

	_rgPtsL_Anchs				= [rs.AddPoint(*_coords) for _coords in _dct_DiasmdDta['anchors']['coords']]
	_rgPtsL_LddVertices			= [rs.AddPoint(*_coords) for _coords in _dct_DiasmdDta['loads']['coords']]
	_rgVecsL_VerticesLds		= [rs.VectorCreate(_vec, [0,0,0]) for _vec in _dct_DiasmdDta['loads']['vecs']]

	return _rgPtsL_Vertices, _rgLnsL_Edges, _rgPtsL_Anchs, _rgPtsL_LddVertices, _rgVecsL_VerticesLds;
	# draw_mesh(quad_mesh_datastructure, group = False)