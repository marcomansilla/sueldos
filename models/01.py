# -*- coding:utf-8 -*-

#Clase para verificar los numeros de cuil/cuit... para salir de lo comun con la X le puse S xDasdfg
class IS_CUIS(object):

    def __init__(self, error_message="El numero ingresado no es valido"):
        self.error_message=error_message

    def __call__(self, value):
        self.valor=value
        self.CONSTANTES=[5,4,3,2,7,6,5,4,3,2]
        try:
                self.parametros=self.valor.split('-')
                self.aux=self.parametros[0]+self.parametros[1]
                self.valor1=0
                x=0
                for i in self.aux:
                        self.valor1=self.valor1+(int(i)*self.CONSTANTES[x])
                        x+=1
            
                self.valor2=self.valor1%11

                if (11-self.valor2)!=int(self.parametros[2]):
                        return (self.valor, self.error_message)
        except Exception:
                self.error_message='El valor tiene que tener el formato XX-YYYYYYY-Z'
                return (self.valor, self.error_message)
        return (self.valor, None)


#Validador de actividades para los empleadores
class IS_ACTIVITY(object):
    def __init__(self, error_message="El numero ingresado no es valido", sep=","):
        self.error_message=error_message
        self.sep=sep
        
    def __call__(self, value):
       self.valores=value

       for valor in self.valores:
            valor=int(valor.strip())
            if IS_NOT_IN_DB(db, db.actividades.codigo)(valor)[1] != None:
                return (self.valores, self.error_message)
       return (self.valores, None)
