try:
	import Rhino.Geometry as RG
except:
	pass

from compas_ghc.DataStructures.CGHDiagrams 	import CGHDiagram

def RGMeshToCompasDataStructure (RGMesh, clsInstc = CGHDiagram):
    _RGMesh 			= RGMesh
    _RGPtsL     		= list(_RGMesh.Vertices.ToPoint3dArray())
    _cDtaStruct     	= clsInstc()
    
    [_cDtaStruct.add_vertex(x=_RGPt.X, y=_RGPt.Y, z=_RGPt.Z) for _RGPt in _RGPtsL]
    for _RGMeshFace in RGMesh.Faces:
        _vKeysL = []
        [_vKeysL.append(_vKey) for _vKey in _RGMeshFace if _vKey not in _vKeysL]
        _cDtaStruct.add_face(_vKeysL)

    return _cDtaStruct

def CompasDataStructureToRGMesh (cDtaStruct):

    _cDtaStruct = cDtaStruct
    
    _RGMesh = RG.Mesh()

    _vKeysL_Vertices            = sorted(list(_cDtaStruct.vertex.keys()))
    _coordsL_Vertices           = _cDtaStruct.get_vertices_attributes(names=['x','y','z'],keys=_vKeysL_Vertices)
    [_RGMesh.Vertices.Add(_coords[0],_coords[1],_coords[2]) for _coords in _coordsL_Vertices]

    _fKeysL_Faces               = sorted(list(_cDtaStruct.face.keys()))
    _vKeysLL_FacesVertices      = [_cDtaStruct.face[_fKey] for _fKey in _fKeysL_Faces]
    [_RGMesh.Faces.AddFace(*_vKeysL) for _vKeysL in _vKeysLL_FacesVertices if len(_vKeysL) <= 4]

    _RGMesh.Normals.ComputeNormals()
    _RGMesh.Compact()

    return _RGMesh;

