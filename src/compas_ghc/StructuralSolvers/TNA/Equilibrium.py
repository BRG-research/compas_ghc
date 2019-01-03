from compas_ghc.DataStructures.CGHDiagrams import CGHFormDiagram as FormDiagram
from compas_ghc.DataStructures.CGHDiagrams import CGHForceDiagram as ForceDiagram
from compas_tna.equilibrium import horizontal_nodal
from compas_tna.equilibrium import vertical_from_zmax

from copy import deepcopy

__all__ = [
    'HorizontalEquilibrium_fromData',
    'VerticalEquilibrium_fromZMax_fromData'
]

def VerticalEquilibrium_fromZMax_fromData (formdata, zmax, kmax=100, density = 1.0): # *args, **kwargs
    form = FormDiagram.from_data(deepcopy(formdata))
    scale = vertical_from_zmax(form, zmax, kmax, density = density)
    return form.to_data(), scale;


def HorizontalEquilibrium_fromData (formdata, forcedata, alpha = 100, kmax = 100): # *args, **kwargs
    form = FormDiagram.from_data(deepcopy(formdata))
    force = ForceDiagram.from_data(deepcopy(forcedata))

    horizontal_nodal (form, force, alpha, kmax)

    formdata, forcedata = form.to_data(), force.to_data()
    
    return formdata, forcedata

def EvaluateParallisationSuccess (formDiag, ang_Thrld=5):
    
    _aL             = formDiag.get_edges_attribute(name='a')
    _cDctRes        = {}
    boolsL_APass    = [_a <= ang_Thrld for _a in aL]
    flt_PCPass      = sum(boolsL_APass) / len(_aL)
    bool_AllPass    = all(boolsL_APass)

    _cDctRes    = {'a':_aL, 'aPass':boolsL_APass, 'pcPass':flt_PCPass, 'allPass':bool_AllPass}
    return bool_AllPass, _cDctRes