from scripts import RE_module

# RE_module.patrones_basicos()
RE_module.resume_regex()

def test_search():
    #RE:SEARCH
    string = "an example word:maw!!"
    pat = r'word:\w\w\w' # Busca por el patrón 'word:' seguido de tres letras - 
                        # Se considera neceseario la r delante para enviar la string como "raw", 
                        # para tener en cuenta los valores especiales y con barras invertidas 
    RE_module.search(pat, string)

    # Usando re.seach se almacena los resultados en una variable. Si no hubiera resultados, se devolvería None de forma que se obtendría resultado False -  No existe.

