# Apertura
import re
file = open('spanishwords.txt', encoding="utf-8")

# Procesa la base de datos de palabras
dictionary = dict()
for line in file:
    word = line.rstrip()
    extention = len(word)
    dictionary[word] = dictionary.get(word, extention)

    # Tranforma el diccionario en una lista y la ordena de mayor a menor
lista = list()
for word, extention in dictionary.items():
    newtupple = (extention, word)
    lista.append(newtupple)
lista = sorted(lista, reverse = True)

    # Elimina la extension de cada palabra de la lista y hace una lista de solo palabras
lis = list()
for extention, word in lista:
    newtupple = (word)
    lis.append(newtupple)

# Separa las palabras
while True:
    string = 0
    string = str()
    dictionary = 0
    dictionary = dict()
    word = str()
    number = 0
    terminos = list()
    positionofstartfind = 1
    string = str()
    li = list()
    listafinal = list()
    text = input('\n\nHola! Este programa le permitira separar palabras unidas de una cadena de texto. Simplemente pegue el texto aqui y luego copie el resultado que le genere. Ingrese Exit para salir del programa.\n\nIngrese el texto a separar:\n').lower()
    if text == 'Exit' or text == 'exit' or text == 'cls': break
    for terminodebusqueda in lis:
        id = 0
        id = text.find(str(terminodebusqueda))  # Id del primer resultado, sino busca el inicio de la cadena y lo asigna como Id de la palabra en la cadena
        if id == -1: continue   # Si no hay termino, continuar
        numberofappearances = text.count(terminodebusqueda) # Codigo para cuando aparece una palabra varias veces en el texto
        terminoplusspace = terminodebusqueda + ' '
        if numberofappearances == 1:
            dictionary[id] = dictionary.get(id, terminoplusspace)
        else:
            while number <= numberofappearances:
                id = text.find(str(terminodebusqueda), id, 99999)
                dictionary[id] = dictionary.get(id, terminoplusspace)
                id = id + 1
                number = number + 1
            number = 0
        for letter in terminodebusqueda:   # Reemplaza el texto por & para no alterar los Id que se cuenten a posterioridad
            word = word + '&' 
        text = text.replace(terminodebusqueda, word)
        word = str()
    # print('\nMatches:\n', text, '\n')    # Control de matches.
    for (id, word) in dictionary.items():
        #print(id, word)
        if id >= 0:
            newtupple = (id, word)
            listafinal.append(newtupple)
    lista = sorted(listafinal)
    for extention, value in lista:
        newtupple = (value)
        li.append(newtupple)
    for value in li:
        string = string + str(value)
    string = string.replace(' , ', ', ').replace(' . ', '. ').replace(' : ', ': ').replace(' n ro. ', ' nro. ').replace(' s / ', ' s/').replace('/ ', '/').replace(' ; ', '; ').replace(' c o mo', ' como ').replace(' ene l ', ' en el ').replace(' ?', '?').replace(' !', '!').replace(' dirigir mea ',' dirigirme a ').replace('1 ','1').replace('2 ','2').replace('3 ','3').replace('4 ','4').replace('5 ','5').replace('6 ','6').replace('7 ','7').replace('8 ','8').replace('9 ','9').replace('0 ','0').replace(' del a ',' de la ')
    print('Texto generado:\n',string)
    print('\nTobiasCoding.\n')