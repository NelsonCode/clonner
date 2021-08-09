from server import app, socketio
import click
from clonner import Clonner
import socket


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


@click.command()
@click.option('--url', default="", help='URL for clone website')
@click.option('--port', default=5000, help='PORT for runner server')
def hello(url, port):
    clonner = Clonner(url=url)
    output = clonner.clone()
    print(output)
    print(f"Listening to new connections in port http://{get_ip()}:{port}")
    socketio.run(app, host="0.0.0.0", port=port)


if __name__ == '__main__':
    hello()
