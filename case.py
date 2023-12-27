
def soma_inteiros (lista, target):

    lista_2 = []

    for i in lista:

        complemento = target - i
        lista_2.append(i)

        if complemento in lista_2:
            pass

        elif complemento in lista: 
            return print(f"[{i}, {complemento}]")
        
        else:
            pass

    return -1

lista = [5,7,3,8,19,23,32,1]
target = 10

print(soma_inteiros(lista, target))



# def soma_inteiros (lista, target):

#     lista_2 = []

#     for i in lista:

#         complemento = target - i

#         if complemento in lista_2: 
#             return print(f"[{i}, {complemento}]")
#         else:
#             pass

#         lista_2.append(i)

#     return -1

# lista = [3,7,4,8,19,23,32,6]
# target = 10

# print(soma_inteiros(lista, target))



