import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required("operator"): str,
    }
)

class EnelBRPowerCostConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gerencia o fluxo de configuração da integração EnelBR Power Cost."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Passo inicial para a configuração pelo usuário."""
        errors = {}
        
        if user_input is not None:
            _LOGGER.info("🔧 Iniciando configuração com dados: %s", user_input)
            return self.async_create_entry(
                title="EnelBR Power Cost ⚡",
                data=user_input
            )

        _LOGGER.debug("📝 Exibindo formulário de configuração para o usuário.")
        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Retorna a classe de fluxo de opções."""
        return EnelBROptionsFlowHandler(config_entry)


class EnelBROptionsFlowHandler(config_entries.OptionsFlow):
    """Gerencia as opções da integração."""

    def __init__(self, config_entry):
        """Inicializa o fluxo de opções."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Gerencia a configuração das opções."""
        if user_input is not None:
            _LOGGER.info("⚙️ Atualizando opções da integração: %s", user_input)
            return self.async_create_entry(title="", data=user_input)

        _LOGGER.debug("📝 Exibindo formulário de opções para o usuário.")
        return self.async_show_form(step_id="init", data_schema=DATA_SCHEMA)
