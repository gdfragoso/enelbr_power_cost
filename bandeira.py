#!/usr/bin/env python3

import requests
import json
import datetime

anomes = datetime.date.today().strftime("%Y-%m") + '-%'

url = 'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql?sql=SELECT * from "0591b8f6-fe54-437b-b72b-1aa2efd46e42" where "DatCompetencia" like \'{}\''.format(anomes)


result = requests.get(url).json()
#print(json.dumps(result, indent=4))

if result['success']:
    r = result['result']['records'][-1]
    bandeira = r['NomBandeiraAcionada']
    valor = float(r['VlrAdicionalBandeira'].replace(",", "."))/1000
    print('{{ "bandeira": "{}", "valor": "{}" }}'.format(bandeira, valor))