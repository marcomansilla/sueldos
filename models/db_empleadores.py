#-*- coding: utf-8 -*-
#Tablas relacionadas con los empleadores

from plugin_multiselect_widget import (
    hmultiselect_widget, vmultiselect_widget,
    rhmultiselect_widget, rvmultiselect_widget,
    )
  

db.define_table('actividades',
    Field('codigo'),
    Field('nombre'),
    Field('detalle','text'),
    Field('comentario','text'),
    format = '%(nombre)s'
    )

db.define_table('empleadores',
    Field('nombre', 'string', label='Nombre o razón social'),
    Field('cuit',label='C.U.I.T',requires=[IS_NOT_EMPTY(),IS_CUIS()], comment='Debe tener la forma 11-22222222-4'),
    Field('domicilio', label='Domicilio legal'),
    Field('provincia', requires=IS_IN_SET(PROVINCIA)),
    Field('localidad'),
    Field('cp', label='Codigo postal'),
    # Field('cactividad', 'list:integer',requires=[IS_IN_DB(db, db.actividades.codigo)], label='Codigo de actividad'),
    # Field('nactividad',label='Nombre de actividad'),
    Field('telefono'),
    Field('email', requires=IS_EMAIL(), label='E-Mail'),
    # Field('convenios', requires=(IS_IN_DB(db, db.gremios.sindicato, multiple=True)))
    )

#db.empleadores.convenios.widget=hmultiselect_widget

# db.empleadores.nactividad.widget=SQLFORM.widgets.autocomplete(request, db.actividades.nombre, limitby=(0,10), min_length=2)
# db.empleadores.cactividad.widget=SQLFORM.widgets.autocomplete(request, db.actividades.codigo, limitby=(0,10), min_length=2)


db.define_table('notas',
    Field('nota', 'text'),
    Field('fecha','date', default=request.now, writable=False),
    )

