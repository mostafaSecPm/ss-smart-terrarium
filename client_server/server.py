import json
from base_socket import BaseSocket
from typing import Dict, Union
import socket
class Server(BaseSocket):
    """Server class to handle incoming client connections."""

    def start_server(self) -> None:
        """Start the server to accept clients."""
        self.establish_connection()
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print("Server started. Waiting for clients...")

        client_socket, addr = self.socket.accept()
        print(f"Connection established with {addr}")
        self.handle_client(client_socket)

    def handle_client(self, client_socket: socket.socket) -> None:
        """Handle incoming client requests."""
        try:
            while True:
                self._socket = client_socket  # Set the client socket for the base methods
                request = self.receive_data()  # Use receive_data from BaseSocket
                if request:
                    print(f"Received request: {request}")  # Debug output
                    response = self.process_request(request)
                    self.send_message(response)  # Use send_message from BaseSocket
                else:
                    print("No request received, closing connection.")
                    break
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            self.close_connection()  # Close connection using BaseSocket
            print("Client socket closed.")

    def process_request(self, request: Dict[str, Union[int, str]]) -> Dict[str, Union[int, str, Dict]]:
        """Process the received request and generate a response."""
        if request["request_type"] == 1:
            device_id = request["device_id"]
            device_type = request["device_type"]
            return {'result_code': 0, 'error_message': '', 'data': {'message': f'Device of type {device_type} created'}}
        elif request["request_type"] == 2:
            device_id = request["device_id"]
            device_action = request["device_action"]
            value = request.get("value")
            return {'result_code': 0, 'error_message': '', 'data': {'message': f'Device {device_id} turned {device_action.lower()}'}}
        elif request["request_type"] == 3:
            device_id = request["device_id"]
            return {'result_code': 0, 'error_message': '', 'data': {'device_id': device_id, 'state': 'ON'}}
        else:
            return {'result_code': 1, 'error_message': 'Invalid request type', 'data': {}}

if __name__ == "__main__":
    server = Server('127.0.0.1', 65432)
    server.start_server()
