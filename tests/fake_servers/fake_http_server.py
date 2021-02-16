import socket
from http_server_mock import HttpServerMock

app = HttpServerMock(__name__)


def get_free_tcp_port():
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.bind(('', 0))
    addr, port = tcp_sock.getsockname()
    tcp_sock.close()
    return addr, port


@app.route("/RandomCity", methods=["GET"])
def get_weather():
    return "RandomCity: 🌨  +30°C"
