
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

    def IndexToEKeyUV(self, bool_ExclExt=True, dctsL_AddtlVertexCndtns={}):
        _dctMap__Key_to_Ind = self.EKeyUVToIndex(bool_ExclExt, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns)
        return self._CreateReverseMap(_dctMap__Key_to_Ind);

    def FKeyToIndex(self, bool_ExclExt=True):
        return {_f: _i for _i, _f in enumerate(self.FaceKeys(bool_ExclExt))}

    def IndexToFKey(self, bool_ExclExt=True):
        return self._CreateReverseMap(self.FKeyToIndex());

