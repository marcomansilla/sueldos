#-*- coding: utf-8 -*-
#Tablas relacionadas con los empleadores

db.define_table('actividades',
    Field('codigo', 'integer'),
    Field('nombre'),
    Field('detalle','text'),
    format = '%(nombre)s'
    )

db.define_table('empleadores',
    Field('nombre', 'string', label='Nombre o razón social'),
    Field('cuit',label='C.U.I.T',requires=[IS_NOT_EMPTY(),IS_CUIS()]),
    Field('domicilio', label='Domicilio legal'),
    Field('provincia', requires=IS_IN_SET(PROVINCIA)),
    Field('localidad'),
    Field('cp', label='Codigo postal'),
    Field('cactividad','list:integer',requires=IS_ACTIVITY(), label='Codigo de actividad'),
    Field('nactividad', label='Nombre de actividad', requires=IS_IN_SET(db.actividades)),
    Field('telefono'),
    Field('email')
    )


