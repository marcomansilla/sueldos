#-*- coding: utf-8 -*-

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
    Field('convenio'),
    Field('tdoc',label='Tipo de documento', requires=IS_IN_SET(TIPO_DOCUMENTO)),
    Field('ndoc',label='Numero de documento')
    )

db.empleados.id.readable=True
db.empleados.legajo.default=default=db(db.empleados.id>0).count()+1
db.empleados.legajo.unique=True
db.empleados.legajo.writable=False
#db.empleados.convenio.requires=IS_IN_SET([db(db.empleadores.id==request.vars.id).select(db.empleadores.convenios)])
#db.empleados.convenio.requires=IS_IN_DB(db, db.empleadores.convenios)
