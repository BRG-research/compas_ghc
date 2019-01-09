from compas_ghc.Utilities.RCGeometriesDrawers   import RGPointDrawers as RGPtDwrs
from compas_ghc.Utilities.RCGeometriesDrawers   import RGLineDrawers as RGLnDwrs
import collections
typIter = collections.Iterable 
from numbers import Number as numTyp

from collections import OrderedDict

class ElementsRetrival:

    def RetrieveCoordinates (self, vKeys):
        if isinstance(vKeys, numTyp):
            inpTyp      = 2
            _vKeysLL    = [[vKeys]]
        elif isinstance(vKeys, typIter) == True and isinstance(vKeys[0], numTyp):
            inpTyp      = 1
            _vKeysLL    = [vKeys]
        elif isinstance(vKeys, typIter) == True and isinstance(vKeys[0], typIter) and isinstance(vKeys[0][0], numTyp):
            inpTyp      = 0
            _vKeysLL    = vKeys

        _coordsLL   = [self.get_vertices_attributes(names=['x','y','z'],keys=list(_vKeysL)) for _vKeysL in _vKeysLL]
        _coordsRes  = _coordsLL

        for _i in range (0,inpTyp):
            _coordsRes = _coordsRes[0]
        return _coordsRes

    def _FilterDictionaryByAttributes (self, dtaDct, strsL_AttrNms=None):
        _dtaDct = dtaDct
        if strsL_AttrNms is not None:
            for _key, _attr in _dtaDct.items():
                _attr_New = {}
                for _attrNm, attrVal in _attr.items():
                    if _attrNm in strsL_AttrNms:
                        _attr_New[_attrNm] = attrVal
                _dtaDct[_key] = _attr_New 

    def _BreakdownData (self, dtaDct, bool_RtnDtaLL, strsL_AttrNms):
        _dtaDct = dtaDct
        if strsL_AttrNms is not None and len(strsL_AttrNms)>0 and bool_RtnDtaLL == True:
            _nElems = len(dtaDct.keys())
            _nAttrs = len(strsL_AttrNms)
            _dtaLL  = [[None for __iElem in range(0, _nElems)] for __iAttr in range(0, _nAttrs)]
            _iElem  = 0
            for _key, _attr in _dtaDct.items():
                for _attrNm, attrVal in _attr.items():
                    if _attrNm in strsL_AttrNms:
                        _iAttr = strsL_AttrNms.index(_attrNm)
                        _dtaLL[_iAttr][_iElem] = attrVal
                _iElem += 1
            return _dtaLL
        else:
            return dtaDct

    def RetrieveVertexData (self, bool_ExclExt = True, strsL_AttrNms = None, bool_RtnDtaLL = False, bool_RtnKeysLst=False):
        _vKeysL = self.VertexKeys(bool_ExclExt=bool_ExclExt)
        _dtaDct = OrderedDict([(_v, _a) for _v, _a in self.vertex.items() if _v in _vKeysL])
        self._FilterDictionaryByAttributes(_dtaDct, strsL_AttrNms)
        _dtaFnl = self._BreakdownData(_dtaDct, bool_RtnDtaLL, strsL_AttrNms)
        if not bool_RtnKeysLst:
            return _dtaFnl;
        else:
            return _dtaFnl, _vKeysL

    def RetrieveEdgeData (self, bool_ExclExt = True, bool_RtnDtaLL = False, strsL_AttrNms = None, bool_RtnKeysLst=False):
        _eKeysL = self.EdgeKeys(bool_ExclExt=bool_ExclExt)
        _dtaDct = OrderedDict([((_u, _v), _a) for _u, _v, _a in self.edges(True) if (_u, _v) in _eKeysL])
        self._FilterDictionaryByAttributes(_dtaDct, strsL_AttrNms)
        _dtaFnl = self._BreakdownData(_dtaDct, bool_RtnDtaLL, strsL_AttrNms)
        if not bool_RtnKeysLst:
            return _dtaFnl;
        else:
            return _dtaFnl, _eKeysL

    def RetrieveFaceData (self, bool_ExclExt = True, strsL_AttrNms = None):
        _fKeysL = self.FaceKeys(bool_ExclExt=bool_ExclExt)
        _dtaDct = {_f: _a for _f, _a in self.faces(True) if _f in _fKeysL}
        self._FilterDictionaryByAttributes(_dtaDct, strsL_AttrNms)
        return _dtaDct;

    def RetrieveFullVerticesData    (self, 
                                    bool_ExclExt = True,
                                    bool_Keys = True, 
                                    bool_Ind = True, 
                                    bool_Coords = True,
                                    bool_DrawRG = True,
                                    dctsL_AddtlVertexCndtns = {}):
        _resDct                         = {} 
        _vKeysL_Vertices                = self.VertexKeys(bool_ExclExt, dctsL_AddtlVertexCndtns)
        if bool_Keys:
            _resDct['keys']             = _vKeysL_Vertices
        if bool_Ind:
            _vIndsL_Vertices            = self.VertexKeys(bool_ExclExt, bool_Ind=True, dctsL_AddtlVertexCndtns=dctsL_AddtlVertexCndtns)
            _resDct['inds']             = _vIndsL_Vertices
        if bool_Coords or bool_DrawRG:
            _coordsL_Vertices           = self.RetrieveCoordinates(_vKeysL_Vertices)
            if bool_Coords:
                _resDct['coords']       = _coordsL_Vertices
            if bool_DrawRG:
                _resDct['RGs']          = RGPtDwrs.CoordinatesListToRGPointsList(_coordsL_Vertices)
        return _resDct

    def RetrieveFullEdgesData     ( self, 
                                    bool_ExclExt = True,
                                    bool_Key = True, 
                                    bool_Ind = True,
                                    bool_Coords = True, 
                                    bool_DrawRGPts = True,
                                    bool_DrawRGLns = True,
                                    dctsL_AddtlVertexCndtns = {},
                                    bool_Dta = False):
        
        _resDct                         = {}
        _eKeysL_Edges                   = self.EdgeKeys(bool_ExclExt)
        if bool_Key:
            _resDct['keys']             = _eKeysL_Edges
        if bool_Ind:   
            _eIndsL_Edges               = self.EdgeKeys(bool_ExclExt, bool_Ind=True)
            _resDct['inds']             = _eIndsL_Edges
        if bool_DrawRGPts or bool_DrawRGLns:
            _resDct['RGs']              = {}
            _coordsL_LnEndPts           = self.RetrieveCoordinates(_eKeysL_Edges)
            if bool_DrawRGPts:
                _RGPtsPairsL            = RGPtDwrs.CoordinatesList2ToRGPointsList2(_coordsL_LnEndPts)
                _resDct['RGs']['pts']   = _RGPtsPairsL
            if bool_DrawRGLns:
                _RGLnsL                 = RGLnDwrs.CoordinatesPairsListToRGLinesList(_coordsL_LnEndPts)
                _resDct['RGs']['lns']   = _RGLnsL
        return _resDct

    def RetrieveFullFacesData   (   self, 
                                    bool_ExclExt = True,
                                    bool_Key = True, 
                                    bool_Ind = True,
                                    bool_Coords = True,
                                    bool_DrawRGPts  = True,
                                    bool_DrawRGPLns = True,
                                    bool_Coords_FaceCnts = True,
                                    bool_DrawRGPts_FaceCnts = True):
        _resDct                                 = {}
        _fKeysL_Faces                           = self.FaceKeys(bool_ExclExt)



        if bool_DrawRGPts or bool_DrawRGPLns:
            _resDct['RGs']                      = {}
            _vKeysLL_FacesVertices              = self.FaceVerticesKeys(bool_ExclExt)
            
        if bool_Key:
            _resDct['keys']                     = {}
            _resDct['keys'][0]                  = _fKeysL_Faces
            _resDct['keys'][1]                  = _vKeysLL_FacesVertices
        if bool_Ind:   
            _fIndsL_Faces                       = self.FaceKeys(bool_ExclExt, bool_Ind=True)
            _resDct['inds']                     = {}
            _resDct['inds'][0]                  = _fIndsL_Faces
            _resDct['inds'][1]                  = self.FaceVerticesKeys(bool_ExclExt, bool_Ind=True)

        if any([bool_Coords, bool_DrawRGPts, bool_DrawRGPLns]):
            _coordsLL_FacesVertices             = self.RetrieveCoordinates(_vKeysLL_FacesVertices)
        if any([bool_Coords_FaceCnts, bool_DrawRGPts_FaceCnts]):
            from compas.geometry import centroid_points
            _coordsL_FaceCnts                   = [centroid_points(_coordsL) for _coordsL in _coordsLL_FacesVertices]

        if any([bool_Coords, bool_Coords_FaceCnts]):
            _resDct['coords']                   = {}
            if bool_Coords:
                _resDct['coords'][0]            = _coordsLL_FacesVertices
            if bool_Coords_FaceCnts:
                _resDct['coords'][1]            = _coordsL_FaceCnts

        if any([bool_DrawRGPts, bool_DrawRGPts_FaceCnts, bool_DrawRGPLns]):
            _resDct['RGs']                      = {}
            if any([bool_DrawRGPts, bool_DrawRGPts_FaceCnts]):
                _resDct['RGs']['pts']           = {}
                if bool_DrawRGPts:  
                    _RGPtsLL_FaceVertices       = RGPtDwrs.CoordinatesList2ToRGPointsList2(_coordsLL_FacesVertices)  #ListList
                    _resDct['RGs']['pts'][0]    = _RGPtsLL_FaceVertices
                if bool_DrawRGPts_FaceCnts:  
                    _RGPtsL_FaceCnts            = RGPtDwrs.CoordinatesListToRGPointsList(_coordsL_FaceCnts)        
                    _resDct['RGs']['pts'][0]    = _RGPtsL_FaceCnts

            if bool_DrawRGPLns:
                _RGPlnsL                        = RGLnDwrs.CoordinatesList2ToRGPolylinesList(_coordsLL_FacesVertices, bool_IsPrdic=True)
                _resDct['RGs']['plns']          = _RGPlnsL
                
        return _resDct

