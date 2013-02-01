# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

def index():
    response.flash = T("Sistema listo y funcional!")
    return dict()       

def clientes():
    # Nueva anotacion
    form=SQLFORM(db.notas)
    if form.process().accepted:
        redirect(URL('default','clientes'))
        response.flash='Su nota ha sido agendada'
    elif form.errors:
        response.flash='Por favor revise el formulario'

    # nuevo empleador
    nuevo=SQLFORM(db.empleadores)
    if nuevo.process().accepted:
        session.flash='Se ha agregado el nuevo cliente'
    elif nuevo.errors:
        session.flash='El formulario tiene errores'

    # Nuevo convenio por cada empleador
    convenionuevo=SQLFORM(db.convenios)
    if convenionuevo.process().accepted:
        session.flash='El convenio ha sido agregado'
    elif convenionuevo.errors:
        session.flash='El formulario tiene errores'
    
    anotaciones=db(db.notas.id>0).select(limitby=(0,5), orderby=~db.notas.fecha)
    lista=db(db.empleadores.id>0).select()
    return dict(nota=form, anotaciones=anotaciones, lista=lista, nuevo=nuevo, convenionuevo=convenionuevo)

def convenios():
    nuevo=SQLFORM(db.gremios)

    if nuevo.process().accepted:
        redirect(URL('default','convenios'))
        response.flash='Se ha agregado el nuevo gremio'
    elif nuevo.errors:
        response.flash='El formulario tiene errores'

    listado=db().select(db.gremios.ALL)
    return dict(listado=listado, nuevo=nuevo )

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
