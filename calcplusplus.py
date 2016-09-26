#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__ == "__main__":
    calculadora = calcoohija.CalculadoraHija()

    with open(sys.argv[1], newline='\n') as f:
        lineas = csv.reader(f)
        for linea in lineas:
            resultado = int(linea[1])
            operacion = linea[0]
            elementos = linea[2:]

            for operandos in elementos:

                if operacion == "suma":
                    resultado = calculadora.suma(resultado, int(operandos))
                elif operacion == "resta":
                    resultado = calculadora.resta(resultado, int(operandos))
                elif operacion == "multiplica":
                    resultado = calculadora.multiplicar(resultado,
                                                        int(operandos))
                elif operacion == "divide":
                    resultado = calculadora.dividir(resultado, int(operandos))
                else:
                    sys.exit('Operación sólo puede ser suma, resta, mutiplica'
                             'y divide.')

            print(resultado)
