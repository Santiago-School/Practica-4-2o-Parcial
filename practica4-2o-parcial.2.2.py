print("Francisco Santiago Carrasco Correa 0421 3°W")
print(" ")

# se crea un diccionario vacio para las traducciones
diccionario = {}

# se pide al usuario que ingrese las traducciones
entradas = input("ingresa las traducciones en formato palabra:traduccion, separados por comas: ")

# se procesa cada entrada y se añade al diccionario
for entrada in entradas.split(","):
    # se separa la palabra y la traduccion
    if ":" in entrada:
        palabra, traduccion = entrada.split(":")
        diccionario[palabra.strip()] = traduccion.strip()

# se imprime el diccionario de traduccion
print("diccionario de traduccion:", diccionario)

# se pide una frase en español para traducir
frase = input("ingresa una frase en español: ")

# se traduce la frase palabra por palabra
frasetraducida = []
for palabra in frase.split():
    # se busca la traduccion en el diccionario
    traduccion = diccionario.get(palabra, palabra)  # si no se encuentra, se deja la palabra sin traducir
    frasetraducida.append(traduccion)

# se imprime la frase traducida
print("frase traducida:", " ".join(frasetraducida))
