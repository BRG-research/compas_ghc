


from compas_tna.diagrams import FormDiagram
from compas_tna.diagrams import ForceDiagram
from compas_tna.equilibrium import horizontal_nodal_rhino 
from compas_tna.equilibrium import vertical_from_zmax_rhino

__all__ = [
    'test_func',
    'horizontal_nodal_rpc',
]

def test_func():
	print ("hello world")
	return str("hello world")
	pass

def horizontal_nodal_rpc (formdata, forcedata, alpha = 100, kmax = 100, *args, **kwargs):
    import compas_rhino
    def callback(line, args):
        print(line)
        compas_rhino.wait()

    form = FormDiagram.from_data(formdata)
    force = ForceDiagram.from_data(formdata)
    horizontal_nodal (form, force, alpha, kmax)
    # f = XFunc('compas_tna.equilibrium.horizontal_nodal_xfunc', tmpdir=compas_tna.TEMP, callback=callback)
    formdata, forcedata = form.to_data(), force.to_data()
    return formdata, forcedata