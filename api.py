import logging
import aiohttp
from datetime import date

from .const import DOMAIN, API_HOST, TIMEOUT

_LOGGER = logging.getLogger(__name__)

class EnelBRPowerCostAPI:
    """Classe para requisição de dados da API da ANEEL de forma assíncrona."""

    def __init__(self, hass):
        """Inicializa a API com a sessão assíncrona do Home Assistant."""
        self.hass = hass
        self.session = aiohttp.ClientSession()

    async def get_tariff_cost(self, operator):
        """Obtém o custo da tarifa de energia elétrica de forma assíncrona."""
        today = date.today()
        url = (
            f"{API_HOST}/api/3/action/datastore_search_sql?"
            f"sql=SELECT * from \"fcf2906c-7c32-4b9b-a637-054e7a5234f4\" "
            f"where \"SigAgente\"= '{operator}' and \"DscBaseTarifaria\"='Tarifa de Aplicação' "
            f"and \"DscSubGrupo\"='B1' and \"DscClasse\"='Residencial' "
            f"and \"DscModalidadeTarifaria\"='Convencional' and \"DscSubClasse\"='Residencial' "
            f"and \"DscDetalhe\"='Não se aplica' and \"DatFimVigencia\" > '{today}'"
        )

        async with self.session.get(url, timeout=TIMEOUT) as response:
            data = await response.json()
            if data.get("success") and data["result"]["records"]:
                r = data["result"]["records"][0]
                total_value = float(r["VlrTUSD"].replace(",", ".")) + float(r["VlrTE"].replace(",", "."))
                if r["DscUnidadeTerciaria"] == "MWh":
                    total_value /= 1000
                return total_value
        return None

    async def get_tariff_flag(self):
        """Obtém a bandeira tarifária atual de forma assíncrona."""
        today = date.today()
        yearmonth = today.strftime("%Y-%m") + "-%"
        url = (
            f"{API_HOST}/api/3/action/datastore_search_sql?"
            f"sql=SELECT * from \"0591b8f6-fe54-437b-b72b-1aa2efd46e42\" "
            f"where \"DatCompetencia\" like '{yearmonth}'"
        )

        async with self.session.get(url, timeout=TIMEOUT) as response:
            data = await response.json()
            if data.get("success") and data["result"]["records"]:
                r = data["result"]["records"][-1]
                return r["NomBandeiraAcionada"]
        return None

    async def close(self):
        """Fecha a sessão assíncrona."""
        await self.session.close()