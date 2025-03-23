
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, SENSOR_TYPES, DEVICE_NAME, DEVICE_MANUFACTURER, DEVICE_MODEL

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Configuração da plataforma de sensores EnelBR-PowerCost no Home Assistant."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    sensors = [
        EnelBRPowerCostSensor(coordinator, sensor_key, sensor_data)
        for sensor_key, sensor_data in SENSOR_TYPES.items()
    ]

    async_add_entities(sensors, update_before_add=True)

    _LOGGER.info("✅ Sensores da integração EnelBR-PowerCost adicionados com sucesso!")

class EnelBRPowerCostSensor(CoordinatorEntity, SensorEntity):
    """Representação de um sensor EnelBR-PowerCost no Home Assistant."""

    def __init__(self, coordinator, sensor_key, sensor_data):
        """Inicializa o sensor EnelBR-PowerCost."""
        super().__init__(coordinator)

        self._sensor_key = sensor_key
        self._api_field = sensor_data["api_field"]
        self._attr_name = sensor_data["name"]
        self._attr_unique_id = sensor_key
        self._attr_device_class = sensor_data["device_class"]
        self._attr_state_class = sensor_data["state_class"]
        self._attr_native_unit_of_measurement = sensor_data["unit"]

        self._attr_device_info = {
            "identifiers": {(DOMAIN, "enelbr_powercost")},
            "name": DEVICE_NAME,
            "manufacturer": DEVICE_MANUFACTURER,
            "model": DEVICE_MODEL,
            "sw_version": "1.0",
        }

    @property
    def native_value(self):
        """Retorna o valor atualizado do sensor."""
        return self.coordinator.data.get(self._api_field, None)

    async def async_update(self):
        """Solicita uma atualização ao coordinator e aguarda novos dados."""
        
        _LOGGER.debug(f"🔄 Solicitando atualização para sensor {self._attr_name}...")

        new_value = self.coordinator.data.get(self._api_field)

        if new_value is not None:
            self._state = new_value
            _LOGGER.info(f"✅ Sensor {self._attr_name} atualizado para: {self._state} {self._attr_native_unit_of_measurement}")
        else:
            _LOGGER.warning(f"⚠️ Chave {self._api_field} não encontrada na resposta da API.")
