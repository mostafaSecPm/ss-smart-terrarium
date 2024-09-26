from class_manager.device import Device
from class_manager.device_status import DeviceStatus
from class_manager.enums import SensorType


class Sensor(Device):
    """Concrete class representing a Sensor device."""

    def __init__(self, id: int, sensor_type: SensorType) -> None:
        """
        Initialize a Sensor instance.

        Args:
            id (int): The ID of the sensor.
            sensor_type (SensorType): The type of the sensor.
        """
        self.__id = id
        self.__status = "off"
        self.__sensor_type = sensor_type
        self.__value = 0

    @property
    def id(self) -> int:
        """Return the ID of the sensor."""
        return self.__id

    @property
    def status(self) -> str:
        """Return the status of the sensor."""
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        """
        Set the status of the sensor.

        Args:
            value (str): The status to set (must be "on" or "off").

        Raises:
            ValueError: If the status is not "on" or "off".
        """
        if value in ["on", "off"]:
            self.__status = value
        else:
            raise ValueError("Status must be 'on' or 'off'.")

    @property
    def sensor_type(self) -> SensorType:
        """Return the type of the sensor."""
        return self.__sensor_type

    @property
    def value(self) -> float:
        """Return the value of the sensor."""
        return self.__value

    def on(self) -> str:
        """Turn the sensor on and update its status."""
        self.status = "on"
        return f"Sensor {self.id} is now ON."

    def off(self) -> str:
        """Turn the sensor off and update its status."""
        self.status = "off"
        return f"Sensor {self.id} is now OFF."

    def perform_action(self) -> float:
        """
        Return the current value of the sensor.

        Returns:
            float: The value of the sensor.
        """
        return self.value

    def device_status(self) -> DeviceStatus:
        """
        Return the current status of the sensor, including its type and value.

        Returns:
            DeviceStatus: The status of the sensor.
        """
        return DeviceStatus(
            id=self.id,
            status=self.status,
            sensor_type=self.sensor_type,
            value=self.value
        )
