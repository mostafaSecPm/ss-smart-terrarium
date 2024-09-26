from typing import Optional

from class_manager.device import Device
from class_manager.device_status import DeviceStatus


class Relay(Device):
    """Concrete class representing a Relay device."""

    def __init__(self, id: int) -> None:
        """
        Initialize a Relay instance.

        Args:
            id (int): The ID of the relay.
        """
        self.__id = id
        self.__status = "off"
        self.__path = None

    @property
    def id(self) -> int:
        """Return the ID of the relay."""
        return self.__id

    @property
    def status(self) -> str:
        """Return the status of the relay."""
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        """
        Set the status of the relay.

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
    def path(self) -> Optional[int]:
        """Return the path of the relay."""
        return self.__path

    @path.setter
    def path(self, value: int) -> None:
        """
        Set the path of the relay.

        Args:
            value (int): The path to set (must be an integer between 1 and 4).

        Raises:
            ValueError: If the path is not an integer between 1 and 4.
        """
        if isinstance(value, int) and 1 <= value <= 4:
            self.__path = value
        else:
            raise ValueError("Path must be an integer between 1 and 4.")

    def on(self) -> str:
        """Turn the relay on and update its status."""
        self.status = "on"
        return f"Relay {self.id} is now ON."

    def off(self) -> str:
        """Turn the relay off and update its status."""
        self.status = "off"
        return f"Relay {self.id} is now OFF."

    def perform_action(self, path: int) -> str:
        """
        Set the relay path and return the change.

        Args:
            path (int): The path to set.

        Returns:
            str: Confirmation message of path change.
        """
        self.path = path
        return f"Path of relay {self.id} changed to {self.path}."

    def device_status(self) -> DeviceStatus:
        """
        Return the current status of the relay, including its path.

        Returns:
            DeviceStatus: The status of the relay.
        """
        return DeviceStatus(
            id=self.id,
            status=self.status,
            path=self.path
        )
