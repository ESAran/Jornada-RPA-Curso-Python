lista = [1,2,9,14,30]


# Versão destrinchada
def valores_menores(listain, valor):
  listafin = []
  for item in listain:
    if item < valor:
      listafin.append(item)
  
  return listafin
print(valores_menores(lista, 15))

# Versão compacta
def busca_list(lst, value):
    return [x for x in lst if x < value]
print(busca_list(lista, 15))
