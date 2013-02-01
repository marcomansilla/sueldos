#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata 

def elimina_tildes(cadena):
    # http://guimi.net
    # Cambiamos caracteres modificados (áüç...) por los caracteres base (auc...)
    # Basado en una función de Miguel en
    # http://www.leccionespracticas.com/uncategorized/eliminar-tildes-con-python-solucionado/
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

f=open('prueba3.csv', 'rw')

for line in f:
    print unicodedata.normalize('NFKD', line.decode('unicode-escape')).encode('ASCII', 'ignore').lower()

f.close()
