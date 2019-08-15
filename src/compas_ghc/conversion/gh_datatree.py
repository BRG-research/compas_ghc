try:
    from Grasshopper import DataTree
    from Grasshopper.Kernel.Data import GH_Path
    from scriptcontext import sticky
except:
    pass
import collections



def list_to_tree (nstdDtaLst, strsL_IterTypExcp=[None], path_Init = None):
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

def tree_to_list (aTree):
    theList = []
    for i in range(aTree.BranchCount ):
        thisListPart = []
        thisBranch = aTree.Branch(i)
        for j in range(len(thisBranch)):
            thisListPart.append( thisBranch[j] )
        theList.append(thisListPart)
    return theList

def trim_tree (datatree, deg = 1):
    paths = datatree.Paths
    datacounts = datatree.DataCount
    datatree_new = DataTree[object]()
    for _path in paths:
        _branch_data = datatree.Branch(_path)
        _path_new = GH_Path(*list(_path.Indices)[0:-deg])
        for _data in _branch_data:
            datatree_new.Add(_data, _path_new)
    return datatree_new           

from compas_ghc.conversion.gh_datatree import list_to_tree
