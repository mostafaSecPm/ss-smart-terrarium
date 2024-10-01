from class_manager.device import Device
from class_manager.device_status import DeviceStatus


class Motor(Device):
    """Concrete class representing a Motor device."""

    def __init__(self, id: int) -> None:
        """
        Initialize a Motor instance.

        Args:
            id (int): The ID of the motor.
        """
        self.__id = id
        self.__status = "off"
        self.__speed = 0

    @property
    def id(self) -> int:
        """Return the ID of the motor."""
        return self.__id

    @property
    def status(self) -> str:
        """Return the status of the motor."""
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        """
        Set the status of the motor.

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
    def speed(self) -> int:
        """Return the speed of the motor."""
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        """
        Set the speed of the motor.

        Args:
            value (int): The speed to set (must be non-negative).

        Raises:
            ValueError: If the speed is not within the range (0-100).
        """
        if 0 <= value <= 100:
            self.__speed = value
        else:
            raise ValueError("Speed must be between 0 and 100.")

    def on(self) -> str:
        """Turn the motor on and update its status."""
        self.status = "on"
        return f"Motor {self.id} is now ON."

    def off(self) -> str:
        """Turn the motor off and update its status."""
        self.status = "off"
        return f"Motor {self.id} is now OFF."

    def perform_action(self, speed: int) -> str:
        """
        Set the motor speed and return the change.

        Args:
            speed (int): The speed to set.

        Returns:
            str: Confirmation message of speed change.
        """
        self.speed = speed
        return f"Speed of motor {self.id} changed to {self.speed}."

    def device_status(self) -> DeviceStatus:
        """
        Return the current status of the motor, including its speed.

        Returns:
            DeviceStatus: The status of the motor.
        """
        return DeviceStatus(
            id=self.id,
            status=self.status,
            speed=self.speed
        )
