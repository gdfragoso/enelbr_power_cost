from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from datetime import timedelta

DOMAIN = "enelbr_power_cost"
DEVICE_NAME = "EnelBR-PowerCost"
DEVICE_MANUFACTURER = "Enel Brasil"
DEVICE_MODEL = "Tariff Monitor V1"
DEVICE_ICON = "mdi:currency-usd"

API_HOST = "https://dadosabertos.aneel.gov.br"
TIMEOUT = 30
UPDATE_INTERVAL = timedelta(hours=24)

SENSOR_TYPES = {
    "enelbr_tariff_cost": {
        "name": "Custo da Tarifa",
        "api_field": "cost",
        "device_class": SensorDeviceClass.MONETARY,
        "state_class": SensorStateClass.MEASUREMENT,
        "unit": "BRL/kWh",
    },
    "enelbr_tariff_flag": {
        "name": "Bandeira Tarifária",
        "api_field": "brand",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
}