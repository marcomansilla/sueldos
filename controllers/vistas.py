# -*- coding: utf-8 -*-

def personal():
    form = SQLFORM.grid(db.empleados, ui='jquery-ui', user_signature=False)
    return dict(form=form)
