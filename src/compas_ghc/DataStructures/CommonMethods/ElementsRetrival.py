def RetreiveCoordinatesFromCGHDiagram (CGHDiag, vKeys):
    _typIter = collections.Iterable
    if isinstance(vKeys, numTyp):
        inpTyp      = 2
        _vKeysLL    = [[vKeys]]
    elif isinstance(vKeys, typIter) == True and isinstance(vKeys[0], numTyp):
        inpTyp      = 1
        _vKeysLL    = [vKeys]
    elif isinstance(vKeys, typIter) == True and isinstance(vKeys[0], typIter) and isinstance(vKeys[0][0], numTyp):
        inpTyp      = 0
        _vKeysLL    = vKeys

    _coordsLL   = [CGHDiag.get_vertices_attributes(names=['x','y','z'],keys=list(_vKeysL)) for _vKeysL in _vKeysLL]
    _coordsRes  = _coordsLL

    for _i in range (0,inpTyp):
        _coordsRes = _coordsRes[0]
    return _coordsRes

def RetrieveCGHDiagramVertex (  self, 
                                bool_VKeys = True, 
                                bool_VInds = True, 
                                bool_RGPt = True):
    _vKeysL_Vertices            = self.VertexKeys()
    _vIndsL_Vertices            = self.VertexIndices()
    _coordsL_EdgesEndPts        = RetreiveCoordinatesFromCGHDiagram(CGHDiag, _eKeysL_Edges)
    return _cDct_RetrvdDta

def RetrieveCGHDiagramEdges  (  self, 
                                bool_EKeys = True, 
                                bool_EInds = True, 
                                bool_RGEndPts = True,
                                bool_RGLns = True):
    _eKeysL_Edges               = self.EdgeKeys()
    _eIndsL_Edges               = self.EdgeIndices()
    _coordsLL_EdgesEndPts       = RetreiveCoordinatesFromCGHDiagram(CGHDiag, _eKeysL_Edges)
    if bool_RGLns:
        _RGLnsL = pass

    return _cDct_RetrvdDta

def RetrieveCGHDiagramFaces  (  self, 
                                bool_FKeys = True, 
                                bool_FInds = True, 
                                bool_VKeysLL = True,
                                bool_RGFacePts = True,
                                bool_RGFacePLns = True):
    _fKeysL_Faces               = self.FaceKeys()
    _fIndsL_Faces               = self.FaceIndices()
    _vKeysLL_FacesVertices      = self.VertexKeysPerFaceKeys()
    _coordsLL_FacesVertices     = RetreiveCoordinatesFromCGHDiagram(_cDtaStruct,_vKeysLL_FacesVertices)
    return _cDct_RetrvdDta
    
