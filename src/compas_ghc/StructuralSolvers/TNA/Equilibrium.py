from compas_ghc.DataStructures.CGHDiagrams import CGHFormDiagram as FormDiagram
from compas_ghc.DataStructures.CGHDiagrams import CGHForceDiagram as ForceDiagram
from compas_tna.equilibrium import horizontal_nodal
from compas_tna.equilibrium import vertical_from_zmax

from copy import deepcopy

__all__ = [
    'HorizontalEquilibrium_fromData',
    'VerticalEquilibrium_fromZMax_fromData'
]
FormDiagram()
def VerticalEquilibrium_fromZMax_fromData (formdata, zmax, kmax=100): # *args, **kwargs
    form = FormDiagram.from_data(deepcopy(formdata))
    scale = vertical_from_zmax(form, zmax, kmax)
    return form.to_data(), scale;


def HorizontalEquilibrium_fromData (formdata, forcedata, alpha = 100, kmax = 100): # *args, **kwargs
    form = FormDiagram.from_data(deepcopy(formdata))
    force = ForceDiagram.from_data(deepcopy(forcedata))

    horizontal_nodal (form, force, alpha, kmax)

    formdata, forcedata = form.to_data(), force.to_data()

    return formdata, forcedata

# from compas_kmmt.utilities.CodeTimer.CodeTimer import CodeTimer
# from compas_tna.equilibrium import vertical_from_zmax_rhino
# codeTm.Mark('diagram from data')
# codeTm.Mark('parallelisation')
# f = XFunc('compas_tna.equilibrium.horizontal_nodal_xfunc', tmpdir=compas_tna.TEMP, callback=callback)
# codeTm.Mark('diagram to data')