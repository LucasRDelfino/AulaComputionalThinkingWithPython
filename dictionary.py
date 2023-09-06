from functions import acha_maior

parentes = {}
parentes['pai'] = 'Edson'
parentes['Mae'] = 'Adna'

for key in parentes.keys():
    print(f"O nome do/da seu/seu {key} é {parentes[key]}")


modelos = {'carros' : ['jetta','celta','uno de escada'],
           'precos'  : [1000 , 2000 , 3000]}

print(f"O carro mais caro é o {acha_maior(modelos['precos'],modelos['carros'])}")
maior = modelos['precos'][0]
indice_maior = 0



