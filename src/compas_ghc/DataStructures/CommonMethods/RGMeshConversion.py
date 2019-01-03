try:
    from System import Array
    import Rhino as RC
except:
    pass

class RGMeshConversion ():
    def ToRGMesh(self, bool_ExclExt=True):
        _RGMesh = RC.Geometry.Mesh()
        _vKeysL_Vertices            = list(self.VertexKeys(bool_ExclExt))
        _coordsL_Vertices           = self.RetrieveCoordinates(_vKeysL_Vertices) 
        [_RGMesh.Vertices.Add(_coords[0],_coords[1],_coords[2]) for _coords in _coordsL_Vertices]

        _fKeysL_Faces               = self.FaceKeys(bool_ExclExt)
        _vKeysLL_FacesVertices      = self.FaceVerticesKeys(bool_ExclExt)
        [_RGMesh.Faces.AddFace(*_vKeysL) for _vKeysL in _vKeysLL_FacesVertices if len(_vKeysL) <= 4]

        _RGMesh.Normals.ComputeNormals()
        _RGMesh.Compact()
        return _RGMesh

    @classmethod
    def FromRGMesh(cls, RGMesh):
        _RGMesh                     = RGMesh
        _cDtaStruct                 = cls()

        _RGPtsL                     = list(_RGMesh.Vertices.ToPoint3dArray())
        [_cDtaStruct.add_vertex(x=_RGPt.X, y=_RGPt.Y, z=_RGPt.Z) for _RGPt in _RGPtsL]

        for _RGMeshFace in RGMesh.Faces:
            _vKeysL = []
            [_vKeysL.append(_vKey) for _vKey in _RGMeshFace if _vKey not in _vKeysL]
            _cDtaStruct.add_face(_vKeysL)

        return _cDtaStruct;
