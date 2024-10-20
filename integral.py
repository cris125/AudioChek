def calcular_integral(edad_inicial, edad_final, frecuencia_inicial, frecuencia_final):
    termino_inicial = ((16.58 * frecuencia_final**2) - (16.58 * frecuencia_inicial**2)) / 2
    funcion = (1 / ((20.761 - (0.1658 * edad_final)) * 0.1658)) - (1 / ((20.761 - (0.1658 * edad_inicial)) * 0.1658))
    
    print(funcion)
    print(termino_inicial)
    
    resultado = (termino_inicial * funcion) / ((edad_final - edad_inicial) * (frecuencia_final - frecuencia_inicial))
    return resultado

print(calcular_integral(45, 50, 19.9, 20))
