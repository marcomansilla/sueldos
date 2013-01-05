#-*- coding: utf-8 -*-



db.define_table('sindicatos',
    Field('nombre')
    )

db.define_table('categorias',
    Field('sindicato', db.sindicatos),
    Field('nombre')
    )

db.define_table('clases',
    Field('categoria', db.categorias),
    Field('Tipo','string', length=1)
    )

db.define_table('antiguedad',
    Field('nombre')
    )
