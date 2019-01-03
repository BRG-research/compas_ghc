class ElementsIdentifiers:
    def VerticesOnBoundary(self, bool_FltLst=True):
        if bool_FltLst:
            return [_v for _vL in self.vertices_on_boundaries() for _v in _vL];
        else:
            return self.vertices_on_boundaries();

    def Anchors(self, bool_ExclExt, bool_Ind = False):
        _vKeysL_Anchs           = self.vertices_where({'is_fixed':True})
        if bool_Ind:
            _dctMap__VKey_to_Ind    = self.VKeyToIndex(bool_ExclExt = bool_ExclExt)
            _vKeysIL_Anchs          = [_dctMap__VKey_to_Ind[_v] for _v in _vKeysL_Anchs]
            return _vKeysIL_Anchs;
        else:
            return _vKeysL_Anchs;


    def VertexKeys (self, bool_ExclExt = True, bool_Ind = False, dctsL_AddtlVertexCndtns = {}):
        if bool_ExclExt or len(dctsL_AddtlVertexCndtns)>0:
            dctsL_Cndtns = {}
            if bool_ExclExt:
                dctsL_Cndtns.update({'is_external':False})
            dctsL_Cndtns.update(dctsL_AddtlVertexCndtns)
            _vKeysL = [_k for _k in self.vertices_where(conditions = dctsL_Cndtns, data=False)]
        else:
            _vKeysL = list(self.vertex.keys())

        if not bool_Ind:
            return _vKeysL;
        else:
            return list(range(0, len(_vKeysL))); 

    def EdgeKeys (self, bool_ExclExt = True, bool_Ind = False, dctsL_AddtlVertexCndtns = {}):
        if bool_ExclExt:
            _vKeys_VerticesOnBound = self.VerticesOnBoundary(bool_FltLst = True)
            _eKeysL = [(_u, _v) for _u, _v in self.edges(False) if _u not in _vKeys_VerticesOnBound and _v not in _vKeys_VerticesOnBound] #self.edges_where(conditions={'is_edge':True})]
        else:
            _eKeysL = [(_u, _v) for _u, _v in self.edges(False)]

        if not bool_Ind:
            return _eKeysL
        else:
            dctMap__VKey_to_Ind = self.VKeyToIndex(bool_ExclExt, dctsL_AddtlVertexCndtns = dctsL_AddtlVertexCndtns)
            return [(dctMap__VKey_to_Ind[_eKey[0]], dctMap__VKey_to_Ind[_eKey[1]]) for _eKey in _eKeysL]

    def FaceKeys (self, bool_ExclExt=True, bool_Ind = False):
        if bool_ExclExt:
            _fKeys_FacesOnBounds = self.faces_on_boundary()
            _fKeysL = [_fK for _fK in self.face.keys() if _fK not in _fKeys_FacesOnBounds]
        else:
            _fKeysL = list(self.face.keys())

        if not bool_Ind:
            return _fKeysL;
        else:
            return list(range(0, len(_fKeysL)));

    def FaceVerticesKeys (self, bool_ExclExt = True, bool_Ind = False, dctsL_AddtlVertexCndtns = {}):
        _fKeysL = self.FaceKeys(bool_ExclExt)
        _vKeysLL_FaceVertices = [list(self.face[_fKey]) for _fKey in _fKeysL]
        if not bool_Ind:
            return _vKeysLL_FaceVertices;
        else:
            dctMap__VKey_to_Ind = self.VKeyToIndex(dctsL_AddtlVertexCndtns)
            return [[dctMap__VKey_to_Ind[_v] for _v in _vKeysLL_FaceVertices[_fKey]] for _fKey in _fKeysL]
    
