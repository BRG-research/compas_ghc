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

	vKeysL_Vertices 		= _cDtaStruct.vertex.keys()
	coordsL_Vertices 		= [(_a['x'], _a['y'], _a['z']) for _k, _a in _cDtaStruct.vertex.items()]

	eKeysL_Edges 			= [(_u,_v) for _u,_v in _cDtaStruct.edges() if _u != _v]
	coordsLL_EdgesEndPts	= [_cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=list(_eKey)) for _eKey in eKeysL_Edges]

	fKeysL_Faces			= _cDtaStruct.face.keys()
	vKeysLL_FacesVertices	= [_vL for _f, _vL in _cDtaStruct.face.items()]

	vKeysL_Anchs			= _cDtaStruct.vertices_where({'is_anchor':True})
	coordsL_Anchs			= _cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=vKeysL_Anchs)

	vKeysL_LddVertices		= [_v for _v, _a in _cDtaStruct.vertex.items() if abs(_a['px'])>= 0 or abs(_a['py'])>=0 or abs(_a['pz'])>=0]
	coordsL_LddVertices		= _cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=vKeysL_LddVertices)
	vecsL_VerticesLds		= _cDtaStruct.get_vertices_attributes(names=['px','py','pz'],keys=vKeysL_LddVertices)


	# draw_mesh(quad_mesh_datastructure, group = False)