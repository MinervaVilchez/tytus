import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class Sind(Instruccion):
    def __init__(self, valor, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.DOUBLE_PRECISION),linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función sind("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        try:
            if resultado % 90 == 0:
                return (0, 1, 0, -1)[int(resultado // 90) % 4]
            else:
                return math.sin(math.radians(resultado))
        except ValueError as c:
            error = Excepcion('22003',"Semántico","La entrada está fuera de rango",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error