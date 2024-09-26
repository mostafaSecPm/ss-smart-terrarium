from base_socket import BaseSocket
import socket
class Client(BaseSocket):
    """Client class to communicate with the server via socket."""

    def __init__(self, host: str, port: int) -> None:
        super().__init__(host, port)

    def connect(self) -> None:
        """Connect to the server."""
        self.establish_connection()
        try:
            self.socket.connect((self.host, self.port))
            print("Connected to the server.")
        except socket.error as e:
            print(f"Error connecting to server: {e}")

    def show_menu(self) -> None:
        """Display the menu and handle user choices."""
        while True:
            print("\nMenu:")
            print("1. Create Device")
            print("2. Control Device")
            print("3. Get Device State")
            print("4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_device()
            elif choice == '2':
                self.control_device()
            elif choice == '3':
                self.get_device_state()
            elif choice == '4':
                self.close_connection()
                break
            else:
                print("Invalid choice, try again.")

    def create_device(self) -> None:
        """Handle device creation."""
        print("Device Types:")
        print("1. MOTOR")
        print("2. SENSOR")
        print("3. RELAY")
        choice = input("Enter choice (1-3): ")

        device_type_map = {
            '1': 'MOTOR',
            '2': 'SENSOR',
            '3': 'RELAY'
        }

        device_type = device_type_map.get(choice)
        if device_type is None:
            print("Invalid choice.")
            return

        device_id = input("Enter device ID: ")
        message = {
            "request_type": 1,
            "device_id": device_id,
            "device_type": device_type
        }
        self.send_message(message)
        response = self.receive_data()
        if response:
            print(response)

    def control_device(self) -> None:
        """Handle controlling a device."""
        device_id = input("Enter device ID: ")

        print("You can:")
        print("1. Turn On")
        print("2. Turn Off")
        print("3. Change Speed")
        print("4. Change Path")
        choice = input("Enter choice (1-4): ")

        action_map = {
            '1': 'ON',
            '2': 'OFF',
            '3': 'CHANGE_SPEED',
            '4': 'CHANGE_PATH'
        }

        action = action_map.get(choice)
        if action is None:
            print("Invalid choice.")
            return

        value = None
        if action == 'CHANGE_SPEED':
            value = input("Enter speed (0-100): ")
        elif action == 'CHANGE_PATH':
            value = input("Enter path (0-3): ")

        message = {
            "request_type": 2,
            "device_id": device_id,
            "device_action": action,
            "value": value
        }
        self.send_message(message)
        response = self.receive_data()
        if response:
            print(response)

    def get_device_state(self) -> None:
        """Request and display the state of a device."""
        device_id = input("Enter device ID: ")
        message = {
            "request_type": 3,
            "device_id": device_id
        }
        self.send_message(message)
        response = self.receive_data()
        if response:
            print(response)

if __name__ == "__main__":
    client = Client('127.0.0.1', 65432)
    client.connect()
    client.show_menu()
