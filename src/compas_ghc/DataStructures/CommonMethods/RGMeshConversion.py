try:
    from System import Array
    import Rhino as RC
except:
    pass

class RGMeshConversion ():
    def ToRGMesh(self, bool_ExclExt=True):
        _RGMesh = RC.Geometry.Mesh()
        _vKeysL_Vertices            = list(self.VertexKeys(bool_ExclExt))
        _coordsL_Vertices           = self.RetreiveCoordinates(_vKeysL_Vertices) 
        [_RGMesh.Vertices.Add(_coords[0],_coords[1],_coords[2]) for _coords in _coordsL_Vertices]

        _fKeysL_Faces               = self.FaceKeys(bool_ExclExt)
        _vKeysLL_FacesVertices      = self.FaceVerticesKeys(bool_ExclExt)
        [_RGMesh.Faces.AddFace(*_vKeysL) for _vKeysL in _vKeysLL_FacesVertices if len(_vKeysL) <= 4]

        _RGMesh.Normals.ComputeNormals()
        _RGMesh.Compact()
        return _RGMesh