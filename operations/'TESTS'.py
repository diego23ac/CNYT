'TESTS'

import OPERACIONES_DE_NUMEROS_COMPLEJOS as lc
#SUMA
# Caso 1:
a = (3, 4)
b = (1, 2)
resultado = suma(a, b)
# Resultado esperado: (4, 6)

# Caso 2:
a = (-2, 3)
b = (5, -1)
resultado = suma(a, b)
# Resultado esperado: (3, 2)

# Caso 1:
a = (3, 4)
b = (1, 2)
resultado = resta(a, b)
# Resultado esperado: (2, 2)

# Caso 2:
a = (-2, 3)
b = (5, -1)
resultado = resta(a, b)
# Resultado esperado: (-7, 4)

# Caso 1:
a = (3, 4)
b = (1, 2)
resultado = multiplicacion(a, b)
# Resultado esperado: (-5, 10)

# Caso 2:
a = (-2, 3)
b = (5, -1)
resultado = multiplicacion(a, b)
# Resultado esperado: (-7, 17)

# Caso 1:
a = (3, 4)
b = (1, 2)
resultado = division(a, b)
# Resultado esperado: (2, 0)

# Caso 2:
a = (5, -1)
b = (-2, 3)
resultado = division(a, b)
# Resultado esperado: (-1, -2)

# Caso 1:
a = (3, 4)
resultado = modulo(a)
# Resultado esperado: 5.0

# Caso 2:
a = (-2, -3)
resultado = modulo(a)
# Resultado esperado: 3.605551275463989

# Caso 1:
a = (3, 4)
resultado = conjugado(a)
# Resultado esperado: (3, -4)

# Caso 2:
a = (-2, 3)
resultado = conjugado(a)
# Resultado esperado: (-2, -3)

# Caso 1:
a = (1, 1)
resultado = phase(a)
# Resultado esperado: 1 (equivalente a 45 grados o π/4 radianes)

# Caso 2:
a = (-1, 1)
resultado = phase(a)
# Resultado esperado: 2 (equivalente a 135 grados o 3π/4 radianes)

# Caso 1:
a = (1, 1)
resultado = cartesian_polar(a)
# Resultado esperado: (1, 1)  # Módulo: √2 ≈ 1.41 (redondeado a 1), Ángulo: 45° o π/4

# Caso 2:
a = (-1, 1)
resultado = cartesian_polar(a)
# Resultado esperado: (1, 2)  # Módulo: √2 ≈ 1.41 (redondeado a 1), Ángulo: 135° o 3π/4

# Caso 1:
a = (1, 1)  # (módulo, ángulo)
resultado = polar_cartesian(a)
# Resultado esperado: (1, 0)  # Aproximadamente (0.54, 0.84), redondeado a (1, 0)

# Caso 2:
a = (1, 2)  # (módulo, ángulo)
resultado = polar_cartesian(a)
# Resultado esperado: (-1, 0)  # Aproximadamente (-0.42, 0.91), redondeado a (-1, 0)
