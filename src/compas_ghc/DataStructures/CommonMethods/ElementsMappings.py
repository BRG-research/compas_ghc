
class ElementsMappings:
    def _CreateReverseMap (self, dctMap):
        _dctMap_Rev = {_kB: _kA for _kA, _kB in dctMap.items()}
        return _dctMap_Rev

    def VKeyToIndex(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
        _dctMap__Key_to_Ind = {_v: _i for _i, _v in enumerate(self.VertexKeys(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns))}
        return _dctMap__Key_to_Ind;

    def IndexToVKey(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
        return self._CreateReverseMap(self.VKeyToIndex(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns));

    def EKeyUVToIndex(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
        _dctMap__Key_to_Ind = {(_u, _v): _i for _i, _u, _v in enumerate(self.EdgeKeys(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns))}
        return _dctMap__Key_to_Ind;

    def _EKeyUVToDualERef (self, dualDiag, eKeys_DualDiag = None, boolsL_ExclExt = [False, True], bool_UseEKey=True):
        _eKeys_DualDiag = dualDiag.EdgeKeys(boolsL_ExclExt[1]) if eKeys_DualDiag is None else eKeys_DualDiag
        if not dualDiag:
            return dict(((u, v), index) for index, (u, v) in enumerate(self.edges()))
        dctMap__EKeyUV_to_ERef = dict()

        _eKeysL = self.EdgeKeys(boolsL_ExclExt[0])
        for _i, (_u, _v) in enumerate(_eKeys_DualDiag):
            _f1 = dualDiag.halfedge[_u][_v]
            _f2 = dualDiag.halfedge[_v][_u]
            if (_f1, _f2) in _eKeysL:
                _SelfEKey = (_f1, _f2)
            elif (_f2, _f1) in _eKeysL:
                _SelfEKey = (_f2, _f1)
            else:
                _SelfEKey = None
            _dualRef = _i if bool_UseEKey == False else (_u,_v)
            dctMap__EKeyUV_to_ERef[_SelfEKey] = _dualRef
        return dctMap__EKeyUV_to_ERef

    def EKeyUVToDualEKey(self, dualDiag, eKeys_DualDiag = None, boolsL_ExclExt = [False, True]):
        return self._EKeyUVToDualERef(dualDiag, eKeys_DualDiag, boolsL_ExclExt, bool_UseEKey=True)

    def EKeyUVToDualEIndex(self, dualDiag, eKeys_DualDiag = None, boolsL_ExclExt = [False, True]):
        return self._EKeyUVToDualERef(dualDiag, eKeys_DualDiag, boolsL_ExclExt, bool_UseEKey=False)

    # def EKeyUVToDualIndex(self, dualDiag = None, eKeys_DualDiag = None, bool_ExclExt=True):  ##To remove
    #     _eKeys_DualDiag = dualDiag.EdgeKeys() if eKeys_DualDiag is None else eKeys_DualDiag
    #     if not dualDiag:
    #         return dict(((u, v), index) for index, (u, v) in enumerate(self.edges()))
    #     dctMap__EKeyUV_to_Ind = dict()
    #     for _i, (_u, _v) in enumerate(_eKeys_DualDiag):
    #         _f1 = dualDiag.halfedge[_u][_v]
    #         _f2 = dualDiag.halfedge[_v][_u]
    #         dctMap__EKeyUV_to_Ind[(_f1, _f2)] = _i
    #     return dctMap__EKeyUV_to_Ind

    def IndexToEKeyUV (self, dualDiag = None, eKeys_DualDiag = None):
        _eKeys_DualDiag = dualDiag.EdgeKeys if eKeys_DualDiag is None else eKeys_DualDiag

        if not dualDiag:
            return dict(((u, v), index) for index, (u, v) in enumerate(self.edges()))
        dctMap__EKeyUV_to_Ind = dict()
        for _i, (_u, _v) in enumerate(_eKeys_DualDiag):
            _f1 = dualDiag.halfedge[_u][_v]
            _f2 = dualDiag.halfedge[_v][_u]
            dctMap__EKeyUV_to_Ind[(_f1, _f2)] = _i
        return dctMap__EKeyUV_to_Ind   

    # def EIndKeyToEKey(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
    #     _dctMap__Key_to_Ind = {(_u, _v): _i for _i, _u, _v in enumerate(self.EdgeKeys(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns))}

    def IndexToEKeyUV(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
        _dctMap__Key_to_Ind = self.EKeyUVToIndex(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns)
        return self._CreateReverseMap(_dctMap__Key_to_Ind);

    def FKeyToIndex(self, bool_ExclExt=True):
        return {_f: _i for _i, _f in enumerate(self.FaceKeys(bool_ExclExt))}

    def IndexToFKey(self, bool_ExclExt=True):
        return self._CreateReverseMap(self.FKeyToIndex());

