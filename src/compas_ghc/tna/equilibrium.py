

from compas_tna.diagrams import FormDiagram
from compas_tna.diagrams import ForceDiagram
from compas_tna.equilibrium import horizontal_nodal_rhino 
from compas_tna.equilibrium import vertical_from_zmax_rhino

def test():
	pass
# def horizontal_nodal_rhino(form, force, *args, **kwargs):
#     import compas_rhino
#     def callback(line, args):
#         print(line)
#         compas_rhino.wait()
#     f = XFunc('compas_tna.equilibrium.horizontal_nodal_xfunc', tmpdir=compas_tna.TEMP, callback=callback)
#     formdata, forcedata = f(form.to_data(), force.to_data(), *args, **kwargs)
#     form.data = formdata
#     force.data = forcedata