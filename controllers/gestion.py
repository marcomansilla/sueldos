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
    personal=db(db.empleados.empleador==request.vars.id).select()
    nuevo=SQLFORM(db.empleados)

    if nuevo.process().accepted:
        response.flash='Empleado agregado exitosamente'
    elif nuevo.errors:
        response.flash='El formulario tiene errores'

    return dict(personal=personal, nuevo=nuevo)
