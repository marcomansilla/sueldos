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
