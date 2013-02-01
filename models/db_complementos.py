#-*- coding: utf-8 -*-


db.define_table('gremios',
    Field('rubro'),
    Field('sindicato'),
    Field('web'),
    format='%(sindicato)s'
    )

db.define_table('categorias',
    Field('gremio', db.gremios, default=request.vars.id),
    Field('nombre'),
    Field('basico')
    )

db.define_table('jornadas',
    Field('nombre'),
    Field('horas','integer'),
    Field('descripcion','text'),
    format = '%(nombre)s'
    )
db.define_table('antiguedad',
    Field('nombre')
    )

## Validadores en orden de tablas declaradas

db.gremios.rubro.requires=IS_NOT_EMPTY()
db.gremios.sindicato.requires=IS_NOT_EMPTY()
db.gremios.web.requires=IS_URL()
