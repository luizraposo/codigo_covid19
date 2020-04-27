import requests
import json

req = None
def requisicao():
    try:
        req = requests.get('https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true')
        covid = req.json()
        return covid
    except:
        print('Erro na conexão')
        return None

covid = requisicao()



#def arquivo(covid):

 #   with open('covid19.json','w') as f:

 #       json.dump(covid,f)


#def carregar_covid(arquivo):

#   with open('covid19.json', 'r') as f:

#        return json.load(f)

#covid = (carregar_covid('covid19.json'))



def time(covid):

    time_ = f' lastUpdatedAtSource: {covid["lastUpdatedAtSource"]}'

    return time_


def total(covid):
    total_ = {'total' :
                  {'infectados':covid["infected"],
                   'mortos':covid["deceased"]}
              }
    return total_


estados = {}
evento = {}
for infectados in covid.get('infectedByRegion', dict()):


    estados[infectados.get('state')] = {}

    estados[infectados.get('state')]['infectados'] = infectados.get('count')

evento['estados'] = estados

for mortes in covid.get('deceasedByRegion', dict()):

    estados[mortes.get('state')]['mortes'] = mortes.get('count')


def sourceUrl(covid):

    sourceUrl_ = {'Url':covid["sourceUrl"]}

    return sourceUrl_


covid19 = []

covid19.append(time(covid))
covid19.append(total(covid))
covid19.append(evento)
covid19.append(sourceUrl(covid))

from pprint import pprint as pp

pp(covid19)
