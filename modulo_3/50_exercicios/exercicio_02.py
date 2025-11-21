def rotacionar_lista(lista_original: list, k):
    
# Evita rotações desnecessárias maiores que o tamanho da lista
    k = k % len(lista_original)
    
 # Pega os últimos k elementos da lista
    parte_final = lista_original[-k:]
    
 # Pega todos os elementos restantes (antes dos últimos k)
    parte_inicial = lista_original[:-k]
    
    lista_rotacionada = parte_final + parte_inicial
    
    return lista_rotacionada


numeros = [1, 2, 3, 4, 5]   
passos = 2                 

resultado = rotacionar_lista(numeros, passos)

print(f"Lista original: {numeros}")
print(f"Lista rotacionada {passos} posições à direita: {resultado}")

