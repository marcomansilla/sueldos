#-*- coding: utf-8 -*-

def listarconvenios():
    lista = db(db.gremios.id>0).select()

    nuevo=SQLFORM(db.gremios)

    if nuevo.process().accepted:
        redirect(URL('default','convenios'))
        response.flash='Se ha agregado el nuevo gremio'
    elif nuevo.errors:
        response.flash='El formulario tiene errores'
    
    return dict(lista=lista, nuevo=nuevo )

def listarclientes():
    

    return dict()

def jornadas():
    lista = db(db.jornadas.id>0).select()

    nuevo=SQLFORM(db.jornadas)

    if nuevo.process().accepted:
        redirect(URL('gestion','jornadas'))
        response.flash='Se ha agregado el registro'
    elif nuevo.errors:
        response.flash='El formulario tiene errores'
    return dict(lista=lista, nuevo=nuevo)

def nomina():
    db.empleados.convenio.requires=IS_EMPTY_OR(IS_IN_DB(db((db.convenios.empleador==request.vars.id)&(db.gremios.id==db.convenios.convenio)), 'gremios.rubro', zero='-----'))
    personal=db(db.empleados.empleador==request.vars.eid).select()
    nuevo=SQLFORM(db.empleados)

    if nuevo.process().accepted:
        response.flash='Empleado agregado exitosamente'
    elif nuevo.errors:
        response.flash='El formulario tiene errores'

    return dict(personal=personal, nuevo=nuevo, categoria=SQLTABLE(db(db.categorias.id > 0)(db.categorias.gremio == db.gremios.id).select(db.gremios.id, db.gremios.rubro, db.categorias.nombre)))

def convenios():
    
    return CAT(*[OPTIONS(t.name) for t in db(db.convenios.convenio_id==db.gremios(request.vars.id)).select()])
