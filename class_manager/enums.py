from enum import Enum


class DeviceType(Enum):
    """Enum representing different types of devices."""
    MOTOR = "Motor"
    SENSOR = "Sensor"
    RELAY = "Relay"


class DeviceAction(Enum):
    """Enum representing possible actions that a device can perform."""
    ON = "on"
    OFF = "off"
    CHANGE_SPEED = "change_speed"
    CHANGE_PATH = "change_path"
    GET_VALUE = "get_value"


class SensorType(Enum):
    """Enum representing the types of sensors available."""
    LIGHT_SENSOR = "Light Sensor"
    CO2_SENSOR = "CO2 Sensor"
    SOIL_HUMIDITY_SENSOR = "Soil Humidity Sensor"
    AIR_HUMIDITY_AND_TEMPERATURE_SENSOR = "Air Temperature and Humidity Sensor"
