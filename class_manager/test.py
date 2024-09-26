from class_manager.enums import SensorType
from class_manager.manager import Manager
from class_manager.motor import Motor
from class_manager.relay import Relay
from class_manager.sensor import Sensor
from class_manager.enums import DeviceType, DeviceAction

def test_create_motor():
    manager = Manager()
    print("Testing Motor Creation...")
    result = manager.create_device(DeviceType.MOTOR, id=1)
    print(result)  # Should print: a Motor created with id 1
    motor = next(d for d in manager._Manager__devices if isinstance(d, Motor))
    print(f"Motor ID: {motor.id}")
    print(f"Motor Speed: {motor.speed}")
    print(f"Motor Status: {motor.status}")

def test_create_sensor():
    manager = Manager()
    print("Testing Sensor Creation...")
    result = manager.create_device(DeviceType.SENSOR, 2, SensorType.LIGHT_SENSOR)
    print(result)  # Should print: a Sensor created with id 2
    sensor = next(d for d in manager._Manager__devices if isinstance(d, Sensor))
    print(f"Sensor ID: {sensor.id}")
    print(f"Sensor Type: {sensor.sensor_type}")
    print(f"Sensor Value: {sensor.value}")
    print(f"Sensor Status: {sensor.status}")

def test_create_relay():
    manager = Manager()
    print("Testing Relay Creation...")
    result = manager.create_device(DeviceType.RELAY, id=3)
    print(result)  # Should print: a Relay created with id 3
    relay = next(d for d in manager._Manager__devices if isinstance(d, Relay))
    print(f"Relay ID: {relay.id}")
    print(f"Relay Path: {relay.path}")
    print(f"Relay Status: {relay.status}")

def test_control_motor_on():
    manager = Manager()
    manager.create_device(DeviceType.MOTOR, id=1)
    print("Testing Motor Control (ON)...")
    result = manager.control_device(1, DeviceAction.ON)
    print(result)  # Should print: Motor 1 is now ON.

def test_control_motor_change_speed():
    manager = Manager()
    manager.create_device(DeviceType.MOTOR, id=1)
    print("Testing Motor Speed Change...")
    result = manager.control_device(1, DeviceAction.CHANGE_SPEED, 20)
    print(result)  # Should print: Speed of motor 1 changed to 20

def test_control_sensor_on():
    manager = Manager()
    manager.create_device(DeviceType.SENSOR, id=2)
    print("Testing Sensor Control (ON)...")
    result = manager.control_device(2, DeviceAction.ON)
    print(result)  # Should print: Sensor 2 is now ON.

def test_control_sensor_get_value():
    manager = Manager()
    manager.create_device(DeviceType.SENSOR, id=2)
    print("Testing Sensor Value Retrieval...")
    result = manager.control_device(2, DeviceAction.GET_VALUE)
    print(result)  # Should print: Value of sensor 2: 0

def test_control_relay_on():
    manager = Manager()
    manager.create_device(DeviceType.RELAY, id=3)
    print("Testing Relay Control (ON)...")
    result = manager.control_device(3, DeviceAction.ON)
    print(result)  # Should print: Relay 3 is now ON.

def test_control_relay_change_path():
    manager = Manager()
    manager.create_device(DeviceType.RELAY, id=3)
    print("Testing Relay Path Change...")
    result = manager.control_device(3, DeviceAction.CHANGE_PATH, 2)
    print(result)  # Should print: Path of relay 3 changed to 2

def test_get_device_status():
    manager = Manager()
    manager.create_device(DeviceType.MOTOR, id=1)
    print("Testing Get Device Status...")
    status = manager.get_state(1)
    print(f"Device ID: {status.id}")
    print(f"Device Status: {status.status}")
    print(f"Device Speed: {status.speed}")
    print(f"Device Path: {status.path}")
    print(f"Device Sensor Type: {status.sensor_type}")
    print(f"Device Value: {status.value}")

if __name__ == "__main__":
    test_create_motor()
    test_create_sensor()
    test_create_relay()
    test_control_motor_on()
    test_control_motor_change_speed()
    test_control_sensor_on()
    test_control_sensor_get_value()
    test_control_relay_on()
    test_control_relay_change_path()
    test_get_device_status()
