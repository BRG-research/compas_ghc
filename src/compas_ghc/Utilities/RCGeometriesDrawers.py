try:
    from System import Array
    import Rhino as RC
except:
    pass

class RGPointDrawers:
    @staticmethod
    def CoordinatesToRGPoint(coords_PtToDw):
        return RC.Geometry.Point3d(*coords_PtToDw); 

    @staticmethod
    def CoordinatesListToRGPointsList(coordsL_PtsToDw):
        _RGPtsL             = [RGPointDrawers.CoordinatesToRGPoint(_coords) for _coords in coordsL_PtsToDw]
        return _RGPtsL

    @staticmethod
    def CoordinatesList2ToRGPointsList2 (coordsLL_PtsToDw):
        _RGPtsLL            = [[RGPointDrawers.CoordinatesToRGPoint(_coords) for _coords in list(_coordsL)] for _coordsL in coordsLL_PtsToDw] #list() to convert tuples
        return _RGPtsLL

class RGLineDrawers:
    @staticmethod
    def CoordinatesPairsListToRGLinesList(coordsPairL_LnEndPts):
        _RGPtsLL            = RGPointDrawers.CoordinatesList2ToRGPointsList2(coordsPairL_LnEndPts)
        _RGLnsL             = [RC.Geometry.Line(*_RGPtsPair) for _RGPtsPair in _RGPtsLL]
        return _RGLnsL

    @staticmethod    
    def CoordinatesList2ToRGPolylinesList(coordsLL_PlnsVertices, bool_IsPrdic = False):
        _RGPtsLL            = RGPointDrawers.CoordinatesList2ToRGPointsList2(coordsLL_PlnsVertices)
        _RGPlnsL            = []
        for _RGPtsL in _RGPtsLL:
            _RGPtsL = _RGPtsL + [_RGPtsL[0]] if bool_IsPrdic else _RGPtsL
            _RGPln  = RC.Geometry.Polyline(Array[RC.Geometry.Point3d](_RGPtsL))
            _RGPlnsL.append(_RGPln)
        return _RGPlnsL