#!/usr/bin/env python3

import requests
import json
import datetime

# para descobrir o nome correto da sua operadora
# acesse https://dadosabertos.aneel.gov.br/dataset/tarifas-distribuidoras-energia-eletrica/resource/fcf2906c-7c32-4b9b-a637-054e7a5234f4
# digite o nome, confira o valor da coluna "SigAgente"
operadora = "COPEL-DIS"

hoje = datetime.date.today()
url = 'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search_sql?sql=SELECT * from "fcf2906c-7c32-4b9b-a637-054e7a5234f4" where "SigAgente"= \'{}\' and "DscBaseTarifaria"=\'Tarifa de Aplicação\' and "DscSubGrupo"=\'B1\' and "DscClasse"=\'Residencial\' and "DscModalidadeTarifaria"=\'Convencional\' and "DscSubClasse"=\'Residencial\' and "DscDetalhe"=\'Não se aplica\' and "DatFimVigencia" > \'{}\''.format(operadora, hoje) 


result = requests.get(url).json()
#print(json.dumps(result, indent=4))

if result['success']:
    r = result['result']['records'][0]
    valor_total = float(r['VlrTUSD'].replace(",", ".")) + float(r['VlrTE'].replace(",", "."))
    if r['DscUnidadeTerciaria'] == "MWh":
      valor_total = valor_total/1000
    print(valor_total)
