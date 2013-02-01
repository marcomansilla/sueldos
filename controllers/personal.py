#-*- coding: utf-8 -*-

def nuevopersonal():
    
    form = SQLFORM(db.empleados)

    if form.process().accepted:
        response.flash='El empleado a sido agregado'
    elif form.errors:
        response.flash='El formulario tiene errores'
    else:
        response.flash='Por favor complete los datos del empleado'

    return dict(form=form)
