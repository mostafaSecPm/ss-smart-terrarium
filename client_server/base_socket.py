import socket
import json
from typing import Dict, Union, Optional

class BaseSocket:
    """Base class for socket communication."""

    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._socket = None

    @property
    def host(self) -> str:
        """Get the host."""
        return self._host

    @host.setter
    def host(self, value: str) -> None:
        """Set the host."""
        self._host = value

    @property
    def port(self) -> int:
        """Get the port."""
        return self._port

    @port.setter
    def port(self, value: int) -> None:
        """Set the port."""
        self._port = value

    @property
    def socket(self) -> Optional[socket.socket]:
        """Get the socket."""
        return self._socket

    @socket.setter
    def socket(self, value: Optional[socket]) -> None:
        """Set the socket."""
        self._socket = value

    def establish_connection(self) -> None:
        """Establish a connection to the server or bind the server socket."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self, message: Dict[str, Union[int, str]]) -> None:
        """Send a JSON message to the server."""
        if self.socket is None:
            print("Socket not initialized.")
            return

        try:
            self.socket.sendall(json.dumps(message).encode('utf-8'))
        except socket.error as e:
            print(f"Error sending message: {e}")

    def receive_data(self) -> Optional[Dict[str, Union[int, str]]]:
        """Receive and decode a JSON response from the server."""
        if self.socket is None:
            print("Socket not initialized.")
            return None

        try:
            response = self.socket.recv(1024).decode('utf-8')
            if response:
                return json.loads(response)
            else:
                print("Connection broken or invalid request.")
                return None
        except socket.error as e:
            print(f"Error receiving data: {e}")
            return None

    def close_connection(self) -> None:
        """Close the connection to the server."""
        if self.socket:
            try:
                self.socket.close()
            except socket.error as e:
                print(f"Error closing connection: {e}")
