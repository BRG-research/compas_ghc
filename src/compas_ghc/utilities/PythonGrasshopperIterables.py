
import collections
from numbers import Number as _numBase
try:
    from Grasshopper import DataTree
    from Grasshopper.Kernel.Data import GH_Path
except:
    pass

class ObjectWrapper:  ##for passing dictionaries
    def __init__(self, obj_ToWrp):
        self._obj = obj_ToWrp
    def __call__(self):
        return self._obj

def NestedListToGrasshopperDataTree (nstdDtaLst, strsL_IterTypExcp=[None], path_Init = None):
    path_Init = GH_Path(0) if path_Init is None else path_Init
    def _UnpackList (_nstdDtaLst, _path):
        _dtaTr = DataTree[object]()
        for _dtaElem in _nstdDtaLst:
            _str_DtaElemClsNm = _dtaElem.__class__.__name__
            # print (_str_DtaElemClsNm in strsL_IterTypExcp)
            if _str_DtaElemClsNm not in strsL_IterTypExcp and isinstance(_dtaElem, collections.Iterable):
                _dtaTr.MergeTree(_UnpackList(_dtaElem, _path.AppendElement(0)))
            else:
                _dtaTr.Add(_dtaElem, _path)
            _path = _path.Increment(-1) #+1 would increment one-level up instead
        return _dtaTr;
        
    return _UnpackList (nstdDtaLst, path_Init);

def TrimGrasshopperDataTree (GHDtaTr_ToTrm, int_LvlsToTrm):
    _GHDtaTr = GHDtaTr_ToTrm
    _dtaTr_Trmd = GH.DataTree[object]()
    _GHPaths = _GHDtaTr.Paths
    _dtaLL = _GHDtaTr.Branches

    for _GHPath, _dtaL in zip (_GHPaths, _dtaLL):
        _intAr_Path     = list(_GHPath.Indices)
        _len_Path       = len(_intAr_Path)
        _len_Path_Trmd  = max(_len_Path - int_LvlsToTrm, 1)
        _GHPath_Trmd = GH_Path(*_intAr_Path[0:_len_Path_Trmd])
        [_dtaTr_Trmd.Add(_dta, _GHPath_Trmd) for _dta in _dtaL]
    return _dtaTr_Trmd;

def DictionaryOfListsToGrasshopperDataTree (dtaDct):
    def _GeneratePath (key):
        if isinstance(key, int):
            _GHPath = GH_Path(key)
        elif isinstance(key, tuple):
            _GHPath = GH_Path(*list(key))
        return _GHPath

    def _UnpackDictionaryofList (_dtaDct):
        _dtaTr = DataTree[object]()
        for _key, _dtaElem in _dtaDct.items():
            _GHPath = _GeneratePath(_key)
            if isinstance(_dtaElem, list):
                for _val in _dtaElem:
                    # print (_GHPath.ToString(), _val)
                    _dtaTr.Add(_val, _GHPath)
            else:
                _dtaTr.Add(_dtaElem, _GHPath)
        return _dtaTr;
        
    return _UnpackDictionaryofList (dtaDct);
"""
#example:
_list=[1,[1,2],[2,3],3,4]
_tree=NestedListToGrasshopperDataTree(_list)
"""