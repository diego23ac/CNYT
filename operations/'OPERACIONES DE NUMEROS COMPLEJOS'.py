'OPERACIONES_DE_NUMEROS_COMPLEJOS'

import math

def suma(a,b):
    pr = (a[0] + b[0])
    pi = (a[1] + b[1])
    return (pr,pi)

def resta(a,b):
    pr = (a[0] - b[0])
    pi = (a[1] - b[1])
    return (pr,pi)

def multiplicacion(a,b):
    pr = (a[0]*b[0] - a[1]*b[1])
    pi = (a[0]*b[1] + a[1]*b[0])
    return (pr,pi)

def division(a,b):
    if b[0] == 0 and b[1] == 0:
        return "el divisor debe ser difererente de 0"
    pr = ((a[0]*b[0] + a[1]*b[1])//(b[0]**2 + b[1]**2))
    pi = ((a[1]*b[0] + a[0]*b[1])//(b[0]**2 + b[1]**2))
    return (pr,pi)

def modulo(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def conjugado(a):
    return (a[0],a[1]*-1)

def phase(a):
    if a[1] == 0:
        if a[0] > 0:
            angulo = 0
        elif a[0] < 0:
            angulo = math.pi
        else:
            return "el divisor debe ser difererente de 0"
    elif a[0] == 0:
        angulo = math.pi/2 if a[1] > 0 else -math.pi/2
    else:
        angulo = round(math.atan(a[1]/a[0]))
    return angulo


def cartesian_polar(a):
    pr = round(modulo(a))
    pi = round(phase(a))
    return pr, pi


def polar_cartesian(a):
    pr = round(a[0]*math.cos(a[1]))
    pi = round(a[0]*math.sin(a[1]))
    return (pr, pi)