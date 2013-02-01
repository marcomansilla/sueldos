# -*- coding: utf-8 -*-

def reload(target):
    def js(form):
        response.js = 'web2py_component("%s","%s")' % (URL(target),target)
                
    return js

def personal():
    form = SQLFORM.grid(db.empleados, ui='jquery-ui', user_signature=False)
    return dict(form=form)

def escalas():

    nueva=SQLFORM(db.categorias)

    if nueva.process().accepted:
        response.flash='La categoria ha sido agregada'
    elif nueva.errors:
        response.flash='El formulario tiene errores'

    lista=db(db.categorias.gremio==request.vars.id).select()
    
    return dict(lista=lista, nueva=nueva)


def importes():
    
    nuevo=SQLFORM(db.valores)

    if nuevo.process().accepted:
        response.flash='Aceptado'
    elif nuevo.errors:
        response.flash='Errores'

    lista=db(db.valores.gremio==request.vars.id).select()
        
    return dict(listado=lista, nuevo=nuevo)



