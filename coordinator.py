import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import EnelBRPowerCostAPI
from .const import UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)

class EnelBRPowerCostCoordinator(DataUpdateCoordinator):
    """Gerencia as atualizações dos dados da API EnelBR."""

    def __init__(self, hass: HomeAssistant, api: EnelBRPowerCostAPI, operator: str):
        """Inicializa o coordenador com a API e recebe o operador."""
        self.api = api
        self.operator = operator
        super().__init__(
            hass,
            _LOGGER,
            name="EnelBR Data Coordinator",
            update_interval=UPDATE_INTERVAL,
        )

    async def _async_update_data(self):
        """Busca os dados mais recentes da API."""
        try:
            _LOGGER.info("🔄 Iniciando atualização dos dados da API EnelBR...")
            
            brand_data = await self.api.get_tariff_flag()
            cost_data = await self.api.get_tariff_cost(self.operator)
            
            if brand_data is None or cost_data is None:
                _LOGGER.error("❌ Falha ao buscar dados da API. Resposta vazia ou erro de autenticação.")
                raise UpdateFailed("Erro ao buscar dados da API.")

            return {
                "brand": brand_data,
                "cost": cost_data,
            }

        except Exception as err:
            _LOGGER.exception(f"❌ Erro inesperado ao buscar dados: {err}")
            raise UpdateFailed(f"Erro ao buscar dados da API: {err}")
