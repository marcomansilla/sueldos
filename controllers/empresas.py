#-*- coding: utf-8 -*-

def nuevoempleador():
    form = SQLFORM(db.empleadores)

    if form.process().accepted:
        redirect(URL('default','clientes'))
        response.flash='El cliente ha sido agregado exitosamente'
    elif form.errors:
        response.flash='El formulario tiene errores'
    else:
        response.flash='Por favor complete los datos del empleador'
        
    return dict(form=form)

def convenios():

    nueva=SQLFORM(db.convenios)
    if nueva.process().accepted:
        response.flash='Agregado el convenio'
    elif nueva.errors:
        response.flash='Algo anda mal'
         
    return dict(nueva=nueva)
