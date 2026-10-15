#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________
# Tipos de Datos Primitivos

# Python es un lenguaje de tipado dinámico y fuertemente tipado. Esto significa que no necesitas 
# declarar el tipo de una variable explícitamente, pero el intérprete no realizará conversiones 
# implícitas de tipos incompatibles (por ejemplo, sumar un entero con un texto lanzará un error).
#__________________________________________________________________________________________________________________

# 1. int (Enteros)
# Representan números enteros sin parte decimal, positivos o negativos. En Python 3, los enteros tienen 
# precisión arbitraria; su tamaño solo está limitado por la memoria disponible en el sistema.

edad = 25
poblacion = 8_000_000_000 # Los guiones bajos mejoran la legibilidad y son ignorados por Python

# Pregunta: ¿Cómo se almacenan los enteros en python para que exista la posiblidad de poner un entero 
# de 100 o hasta 1000 dígitos?

#__________________________________________________________________________________________________________________

# 2. float (Punto Flotante)
# Representan números reales con parte decimal. Internamente implementan el estándar IEEE 754 de 
# doble precisión (64 bits).

pi = 3.14159
notacion_cientifica = 2.5e-3  # Equivale a 0.0025

#__________________________________________________________________________________________________________________

# 3. complex (Números Complejos)
# Tienen una parte real y una parte imaginaria. La parte imaginaria se indica con el sufijo j o J.

z = 3 + 4j
print(z.real)  # 3.0 (devuelve float)
print(z.imag)  # 4.0 (devuelve float)

#__________________________________________________________________________________________________________________

# 4. bool (Booleanos)
# Representan valores de verdad: True o False. La clase bool es una subclase de int, donde True 
# equivale numéricamente a 1 y False a 0.

es_valido = True
es_mayor = False

# Comportamiento numérico subyacente:
print(True + True)  # Imprime 2

#__________________________________________________________________________________________________________________

# 5. str (Cadenas de Texto)
# Secuencias inmutables de caracteres Unicode. Se pueden delimitar con comillas simples ('), 
# dobles (") o triples (''' / """) para cadenas multilínea.

nombre = "Python"
multiline = """Línea 1
Línea 2"""

#__________________________________________________________________________________________________________________

# 6. bytes (Secuencia de Bytes)
# Secuencia inmutable de enteros en el rango 0 <= x <256. Se utilizan para manejar datos binarios 
# (imágenes, archivos, red).

datos_binarios = b"Hola"  # Prefijo 'b'
print(datos_binarios[0])  # Imprime 72 (código ASCII de 'H')

#__________________________________________________________________________________________________________________

# 7. NoneType (None)
# Tipo especial que posee un único valor posible: None. Se utiliza para representar la ausencia explícita 
# de un valor o el valor por defecto que retornan las funciones que no ejecutan un return explícito. Es un 
# objeto singleton (solo existe una instancia en memoria).

resultado = None

#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________