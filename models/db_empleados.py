#-*- coding: utf-8 -*-

db.define_table('convenios',
    Field('empleador',db.empleadores, default=request.vars.id),
    Field('convenio', db.gremios)
    )

from plugin_lazy_options_widget import lazy_options_widget

db.define_table('empleados',
    Field('empleador', db.empleadores, default=request.vars.id),
    Field('legajo',label='Nro. de legajo', readable=True),
    Field('apaterno',label='Apellido paterno'),
    Field('amaterno',label='Apellido materno'),
    Field('nombre',label='Nombre/s'),
    Field('cuil',label='C.U.I.L', requires=[IS_NOT_EMPTY(), IS_CUIS()]),
    Field('nacionalidad'),
    Field('ecivil',label='Estado civil', requires=IS_IN_SET(ESTADO_CIVIL)),
    Field('fnac',label='Fecha de nacimiento'),
    Field('domicilio'),
    Field('convenio',comment="<-- Seleccione el convenio"),
    Field('tdoc',label='Tipo de documento', requires=IS_IN_SET(TIPO_DOCUMENTO)),
    Field('ndoc',label='Numero de documento'),
    format = '%(cuil)s'
    )

cascade = CascadingSelect(db.empleadores,db.convenios,db.categorias)
db.empleados.convenio.widget=cascade.widget

# db.empleados.categoria.widget = lazy_options_widget(
#     'empleados_convenio__selected', 'empleado_convenio__unselected',
#     lambda categoria_id: (db.empleados.categoria == categoria_id),
#     request.vars.gremio,
#     orderby=db.empleados.id,
#     # user_signature=True,
#     # If you want to process ajax requests at the time of the object construction (not at the form rendered),
#     # specify your target field in the following:
#     field=db.empleados.categoria,
#     )

db.empleados.id.readable=True
db.empleados.legajo.default=db(db.empleados.id>0).count()+1
db.empleados.legajo.unique=True
db.empleados.legajo.writable=False
#db.empleados.convenio.requires=IS_IN_SET([db(db.convenios.empleador==request.vars.id).select()])
#db.empleados.convenio.requires=IS_IN_DB(db, db.empleadores.convenios)
