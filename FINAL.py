import random
import math

def normaliza (dic):
    novo_dic = {}
    for continente, paisinfo in dic.items():
        for pais, info in paisinfo.items():
            info['continente'] = continente
            novo_dic[pais] = info
    return novo_dic

def sorteia_pais (paises):
    listapaises = []
    for pais in paises.keys():
        listapaises.append(pais)
    paisescolhido = random.choice(listapaises)
    return paisescolhido

def adiciona_em_ordem (pais, distancia, lista):
    j = 0
    x = [pais, distancia]
    for i in lista:
        if distancia > i[1]:
            j = j + 1
    lista.insert(j, x)
    return lista

def esta_na_lista (pais, lista):
    esta = 0
    for i in lista:
        if pais == i[0]:
            esta = 1
    if esta == 1:
        return True
    else:
        return False

def sorteia_letra (palavra, lista_restrita):
    restritas = ['.', ',', '-', ';', ' ', "'"]
    palavra = palavra.lower()
    
    for i in lista_restrita:
        restritas.append(i)
    
    for j in palavra:
        if j in restritas:
            palavra = palavra.replace(j, '')
                
    if palavra == '':
        return ''
        
    letra = random.choice(palavra)
    
    while letra in restritas:
        letra = random.choice(palavra)
        
    return letra

def haversine(r, y1, x1, y2, x2):
    d = (r*2*math.atan2(math.sqrt(math.sin(math.radians(y2-y1)/2)**2+math.cos(math.radians(y1))*math.cos(math.radians(y2))*math.sin(math.radians(x2-x1)/2)**2),math.sqrt(1-(math.sin(math.radians(y2-y1)/2)**2+math.cos(math.radians(y1))*math.cos(math.radians(y2))*math.sin(math.radians(x2-x1)/2)**2))))
    return d

