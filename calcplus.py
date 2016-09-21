#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":
    calculadora = calcoohija.CalculadoraHija()

    fich = open(sys.argv[1], 'r')

    lineas = fich.readlines()

    for linea in lineas:
        elementos = linea.split(',')

        resultado = int(elementos[1])
        operacion = elementos[0]
        elementos = elementos[2:]

        for operandos in elementos:

            if operacion == "suma":
                resultado = calculadora.suma(resultado, int(operandos))
            elif operacion == "resta":
                resultado = calculadora.resta(resultado, int(operandos))
            elif operacion == "multiplica":
                resultado = calculadora.multiplicar(resultado, int(operandos))
            elif operacion == "divide":
                resultado = calculadora.dividir(resultado, int(operandos))
            else:
                sys.exit('Operación sólo puede ser suma, resta, mutiplica'
                         'y divide.')

        print(resultado)
