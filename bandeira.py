#!/usr/bin/env python3

import requests
import json
from datetime import date
from dateutil.relativedelta import relativedelta

def pegabandeira(anomes):
    url = 'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql?sql=SELECT * from "0591b8f6-fe54-437b-b72b-1aa2efd46e42" where "DatCompetencia" like \'{}\''.format(anomes)
    
    result = requests.get(url).json()
    #print(json.dumps(result, indent=4))
    
    if result['success']:
        if len(result['result']['records']) > 0:
            r = result['result']['records'][-1]
            datacompetencia = r['DatCompetencia']
            bandeira = r['NomBandeiraAcionada']
            valor = float(r['VlrAdicionalBandeira'].replace(",", "."))/1000
            output = '{{ "bandeira": "{}", "valor": "{}", "datacompetencia": "{}" }}'.format(bandeira, valor, datacompetencia)
            return output
        else:
            return {}

if __name__ == '__main__':
    today = date.today()
    anomes = today.strftime("%Y-%m") + '-%'
    bandeira = pegabandeira(anomes)
    if bandeira:
        print(bandeira)
    else:
        lastmonth = today - relativedelta(months=1)
        anomespassado = lastmonth.strftime("%Y-%m") + '-%'
        print(pegabandeira(anomespassado))