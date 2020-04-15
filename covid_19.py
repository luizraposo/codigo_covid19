import requests
import json
req = None
def requisicao(covid):
    try:
        req = requests.get(
            'https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true' + covid)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None

resultado = requisicao("covid")

# Retirando Colunas
del resultado['version']
del resultado['historyData']
del resultado['readMe']
del resultado['recovered']
del resultado['tested']
# Renomeando as colunas
resultado['URL'] = resultado.pop("sourceUrl")
resultado['Pais'] = resultado.pop("country")
resultado['ultima_atualizacao_no_Apify'] = resultado.pop("lastUpdatedAtApify")
resultado['ultima_atualizacao_na_fonte'] = resultado.pop("lastUpdatedAtSource")
resultado['Numero_de_Infectados'] = resultado.pop("infected")
resultado['Numero_de_Mortes'] = resultado.pop("deceased")
resultado['Infectados_Estado'] = resultado.pop("infectedByRegion")
resultado['Mortes_Estado'] = resultado.pop("deceasedByRegion")
# Criando variáveis
estados = resultado["Infectados_Estado"]
# Manipulando infectados e mortos
# itera na lista de infectados por estado para extrair o número de infectados
estados = {}
evento = {}
for infectados in resultado.get('Infectados_Estado', dict()):
    # cria um dicionário para cada estado
    estados[infectados.get('state')] = {}
    # adiciona dentro do dicionário de cada estado uma chave com o número de infectados
    estados[infectados.get('state')]['infectados'] = infectados.get('count')
evento['Totais'] = estados
# Manipulando infectados e mortos
for mortes in resultado.get('Mortes_Estado', dict()):
    estados[mortes.get('state')]['mortes'] = mortes.get('count')
# Adcionando a coluna evento
evento.update(resultado)
# Retirando Colunas
del evento['Infectados_Estado']
del evento['Mortes_Estado']
# Resultado Final
print(evento)