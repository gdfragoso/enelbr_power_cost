import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .api import EnelBRPowerCostAPI
from .coordinator import EnelBRPowerCostCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configura a integração EnelBR-PowerCost baseada na UI (Config Entry)."""
    hass.data.setdefault(DOMAIN, {})

    api = EnelBRPowerCostAPI(hass)
    coordinator = EnelBRPowerCostCoordinator(hass, api, entry.data["operator"])
    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    _LOGGER.info("✅ Integração EnelBR-PowerCost configurada com sucesso!")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Remove a integração corretamente ao ser desinstalada."""
    if entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)

    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
