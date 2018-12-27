
import collections
try:
    from Grasshopper import DataTree
    from Grasshopper.Kernel.Data import GH_Path
except:
    pass

def NestedListToGrasshopperDataTree (nstdDtaLst, path_Init = None):
    path_Init = GH_Path(0) if path_Init is None else path_Init
    def _UnpackList (_nstdDtaLst, _path):
        _dtaTr = DataTree[object]()
        for _dtaElem in _nstdDtaLst:
            if isinstance(_dtaElem, collections.Iterable):
                _dtaTr.MergeTree(_UnpackList(_dtaElem, _path.AppendElement(0)))
            else:
                _dtaTr.Add(_dtaElem, _path)
        _path = _path.Increment(-1) #+1 would increment one-level up instead
        return _dtaTr;
        
    return _UnpackList (nstdDtaLst, path_Init);

"""
#example:
_list=[1,[1,2],[2,3],3,4]
_tree=NestedListToGrasshopperDataTree(_list)
"""