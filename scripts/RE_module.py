#doc: https://docs.python.org/es/3/library/re.html
#     https://www.w3schools.com/python/python_regex.asp
#     https://developers.google.com/edu/python/regular-expressions
#     https://regexr.com/
#     https://www.py4e.com/lessons/regex


#Se utiliza e módulo re
from .utils import *
import re

def search(pat, str):
    match = re.search(pat, str)
    if match:
        print("Found", match.group())
    else:
        print("Nope :(")

def patrones_basicos():
    # El poder de las expresiones iregulares es que se puede especificar patrones con ellas.
    # Patrones básicos que coinciden con un carácter
    printing("a, X, 9", """Carácteres que solo coinciden con ellos mismos.
        Hay metacaracteres que no coinciden con si mismos ya que tienen significados especiales.
        Como: . ^ $ * + ? { [ ] \ | ( )""")
    printing(".", "Coincide cualuier carácter excepto en de salto de línea '\\n'")
    printing("\w", """w en minúscula - Coincide con un carácter (carácter palabra) que sea una letra o dígito o barra baja [a-zA-Z0-9_] 
        - Es para coincidir con un único caracter y no con una palabra. 
        \W (En mayúscula) - corresponde con los carácteres que no son los recogidos por la opción con w minúscula.""")

    print(re.search(r'\w\w', "h-ii"))
    print(re.search(r'\W', "h-i"))
    printing("\\b", """Coincide con la cadena vacía, pero sólo al princpio o al final de la palabra - 
        Es decir, el \\b limita el inicio y fin de la palabra en cuanto a la existencia de caracteres 
        considerados "palabra" indicados anteriormente ( [a-zA-Z0-9_] ).
        Por tanto (foo) es válido, pero foo3 no.""")
    print(re.search(r'\bfoo\b', "foo"))
    print(re.search(r'\bfoo\b', "(foo)"))
    print(re.search(r'\bfoo\b', "foo."))
    print(re.search(r'\bfoo\b', "croqueta foo de"))
    print(re.search(r'\bfoo\b', "foo66"))
    printing("\\s", """Coincide con un caracter en blanco (espacio, linea nueva, retorno de carro, 
    tab, form [  \\n \\r \\t \\f]).
    En el caso de \\S (mayúscula) coincide con cualquier caracter no en blanco.
        """)
    str_aux =  "Co\nsota"
    print(f"String: '{str_aux}'")
    print("\t", re.search(r'\s', str_aux))
    print("\t", re.search(r'\S', str_aux))
    printing("\\d", """Dígitos [0-9]""")
    printing("^", "Inicio - Coincide con el inicio de la string")
    printing("$", "Fin - Coincide con el final de la string")
    printing("\\", "Evita que sea un caracter especial, como en del punto: \\. La barra \\\.")
    printing("REPETICIONES","")
    printing("+", "Una o más repeticiones del token anterior")
    printing("*", "cero o más repeticiones del token anterior")
    printing("?", "Cero o una repeticiones del token anterior - haciéndolo opcional")

    str_aux = "Evee"
    print(re.search(r"e+", str_aux))
    print(re.search(r"\we*", str_aux))
    print(re.search(r"\wx?e", str_aux))
    print(re.search(r"\wv?e", str_aux))

def ejemplos_de_repeticiones():
     ## i+ = one or more i's, as many as possible.
    match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"
    printing("pi+, busca una o más i", match)

    ## Finds the first/leftmost solution, and within it drives the +
    ## as far as possible (aka 'leftmost and largest').
    ## In this example, note that it does not get to the second set of i's.
    match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"
    printing("i+, encuentra la primera coincidencia más a la izquierda", match)

    ## \s* = zero or more whitespace chars
    ## Here look for 3 digits, possibly separated by whitespace.
    match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
    printing("\\s* cero o más carácteres en blanco", match)
    match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
    printing("",match)
    match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"
    printing("",match)

    ## ^ = matches the start of string, so this fails:
    match = re.search(r'^b\w+', 'foobar') # not found, match == None
    # match = re.search(r'^f\w+', 'foobar') # not found, match == None
    printing("^ Coincide con el inicio de string, es decir, la 'b' tiene que ser al principio. [^b\w+]", match)
    ## but without the ^ it succeeds:
    match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"
    printing("Encuentra la b y de ella en adelante, [b\w+]", match)
    match = re.search(r'\w+r$', "perra, perror")
    printing("Palabra terminada por r", match)

def corchetes():
    email = "croqueta beatrix@croquetasalvaje.com dididh"
    printing("CORCHETES", "")
    printing("Corchetes", """Con los corchetes se pueden indicar una serie de carácteres que se pueden usar. 
    Los carácteres especiales como \\w, \\s funcionan también excepto el punto (.), que 
    en este caso sería un punto literal.
    Para el caso de los emails se utiliza: [\w.-]+@[\w.-]+""")
    match = re.search(r"[\w.-]+@[\w.-]+", email)
    if match:
        print(match.group())
    
    printing("Rangos:", """De la a a la z en minúsculas: [a-z] / En mayúsculas: [A-Z] / Ambos: [a-zA-Z] """)
    printing("Indicar solo algunos carácteres","[abc-]")
    str_aux = "Croquetilla - salvabje "
    match = re.search(r"[abc-]", str_aux)
    print(match)
    printing("Indicar solo algunos carácteres que no","[^abc-]")
    match = re.search(r"[^abc-]", str_aux)
    print(match)

def group_extraction():
    email = "croqueta beatrix@croquetasalvaje.com dididh"
    match = re.search(r"([\w.-]+)@([\w.-]+)", email)
    printing("Función de grupo", """La función de grupo permite obtener las partes 
    del texto que coincide. En el caso del email, la primera parte antes del @ y la segunda parte
    después.
    Esto se consigue con el siguiente patrón: r'([\w.-]+)@([\w.-]+)'
    En una búsqueda satisfactoria, se obtendría:
        > Completo:     match.group()
        > Izquierda:    match.group(1)
        > Derecha:      match.group(2)
    """)
    printing("GROUP COMPLETO", match.group())
    printing("GROUP PARTE IZQUIERDA", match.group(1))
    printing("GROUP PARTE DERECHA", match.group(2))
    
def email():
    printing("ENCONTRAR EMAIL DENTRO DE UNA STRING", "")
    email = "croqueta beatrix@croquetasalvaje.com dididh"
    pattern = r'\w+@\w+.\w+'
    match = re.search(pattern, email)
    print(match)

def findall():
    printing("findall", """ con re.search() se obtiene el primer match para el matrón. 
    Con findall se encuentran todas las coincidencias y las devuelve como una lista de strings.    
    """)

    str_aux = "croqueta beatrix@croqueta.com zzzz asdf azrael@hh.es dantalion@hh.com bye zzzz luci@luci.com"
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', str_aux)
    print(emails)

    printing("findall con archivos", """También se puede utilizar con archivos:
    # Abre el archivo
    f = open('test.txt', 'r')
    # Usa f.read en el findall usando uno patrón, de forma que se obtienen todos los emails en este caso
    strings = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
    """)

    printing("finall con grupos", """Al igual search, se puede obtener la funcionalidad del group.
    Pero en este caso viene en forma de tupla, de forma que:
    str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
    tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
    print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
    for tuple in tuples:
        print(tuple[0])  ## username
        print(tuple[1])  ## host
    """)

    emails = re.findall(r'([\w\.-]+)@([\w\.-]+)', str_aux)
    printing("emails", emails) 
    for email in emails:
        print("username:", email[0])  ## username
        print("host:", email[1])  ## host

def options():
    printing("OPTIONS", """Las funciones del módulo re tienen un argumento extra que puede ser:
    re.IGNORECASE: ignora upper/lowercase para el matching.
    re.DOTALL: Permite el punto (.) para la coincidencia de una nueva línea. 
    re.MULTILINE: Con una string con multilinea, permite ^ y $ para el inicio y el fin con el inicio
    y fin de cada línea, ya que normalmente coincidiría con la string completa.

    re.search(pat, str, re.IGNORECASE)
    """)

def sustitucion():
    printing("SUBSTITUTION", """ La función re.sub(pat, repacement, str) busca todas
    las coincidencias del patrón en la string dada y las replaza por el valor indicado.
    Se puede usar la función de grupo para sustituir una de las partes.
    \\1 para sustituir el grupo 1 \\2 para sustituir el grupo 2
    """)

    str_aux = "croqueta beatrix@croqueta.com zzzz asdf azrael@hh.es dantalion@hh.com bye zzzz luci@luci.com"
    resultado = re.sub(r'([\w\.-]+@[\w\.-]+)', r'\1@croquetillas.net', str_aux)
    print(resultado)

def resume_regex():
    print("""
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
    """)