from typing import List, Optional, Union
from class_manager.device import Device
from class_manager.device_status import DeviceStatus
from class_manager.enums import SensorType
from class_manager.motor import Motor
from class_manager.relay import Relay
from class_manager.sensor import Sensor
from class_manager.enums import DeviceType, DeviceAction


class Manager:
    """Manager class to handle the creation, control, and status retrieval of devices."""

    def __init__(self) -> None:
        """Initialize the Manager with an empty devices list."""
        self.__devices: List[Device] = []

    @property
    def devices(self) -> List[Device]:
        """
        Get the list of devices managed by this Manager.

        Returns:
            List[Device]: The list of devices.
        """
        return self.__devices

    @devices.setter
    def devices(self, value: List[Device]) -> None:
        """
        Set the list of devices.

        Args:
            value (List[Device]): The list of devices to set.
        """
        if isinstance(value, list) and all(isinstance(d, Device) for d in value):
            self.__devices = value
        else:
            raise ValueError("Devices must be a list of Device objects.")

    def create_device(
        self,
        device_type: DeviceType,
        id: int,
        sensor_type: Optional[SensorType] = None
    ) -> str:
        """
        Create a new device and add it to the devices list.

        Args:
            device_type (DeviceType): The type of device to create.
            id (int): The ID of the device.
            sensor_type (Optional[SensorType]): The type of sensor, if the device is a sensor (optional).

        Returns:
            str: Confirmation message of device creation.
        """
        # Pass the sensor_type only if the device is a sensor, otherwise set it to None
        if device_type == DeviceType.SENSOR:
            device = Device.create(device_type, id, sensor_type)
        else:
            device = Device.create(device_type, id)

        self.devices.append(device)
        return f"A {device_type.value} created with id {id}"

    def control_device(
        self,
        id: int,
        action: DeviceAction,
        value: Optional[Union[int, str]] = None
    ) -> str:
        """
        Control a device by performing the specified action.

        Args:
            id (int): The ID of the device.
            action (DeviceAction): The action to perform on the device.
            value (Optional[Union[int, str]]): The value for the action, if applicable.

        Returns:
            str: Result of the action performed.

        Raises:
            ValueError: If the action is unknown or inappropriate for the device type.
        """
        device = next((d for d in self.devices if d.id == id), None)

        if device:
            if action == DeviceAction.ON:
                return device.on()
            elif action == DeviceAction.OFF:
                return device.off()
            elif action == DeviceAction.CHANGE_SPEED and isinstance(device, Motor):
                return device.perform_action(value)
            elif action == DeviceAction.CHANGE_PATH and isinstance(device, Relay):
                return device.perform_action(value)
            elif action == DeviceAction.GET_VALUE and isinstance(device, Sensor):
                sensor_value = device.perform_action()
                return f"Value of sensor {device.id}: {sensor_value}"
            else:
                raise ValueError(f"Unknown action or inappropriate device type for action: {action}")
        else:
            raise ValueError(f"Device with ID {id} does not exist.")

    def get_state(self, id: int) -> DeviceStatus:
        """
        Retrieve the status of a device by its ID.

        Args:
            id (int): The ID of the device.

        Returns:
            DeviceStatus: The status of the device.

        Raises:
            ValueError: If the device with the given ID does not exist.
        """
        device = next((d for d in self.devices if d.id == id), None)

        if device:
            return device.device_status()
        else:
            raise ValueError(f"Device with ID {id} does not exist.")
