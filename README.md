# Integração EnelBR Power Cost para Home Assistant

## Visão Geral

A integração **EnelBR Power Cost** permite obter informações sobre a tarifa de energia elétrica e a bandeira tarifária vigente diretamente no Home Assistant. Os dados são obtidos a partir dos **Dados Abertos da ANEEL**.

## Recursos

- Obtém automaticamente a **bandeira tarifária vigente** (verde, amarela ou vermelha).
- Obtém o **custo da tarifa de energia elétrica** da distribuidora selecionada.
- **Atualização automática periódica** via Data Update Coordinator.
- **Integração via UI** no Home Assistant.

## Instalação

### 1. Adicione a Integração no Home Assistant

1. Copie a pasta `enelbr_power_cost` para dentro do diretório `custom_components` do seu Home Assistant.
2. Reinicie o Home Assistant para que a integração seja reconhecida.
3. Acesse **Configuração > Dispositivos & Serviços > Adicionar Integração**.
4. Pesquise por **EnelBR Power Cost** e clique para adicionar.

### 2. Preencha os Dados Necessários

- **Operadora de Energia**: O código da distribuidora de energia elétrica.

Para encontrar o código da sua operadora, acesse o site da ANEEL:

[Lista de Tarifas das Distribuidoras](https://www.aneel.gov.br)

Procure pelo nome da sua distribuidora e utilize o valor da coluna **SigAgente**.

## Sensores Criados

Após a configuração, dois sensores serão adicionados ao Home Assistant:

| **Sensor**                  | **Descrição**                                            |
|-----------------------------|----------------------------------------------------------|
| `sensor.enelbr_tariff_cost` | Mostra o custo da tarifa de energia elétrica (R$/kWh). |
| `sensor.enelbr_tariff_flag` | Mostra a bandeira tarifária atual (verde, amarela ou vermelha). |

## Atualização dos Dados

Os dados são atualizados periodicamente conforme definido no arquivo `const.py` pela variável `UPDATE_INTERVAL`.

## Contribuição

Se desejar contribuir com melhorias, relatórios de erro ou novas funcionalidades, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request** no repositório do projeto.