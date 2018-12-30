
class ElementsMappings:
    def _CreateReverseMap (self, dctMap):
        _dctMap_Rev = {_kB: _kA for _kA, _kB in dctMap.items()}
        return _dctMap_Rev

    def VKeyToIndex(self):
        _dctMap__Key_to_Ind = {_v: _i for _i, _v in enumerate(self.vertex.keys())}
        return _dctMap__Key_to_Ind;

    def IndexToVKey(self):
        return self._CreateReverseMap(self.VKeyToIndex());

    def EKeyUVToIndex(self):
        _dctMap__Key_to_Ind = {(_u, _v): _i for _i, _u, _v in enumerate(self.edges(False))}
        return _dctMap__Key_to_Ind;
    

    def IndexToEKeyUV(self):
        _dctMap__Key_to_Ind = self.EKeyUVToIndex()
        _dctMap__Ind_to_Key = self._CreateReverseMap(_dctMap__Key_to_Ind)
        return _dctMap__Ind_to_Key;

    def FKeyToIndex(self):
        return {_f: _i for _i, _f in enumerate(self.face.keys())}

    def FKeyToIndex(self):
        return self._CreateReverseMap(self.FKeyToIndex());

